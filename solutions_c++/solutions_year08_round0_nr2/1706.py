#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

struct trip
{
	int beg,end;
	bool ab;
	bool operator<(const trip &z) const {return beg<z.beg;}
};

vector<trip> V;
priority_queue<int> Q[2];

void funk(int x)
{
	int c[2];
	c[0]=c[1]=0;
	for (int i=0; i<2; i++) while (Q[i].size()) Q[i].pop();
	V.resize(0);
	int trn;
	scanf("%d",&trn);
	int na,nb,h1,h2,m1,m2;
	scanf("%d%d\n",&na,&nb);
	while (na--)
	{
		scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
		m1+=(60*h1);
		m2+=(60*h2);
		trip tmp;
		tmp.beg = m1;
		tmp.end = m2;
		tmp.ab = 1;
		V.push_back(tmp);
	}
	while (nb--)
	{
		scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
		m1+=(60*h1);
		m2+=(60*h2);
		trip tmp;
		tmp.beg = m1;
		tmp.end = m2;
		tmp.ab = 0;
		V.push_back(tmp);
	}
	
	sort(V.begin(),V.end());

	int n = V.size();
	for (int i=0; i<n; i++)
	{
		bool ok=1;
		if (Q[V[i].ab].empty())
		{
			Q[V[i].ab].push(0);
			c[V[i].ab]++;
		}
		else
			if ((0-Q[V[i].ab].top())>V[i].beg) 
			{
				Q[V[i].ab].push(0);
				c[V[i].ab]++;
			}
		Q[V[i].ab].pop();
		Q[1^(V[i].ab)].push(0-(V[i].end+trn));
	}
	printf("Case #%d: %d %d\n",x,c[1],c[0]);
}

int main()
{
	int j;
	scanf("%d",&j);
	for (int i=0; i<j; i++) funk(i+1);
	return 0;
}



