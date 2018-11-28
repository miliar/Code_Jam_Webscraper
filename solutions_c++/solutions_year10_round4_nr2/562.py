#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
using namespace std;
const int oo = 1000000000; 
int dp[11][2048][11];
int p;
int a[2048];
int c[11][2048];

void init()
{
    scanf("%d", &p);
    for (int i = 0; i < (1<<p); i++) 
	{
        scanf("%d", &a[i]);
        for (int j = 0; j <= a[i]; j++)
            dp[0][i][j] = 0;

        for (int j = a[i] + 1;j <= p + 1; j++)
            dp[0][i][j] = oo;
    }
    int len = 1 << (p - 1);
    for (int i = 1;i <= p; i++) 
	{
        for (int j = 0; j < len; j++) 
            scanf ( "%d", &c[i][j]);
        len = len / 2;
    }
}

void process()
{
    int len = 1 << (p - 1);
    for (int i = 1; i <= p; i++) 
	{
        for (int j = 0; j < len; j++) 
		{
            for (int k = p;k >= 0; k--) 
			{
                dp[i][j][k] = oo;
                if (k < p) 
                    dp[i][j][k] = dp[i - 1][j * 2][k + 1] + dp[i - 1][j * 2 + 1][k + 1];

                if (dp[i][j][k] > dp[i - 1][j * 2][k] + dp[i - 1][j * 2 + 1][k] + c[i][j]) 
                    dp[i][j][k] = dp[i - 1][j * 2][k] + dp[i - 1][j * 2 + 1][k] + c[i][j];

                if ((dp[i][j][k] > dp[i][j][k + 1]) && (k < p)) 
                    dp[i][j][k] = dp[i][j][k + 1];

                if (dp[i][j][k] > oo)
                    dp[i][j][k] = oo;
            }
        }
        len = len / 2;
    }
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int test;
    scanf("%d", &test);
    for (int i = 1; i <= test; i++) 
	{
        init();
        process();
		printf ( "Case #%d: %d\n", i, dp[p][0][0]);
    }
}
