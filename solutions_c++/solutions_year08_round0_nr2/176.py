#include <iostream>
#include <vector>
#include <queue>
using namespace std;



priority_queue<int> Que[2];
vector< pair< pair<int, int>, int> > HS;

int main()
{

	int __an, __bn, i, N, T, ctr = 0, hold, hold2, m, j, g;
	char ch;
	freopen("B_L.in", "r", stdin);
	freopen("B_L.out", "w", stdout);
     scanf("%d", &N);
	
	while (N--)
	{
		scanf("%d", &T);
		scanf("%d%d", &__an, &__bn);
			HS.clear();
			//TA.clear();
			for(j = 0; 2 - j; ++j)
			for (i = 0; i < (j ? __bn : __an); ++i)
            {
				scanf("%d%c%d", &hold, &ch, &m);
				hold = hold * 60 + m;
				scanf("%d%c%d", &hold2, &ch, &m);
				hold2 = hold2 * 60 + m;
				HS.push_back(make_pair( pair<int, int>(hold, hold2), j) );
			}

		

			sort(HS.begin(), HS.end());
             while(Que[0].size()) Que[0].pop();
             while(Que[1].size()) Que[1].pop();

			int res[2] = {0, 0};


			for (i = 0; i < __an + __bn; ++i)
			{
				g = HS[i].second;
				//int t = -Q[g].top();
				if ( Que[g].empty() || ( (-Que[g].top()) > HS[i].first.first) )
					++res[g];
				else
					Que[g].pop();


				Que[g ^ 1].push( -(HS[i].first.second + T) );
			}
            printf("Case #%d: %d %d\n", ++ctr, res[0], res[1]);
	}
}
/*
10
5
3 2
09:00 12:00
10:00 13:00
11:00 12:30
12:02 15:00
09:00 10:30
2
2 0
09:00 09:01
12:00 12:02
*/
