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

const int MOD = 10007;
const int MAX_H = 200;
const int MAX_W = 200;

int H, W, R, a[MAX_H][MAX_W], dp[MAX_H][MAX_W], ans;

void Read()
{
	memset(a, 0, sizeof(a));
	memset(dp, 0, sizeof(dp));
	
	scanf("%d %d %d", & H, & W, & R);
	
	for(int i = 0, r, c; i < R; i ++)
	{
		scanf("%d %d", & r, & c);
		
		a[r][c] = 1;
	}
}

void Solve()
{
	dp[1][1] = 1;
	
	for(int h = 1; h <= H; h ++)
	{
		for(int w = 1; w <= W; w ++)
		{
			if(a[h][w]) continue;
			
			for(int i = 0; i <= 5; i ++)
			{
				for(int j = 0; j <= 5; j ++)
				{
					int new_h = h - i;
					int new_w = w - j;
					
					if(!(1 <= new_h && new_h < h)) continue;
					if(!(1 <= new_w && new_w < w)) continue;
					if((h - new_h) * (h - new_h) + (w - new_w) * (w - new_w) != 5) continue;
					
					dp[h][w] += dp[new_h][new_w];
					
					if(MOD <= dp[h][w])
					{
						dp[h][w] -= MOD;
					}
				}
			}
		}
	}
	
	ans = dp[H][W];
}

void Write(const int test_case)
{
	printf("Case #%d: %d\n", test_case, ans);
}

int main()
{
int TESTS;
	
	scanf("%d", & TESTS);
	
	for(int i = 1; i <= TESTS; i ++)
	{
		Read();
		
		Solve();
		
		Write(i);
	}
	
//	system("pause");
	
	return 0;
}
