#include<cstdio>
#include<algorithm>
#include<vector>
#include<queue>

using namespace std;

int inter;
vector<pair<int, char> > stamp;
int cntA=0,cntB=0;

void solve()
{
	priority_queue<int, vector<int>, greater<int> > A;
	priority_queue<int, vector<int>, greater<int> > B;

		// 0 arriva at A
		// 1 arrive at B

		// 2 leave from A
		// 3 leave from B
	cntA=0,cntB=0;
	for(int i=0; i<stamp.size(); ++i)
	{
		switch(stamp[i].second)
		{
		case 0: 
			A.push(stamp[i].first);
			break;
		case 1:
			B.push(stamp[i].first);
			break;
		case 2:
			if(A.empty() || A.top()+inter > stamp[i].first)
				cntA++;
			else
				A.pop();
			break;
		case 3:
			if(B.empty() || B.top()+inter > stamp[i].first)
				cntB++;
			else
				B.pop();
			break;
		}
	}
	
}
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int numCase;
	scanf("%d", &numCase);

	for(int c=0; c<numCase; c++)
	{
		scanf("%d", &inter);
		int na, nb;
		scanf("%d%d", &na, &nb);
		char ta[10],tb[10];
		int hh, mm;
		
		
		stamp.clear();
		// 0 arriva at A
		// 1 arrive at B

		// 2 leave from A
		// 3 leave from B

		for(int i=0; i<na; ++i)     // trip A to B
		{
			scanf("%s %s", ta,tb);

			sscanf(ta, "%d:%d",&hh, &mm);
			stamp.push_back(make_pair(hh*60+mm, 2));  

			sscanf(tb, "%d:%d",&hh, &mm);
			stamp.push_back(make_pair(hh*60+mm, 1));
		}

		for(int i=0; i<nb; i++)
		{
			scanf("%s %s", ta,tb);

			sscanf(ta, "%d:%d",&hh, &mm);
			stamp.push_back(make_pair(hh*60+mm, 3));

			sscanf(tb, "%d:%d",&hh, &mm);
			stamp.push_back(make_pair(hh*60+mm, 0));
		}
		sort(stamp.begin(), stamp.end());

		solve();
		printf("Case #%d: %d %d\n", c+1, cntA, cntB);
	}

	return 0;
}
