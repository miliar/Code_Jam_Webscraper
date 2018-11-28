#include <iostream>
#include <sstream>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()

typedef unsigned long long ull;
typedef long long lint;
typedef pair < int , int > pii;
typedef long double ld;

const int inf = 2000 * 1000 * 1000;
const lint linf = 2000000000000000000LL;
const double eps = 1e-9;

void prepare( )
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
}

struct pos
{
	int len,x,y;
	pos( int a, int X, int Y )
	{
		len = a;
		x = X;
		y = Y;
	}
	pos()
	{
	}
};

queue < pos > q;
int dp[105][105][105];
int a[105];
int f[105];
int n;

bool solve( )
{
	char c;
	int x;
	scanf("%d",&n);
	for ( int i = 0; i < n; i ++ )
	{
		scanf(" %c %d",&c,&x);
		f[i] = c == 'O';
		a[i] = x;
	}
	scanf("\n");
	_(dp,-1);
	dp[0][1][1] = 0;
	q.push(pos(0,1,1));
	int ans = inf;
	pos t;
	while (!q.empty())
	{
		t = q.front();
		q.pop();
		if ( t.len == n )
		{
			ans = min(ans,dp[t.len][t.x][t.y]);
		}

		if (f[t.len] == 0 && a[t.len] == t.x)
		{
			for ( int dy = -1; dy < 2; dy ++ )
			{
				int ny = t.y + dy;
				if ( ny > 0 && ny <= 100 )
				{
					if ( dp[t.len+1][t.x][ny] == -1 )
					{
						dp[t.len+1][t.x][ny] = dp[t.len][t.x][t.y] + 1;
						q.push(pos(t.len+1,t.x,ny));
					}
				}
			}
		}
		if (f[t.len] == 1 && a[t.len] == t.y)
		{
			for ( int dx = -1; dx < 2; dx ++ )
			{
				int nx = t.x + dx;
				if ( nx > 0 && nx <= 100 )
				{
					if ( dp[t.len+1][nx][t.y] == -1 )
					{
						dp[t.len+1][nx][t.y] = dp[t.len][t.x][t.y] + 1;
						q.push(pos(t.len+1,nx,t.y));
					}
				}
			}
		}

		for ( int dx = -1; dx < 2; dx ++ )
		{
			int nx = t.x + dx;
			if ( t.x > 0 && t.x <= 100 )
			{
				for ( int dy = -1; dy < 2; dy ++ )
				{
					int ny = t.y + dy;
					if ( ny > 0 && ny <= 100 )
					{
						if ( dp[t.len][nx][ny] == -1 )
						{
							dp[t.len][nx][ny] = dp[t.len][t.x][t.y] + 1;
							q.push(pos(t.len,nx,ny));
						}
					}
				}
			}
		}
	}
	printf("%d\n",ans);
	return false;
}

int main()
{
	prepare( );
	int t;
	scanf("%d\n",&t);
	for ( int i = 0; i < t; i ++ )
	{
		printf("Case #%d: ",i+1);
		solve();
	}
	return 0;
}