#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <cmath>
#include <bitset>
#include <cctype>
using namespace std;

const int MAX_M = 100000;
const int INF = 100000000;

typedef struct node
{
	int G, C;
};

int M, V, ans;
node tree[MAX_M];
int dp[MAX_M][2];

void Read()
{
	for(int i = 0; i < MAX_M; i ++)
	{
		dp[i][0] = dp[i][1] = INF;
		tree[i].G = tree[i].C = 0;
	}
	
	scanf("%d %d", & M, & V);
	
	for(int i = 1; i <= (M - 1) / 2; i ++)
	{
		scanf("%d %d", & tree[i].G, & tree[i].C);
	}
	
	for(int i = (M - 1) / 2 + 1; i <= M; i ++)
	{
		scanf("%d", & tree[i].G);
		dp[i][tree[i].G] = 0;
	}
}

void Solve()
{
	for(int node = M; 3 <= node; node -= 2)
	{
		if(tree[node / 2].C == 0)
		{
			if(tree[node / 2].G == 0)
			{
				dp[node / 2][0] = min(dp[node / 2][0], dp[node][0] + dp[node - 1][0]);
				dp[node / 2][1] = min(dp[node / 2][1], dp[node][0] + dp[node - 1][1]);
				dp[node / 2][1] = min(dp[node / 2][1], dp[node][1] + dp[node - 1][0]);
				dp[node / 2][1] = min(dp[node / 2][1], dp[node][1] + dp[node - 1][1]);
			}
			else
			{
				dp[node / 2][0] = min(dp[node / 2][0], dp[node][0] + dp[node - 1][0]);
				dp[node / 2][0] = min(dp[node / 2][0], dp[node][0] + dp[node - 1][1]);
				dp[node / 2][0] = min(dp[node / 2][0], dp[node][1] + dp[node - 1][0]);
				dp[node / 2][1] = min(dp[node / 2][1], dp[node][1] + dp[node - 1][1]);
			}
		}
		else
		{
			if(tree[node / 2].G == 0)
			{
				dp[node / 2][0] = min(dp[node / 2][0], dp[node][0] + dp[node - 1][0]);
				dp[node / 2][1] = min(dp[node / 2][1], dp[node][0] + dp[node - 1][1]);
				dp[node / 2][1] = min(dp[node / 2][1], dp[node][1] + dp[node - 1][0]);
				dp[node / 2][1] = min(dp[node / 2][1], dp[node][1] + dp[node - 1][1]);
				
				dp[node / 2][0] = min(dp[node / 2][0], 1 + dp[node][0] + dp[node - 1][0]);
				dp[node / 2][0] = min(dp[node / 2][0], 1 + dp[node][0] + dp[node - 1][1]);
				dp[node / 2][0] = min(dp[node / 2][0], 1 + dp[node][1] + dp[node - 1][0]);
				dp[node / 2][1] = min(dp[node / 2][1], 1 + dp[node][1] + dp[node - 1][1]);
			}
			else
			{
				dp[node / 2][0] = min(dp[node / 2][0], 1 + dp[node][0] + dp[node - 1][0]);
				dp[node / 2][1] = min(dp[node / 2][1], 1 + dp[node][0] + dp[node - 1][1]);
				dp[node / 2][1] = min(dp[node / 2][1], 1 + dp[node][1] + dp[node - 1][0]);
				dp[node / 2][1] = min(dp[node / 2][1], 1 + dp[node][1] + dp[node - 1][1]);
				
				dp[node / 2][0] = min(dp[node / 2][0], dp[node][0] + dp[node - 1][0]);
				dp[node / 2][0] = min(dp[node / 2][0], dp[node][0] + dp[node - 1][1]);
				dp[node / 2][0] = min(dp[node / 2][0], dp[node][1] + dp[node - 1][0]);
				dp[node / 2][1] = min(dp[node / 2][1], dp[node][1] + dp[node - 1][1]);
			}
		}
	}
	
	ans = dp[1][V];
}

int main()
{
int TESTS;
	
	scanf("%d", & TESTS);
	
	for(int i = 1; i <= TESTS; i ++)
	{
		Read();
		
		Solve();
		
		if(ans == INF) printf("Case #%d: IMPOSSIBLE\n", i);
		else printf("Case #%d: %d\n", i, ans);
	}
//	system("pause");
	
	return 0;
}

/*
1
9 1
1 0
1 1
1 1
0 0
1
0
1
0
1
*/
