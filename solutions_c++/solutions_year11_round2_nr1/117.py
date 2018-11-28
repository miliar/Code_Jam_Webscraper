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
}

int n;
char f[105][105];
double wp[105];
double owp[105];
double oowp[105];

double calc1( int x )
{
	double ret = 0;
	int c = 0;
	for ( int i = 0; i < n; i ++ )
	{
		if ( i != x && f[x][i] != '.' )
		{
			c ++;
			if ( f[x][i] == '1' )
				ret += 1.0;
		}
	}
	return ret / (double) c;
}

double calc2( int x )
{
	double ret = 0;
	int cc = 0;
	for ( int i = 0; i < n; i ++ )
	{
		if ( i != x && f[x][i] != '.' )
		{
			cc ++;
			double r1 = 0;
			int c = 0;
			for ( int j = 0; j < n; j ++ )
			{
				if ( i != j && j != x && f[i][j] != '.' )
				{
					c ++;
					if ( f[i][j] == '1' )
					{
						r1 += 1.0;
					}
				}
			}
			ret += r1 / (double) c;
		}
	}
	return ret / (double)cc;
}

double calc3( int x )
{
	double ret = 0;
	int cc = 0;
	for ( int i = 0; i < n; i ++ )
	{
		if ( i != x && f[x][i] != '.' )
		{
			cc ++;
			ret += owp[i];
		}
	}
	return ret / (double)cc;
}

bool solve( )
{
	scanf("%d\n",&n);
	for ( int i = 0; i < n; i ++ )
		scanf("%s\n",f[i]);
	for ( int i = 0; i < n; i ++ )
		wp[i] = calc1(i);
	for ( int i = 0; i < n; i ++ )
		owp[i] = calc2(i);
	for ( int i = 0; i < n; i ++ )
		oowp[i] = calc3(i);
	for ( int i = 0; i < n; i ++ )
	{
		printf("%.9lf\n",0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i]);
	}
	return false;
}

int main()
{
	prepare( );
	int t;
	scanf("%d\n",&t);
	for ( int i = 0; i < t; i ++ )
	{
		printf("Case #%d:\n",i+1);
		solve();
	}
	return 0;
}