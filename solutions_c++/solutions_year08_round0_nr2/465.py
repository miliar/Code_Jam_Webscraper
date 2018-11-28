#include <iostream>
#include <queue>
#include <cstdio>
#include <vector>

using namespace std;

inline int getTime(int h, int m)
{
	return h*60+m;
}


vector<pair<int,int> > na;
vector<pair<int,int> > nb;

priority_queue<int> qna;
priority_queue<int> qnb;

int runNa(int index)
{
	int res = 0;
	if (qna.size() == 0)
	{
		qna.push(1);
		res++;
	}
	if (-qna.top() > na[index].first)
	{
		qna.push(1);
		res++;
	}
	qnb.push(-na[index].second);
	qna.pop();
	return res;
}
int runNb(int index)
{
	int res = 0;
	if (qnb.size() == 0)
	{
		qnb.push(1);
		res++;
	}
	if (-qnb.top() > nb[index].first)
	{
		qnb.push(1);
		res++;
	}
	qna.push(-nb[index].second);
	qnb.pop();
	return res;
}


int main()
{
	freopen("a.txt", "w", stdout);
	freopen("text.txt", "r", stdin);
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++)
	{
		cerr << t << endl;
		na.clear();
		nb.clear();
		while (qna.empty() == false)
			qna.pop();
		while (qnb.empty() == false)
			qnb.pop();
		int time;
		scanf("%d", &time);
		int NA, NB;
		scanf("%d%d", &NA, &NB);
		for (int i=0; i<NA; i++)
		{
			int a,b;
			int s,f;
			scanf("%d:%d", &a,&b);
			s = getTime(a,b);
			scanf("%d:%d", &a,&b);
			f = getTime(a,b)+time;
			na.push_back(make_pair(s,f));
		}
		for (int i=0; i<NB; i++)
		{
			int a,b;
			int s,f;
			scanf("%d:%d", &a,&b);
			s = getTime(a,b);
			scanf("%d:%d", &a,&b);
			f = getTime(a,b)+time;
			nb.push_back(make_pair(s,f));
		}
		sort(na.begin(), na.end());
		sort(nb.begin(), nb.end());
		int naIndex = 0;
		int nbIndex = 0;
		int naRes = 0;
		int nbRes = 0;

		while (true)
		{
			if (naIndex >= NA && nbIndex >= NB)
				break;
			if (naIndex < NA && nbIndex < NB)
			{
				if (na[naIndex].first < nb[nbIndex].first)
				{
					naRes += runNa(naIndex);
					naIndex++;
				}
				else
				{
					nbRes += runNb(nbIndex);
					nbIndex++;
				}
				continue;
			}
			if (naIndex >= NA)
			{
				nbRes += runNb(nbIndex);
				nbIndex++;
				continue;
			}
			if (nbIndex >= NB)
			{
				naRes += runNa(naIndex);
				naIndex++;
				continue;
			}
		}

		printf("Case #%d: %d %d\n", t, naRes, nbRes);
	}
	return 0;
}