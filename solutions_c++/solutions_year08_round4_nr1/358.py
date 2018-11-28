#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int m, v;
int G[10111], C[10111], L[10111], T[10111];

int dp[10111][2];
const int inf = 99999;
int dfs(int u, int c)
{
	if(T[u] == 1)
	{
		if(L[u] == c) dp[u][c] = 0;
		else dp[u][c] = inf;
	} else
	{
		int r10 = dfs(2*u+1, 0);
		int r11 = dfs(2*u+1, 1);
		int r20 = dfs(2*u+2, 0);
		int r21 = dfs(2*u+2, 1);
		if(G[u] == 1) // and
		{
			if(C[u] == 0)
			{
				if(c == 1)
				{
					dp[u][c] = r11 + r21;
				} else
				{
					dp[u][c] = min( min(r10 + r20, r10 + r21), r11 + r20 );
				}
			} else
			{
				if(c == 1)
				{
					dp[u][c] = min(r11 + r21, 1 + min( min(r11+r20, r11+r21),r10+r21 ) );
				} else
				{
					dp[u][c] = min(min( min(r10 + r20, r10 + r21), r11 + r20 ),
								  1+r10 + r20
								);
				}
			}
		} else  // or
		{
			if(C[u] == 0)
			{
				if(c == 1)
				{
					dp[u][c] = min(min(r11 + r21, r10 + r21), r11 + r20);
				} else
				{
					dp[u][c] = r10 + r20;
				}
			} else
			{
				if(c == 1)
				{
					dp[u][c] = min(min(min(r11 + r21, r10 + r21), r11 + r20), 
							   1 + r11 + r21);
				} else
				{
					dp[u][c] = min(r10 + r20,
									1+min(min(r11 + r20, r10 + r21), r10 + r20));
				}
			}
		}
	}
	return dp[u][c];
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t; cin >> t;
	for(int z = 1; z <= t; ++z)
	{
		cin >> m >> v;
		memset(G, 0, sizeof G);
		memset(C, 0, sizeof C);
		for(int i = 0; i < (m-1)/2; ++i)
		{
			cin >> G[i] >> C[i];
			T[i] = 0;
		}
		int q = (m - 1) / 2;
		for(int i = 0; i < (m+1)/2; ++i)
		{
			T[q + i] = 1;
			cin >> L[q + i];
		}
		for(int i = 0; i < 10111; ++i)
			dp[i][0] = dp[i][1] = inf;
		int res = dfs(0, v);
		cout << "Case #" << z << ": ";
		if(res < inf) cout << res << endl;
		else cout << "IMPOSSIBLE" << endl;
	}

	return 0;
}