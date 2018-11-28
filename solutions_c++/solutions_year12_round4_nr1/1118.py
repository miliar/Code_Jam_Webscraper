
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
int di [1000000];
int le [1000000];
int dp[1000000];
int vis[1000000];
using namespace std;
    int main()
        {
			freopen("input.txt","rt", stdin);
			freopen("output.txt","wt", stdout);
			int tests;
			scanf("%d",&tests);
			for (int test = 1; test <= tests; test++)
			{
				//scanf("")
				int n;
				scanf("%d", &n);
				for (int i = 0; i < n; i++)
				{
					scanf("%d", &di[i]);
					scanf("%d", &le[i]);
				
				}
				int res;
				scanf("%d", &res);
				di[n] = res;
				le[n] = 0;
				int mn = 1000000000+200;
				for (int i = 0; i <= n; i++)
				{
					dp[i] = mn;
					vis[i] = 0;
				}
				dp[0] = 0;
				vis[0] = 0;
				while (1)
				{
					int besti = -1;
					int best = mn;
					for (int i = 0; i < n; i++)
						if(vis[i]==0)
							if (dp[i] < best)
							{
								besti = i;
								best = dp[i];
							}
					if (besti == -1)
						break;
					vis[besti] = 1;
					int i = besti;
					for (int j = 0; j < n; j++)
						if (!vis[j])
						{
							//climbup and jump
							//dp - leftmost coordinate
							if (di[j] < di[besti])
								continue;
							
							int nbest = di[j] - le[j];
							nbest = max(di[j] - le[j], di[besti]);
							//if (nbest < di[besti])
								//nbest = di[besti];
							/*
							int delta = di[besti] - dp[besti];
							int t = dp[besti]+delta*2 - di[j];
							int cc = di[j] - t;
							nbest = max(cc, nbest);
							*/
							
							if (di[j] > di[besti] + di[besti] -dp[besti])
								continue;
							//printf("asf   %d  %d\n", j, nbest);
							//printf("di    %d  %d\n", di[j], dp[besti]);
							dp[j] = min(dp[j], nbest);

						}
				}
				int bad = 0;
				for (int i = 0; i < n; i++)
					if (vis[i])
					{
						if (di[i] + di[i]-dp[i] >= res)
							bad = 1;
					}
				

				printf("Case #%d: ",test);				
				if (bad == 0)
					printf("NO\n");
				else
					printf("YES\n");

			}



			
        } 
    // END CUT HERE 
