#pragma comment( linker, "/stack:128000000" )
#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>

void prepare( )
{
	freopen( "input.txt", "r", stdin );
#ifndef _DEBUG
	freopen( "output.txt", "w", stdout );
#endif
}

#include <cmath>
#include <cassert>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <sstream>
#include <iostream>
#include <deque>

using namespace std;

#define fo(a,b,c) for(a =(b);a<(c);++a)
#define fr(a,b) fo(a,0,(b))
#define fi(a) fr(i,(a))
#define fj(a) fr(j,(a))
#define fk(a) fr(k,(a))
#define all(a) (a).begin(),(a).end()
#define mp make_pair
#define pb push_back
#define sz(a) (int)(a).size()
#define _(a,b) memset((a),(b),sizeof(a))
#define __(a) _((a),0)

typedef long long lint;

const int MAXN = 75;
const int MOD = 1000000007;

int n, m;
int b;
lint d;
int dig[MAXN];
int c[MAXN][MAXN];
int fac[MAXN];
int dp[MAXN][MAXN][MAXN];
int v[MAXN][MAXN][MAXN];
int tp[MAXN][MAXN][MAXN][MAXN];
int maxper;

void precalc( )
{
	__( dp );
	__( tp );
	int i, j, k, l;
	tp[0][0][0][0] = 1;
	maxper = 0;
	fi( b )
		maxper += i;
	maxper /= b;
	++ maxper;
	fi( b - 1 ) //last
	{
		fj( b )	 // cur
		{
			fk( maxper ) // per
			{
				fr( l, b ) // tot
				{
					if ( tp[i][j][k][l] >= 0 )
					{
						( tp[i + 1][j][k][l] += tp[i][j][k][l] ) %= MOD;
						int nj = j + ( i + 1 );
						int nk = k;
						if ( nj >= b )
						{
							nj -= b;
							++ nk;
						}
						( tp[i + 1][nj][nk][l + 1] += tp[i][j][k][l] ) %= MOD;
					}
				}
			}
		}
	}
	fj( b )	 // cur
	{
		fk( maxper ) // per
		{
			fr( l, b + 1 ) // tot
			{
				if ( tp[b - 1][j][k][l] >= 0 )
				{
					dp[j][k][l] = tp[b - 1][j][k][l];
				}
			}
		}
	}
}

void preprecalc( )
{
	int i, j;
	c[0][0] = 1;
	fi( MAXN - 1 ) fj( MAXN - 1 )
	{
		( c[i + 1][j] += c[i][j] ) %= MOD; 				
		( c[i + 1][j + 1] += c[i][j] ) %= MOD; 				
	}
	fac[0] = 1;
	fi( MAXN ) if ( i )
	{
		fac[i] = (int)( ( (lint)fac[i - 1] * (lint)i ) % (lint)MOD );
	}
}

int solve( )
{
	int i, j, k, per, cifr;
	__( v );
	fi( b + 1 )
		v[0][i][0] = 1;
	fi( n )
	{
		fj( b + 1 ) if( j )
		{
			fk( maxper )
			{
				if ( v[i][j][k] == 0 )
					continue;
				// j - cifr
				// k - per
				int nv = dig[i] - k;
				int addper = 0;
				if ( nv < 0 )
				{
					nv += b;
					addper = 1;
				}
				//without zero
				fr( per, maxper )
				{
					lint dd = ( (lint)v[i][j][k] * (lint)dp[nv][per][j] ) % (lint)MOD;
					if ( dd == 0 )
						continue;
					fr( cifr, j + 1 )
					{
						lint cc;
						if ( cifr == 0 )
							cc = 1;
						else
							cc = (lint)c[j][cifr] * (lint)fac[cifr] % (lint)MOD;
						( v[i + 1][cifr][per + addper] += (int)( ( dd * cc ) % (lint)MOD ) ) %= MOD; 
					}
				}
				fr( per, maxper )
				{
					lint dd = ( (lint)v[i][j][k] * (lint)dp[nv][per][j - 1] ) % (lint)MOD;
					if ( dd == 0 )
						continue;
					//with zero
					fr( cifr, j + 1 ) if ( cifr )// cifr - with zero
					{
						lint cc;
						if ( cifr == 0 )
							cc = 1;
						else
							cc = (lint)c[j - 1][cifr - 1] * (lint)fac[cifr] % (lint)MOD;
						( v[i + 1][cifr][per + addper] += (int)( ( dd * cc ) % (lint)MOD ) ) %= MOD; 
					}
				}
			}
		}
	}
	return ( v[n][0][0] + v[n - 1][0][dig[n - 1]] ) % MOD;
}

int main( )
{
	prepare( );
	int i, j, k;
	int t, tn;
	preprecalc( );
	cin >> tn;
	fr( t, tn )
	{
		printf( "Case #%d: ", t + 1 );
		cin >> d >> b;
		__( dig );
		n = 0;
		while ( d )
		{
			dig[n ++] = (int)( d % b );
			d /= b;
		}
		precalc( );
		cout << solve( ) << endl;
	}
	return 0;
}