#include <cstdio>
#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <cctype>
#include <memory.h>
using namespace std;

int res[100];
int ans;

int matr[32][32];
int dp[32][32];
int g[32][32];
int v[32][32];

int n, m;

bool process()
{
	for (int i = n-1; i >= 0; --i)
	{
		dp[i][m-1] = 1;
		v[i][m-1] = 1;
		g[i][m-1] = 1;
	}
	for (int j = m-1; j >= 0; --j)
	{
		dp[n-1][j] = 1;
		v[n-1][j] = 1;
		g[n-1][j] = 1;
	}

	int size = 0;
	int x, y;

	for (int i = n-2; i >= 0; --i)
	{
		for (int j = m-2; j >= 0; --j)
		{
			if ( matr[i][j] == -1 )
			{
				dp[i][j] = 0;
				v[i][j] = 0;
				g[i][j] = 0;
				continue;
			}

			if ( matr[i][j] != matr[i][j+1] )
				g[i][j] = g[i][j+1] + 1;
			else
				g[i][j] = 1;
			if ( matr[i][j] != matr[i+1][j] )
				v[i][j] = v[i+1][j] + 1;
			else
				v[i][j] = 1;
			if ( matr[i][j] == matr[i+1][j+1] )
			{
				dp[i][j] = min(g[i][j], v[i][j]);
				dp[i][j] = min(dp[i][j], dp[i+1][j+1] + 1);
			}
			else
			{
				dp[i][j] = 1;
			}
			if ( dp[i][j] >= size )
			{
				size = dp[i][j];
				y = i;
				x = j;
			}
		}
	}

	if ( size > 1 )
	{
		res[size]++;
		for (int i = y; i < y + size; ++i)
		{
			for (int j = x; j < x + size; ++j)
			{
				matr[i][j] = -1;
			}
		}		
	}
	else
	{
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < m; ++j)
			{
				if ( matr[i][j] != -1 )
				{
					res[1]++;
				}
			}
		}
		return true;
	}
	
	return false;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		memset(res, 0, sizeof(res));
		ans = 0;

		scanf("%d %d\n", &n, &m);

		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < m/4; ++j)
			{
				char ch = getchar();
				if ( isdigit(ch) ) ch -= '0';
				else 
				{
					switch (ch )
					{
					case 'A':
						ch = 10;
						break;
					case 'B':
						ch = 11;
						break;
					case 'C':
						ch = 12;
						break;
					case 'D':
						ch = 13;
						break;
					case 'E':
						ch = 14;
						break;
					case 'F':
						ch = 15;
						break;
					}
				}

				for (int h = 3; h >= 0; --h)
				{
					matr[i][j*4+3-h] = (bool) (ch & (1<<h));
				}
			}
			getchar();
		}

		while (!process()) {}

		for (int r = 32; r >= 1; --r)
		{
			if ( res[r] )
			{
				ans++;
			}
		}
	
		printf("Case #%d: %d\n", t+1, ans);
		for (int r = 32; r >= 1; --r)
		{
			if ( res[r] )
			{
				printf("%d %d\n", r, res[r]);
			}
		}

	}



	return 0;
}