#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <functional>
#include <map>
#include <set>
#include <sstream>
#include <deque>
#include <iostream>

using namespace std;

#define fo(a,b,c) for(a=(b);a<(c);++a)
#define fr(a,b) fo(a,0,(b))
#define fi(a) fr(i,(a))
#define fj(a) fr(j,(a))
#define fk(a) fr(k,(a))
#define all(a) (a).begin(),(a).end( )
#define sz(a) (int)(a).size()
#define mp make_pair
#define pb push_back
#define __(a) memset((a),0,sizeof(a))
#define _(a,b) memset((a),(b),sizeof(a))

const int MAXN = 2000005;
typedef long long lint;

int n, r, c;
int d[MAXN];
lint dd[MAXN];
int e[MAXN];
int g[MAXN];

int main( )
{
	int i, j, k;
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int tn, t;
	scanf( "%d", &tn );
	fr( t, tn )
	{
		scanf( "%d %d %d", &r, &c, &n );
		fi( n )
		{
			scanf( "%d", &g[i] );
		}
		_( d, -1 );
		dd[0] = 0;
		int cnt = 0;
		int cur_cap = 0;
		i = 0;
		int tcnt = 0;
		int st = 0;
		bool pruned =  false;
		lint ans = 0;
		while ( cnt < r )
		{
			if ( tcnt < n && cur_cap + g[i] <= c )
			{
				++ tcnt;
				cur_cap += g[i];
				++ i;
				if ( i == n )
					i = 0;
			}
			else
			{
				ans += cur_cap;
				d[st] = cnt;
				cur_cap = 0;
				tcnt = 0;
				++ cnt;
				if ( !pruned )
					dd[cnt] = ans;
				st = i;

				if ( d[i] >= 0 && !pruned )
				{
					int rs = cnt - d[i];
					lint diff = ans - dd[d[i]];
					int tt = ( r - cnt ) / rs;
					ans += (lint)( tt ) * diff;
					cnt += tt * rs;
					pruned = true;
				}
			}
		}
		printf( "Case #%d: ", t + 1 );
		cout << ans << endl;
	}
	return 0;
}