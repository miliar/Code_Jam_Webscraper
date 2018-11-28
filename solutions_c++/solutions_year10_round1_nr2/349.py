// AlexFetisov
// Accepted

#define _CRT_SECURE_NO_DEPRECATE
#pragma comment (linker, "/STACK:32000000")

#include <iostream>
#include <stdio.h>
#include <cstring>

void initf() 
{ 
	freopen( "in.txt", "r", stdin); 
	freopen( "out.txt", "w", stdout); 
}

#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <queue>

using namespace std;

#define fr(i,a,b) for ( int i = ( a ); i <= ( b ); ++i )
#define fi( a ) for ( int i = 0; i < ( a ); ++i )
#define fj( a ) for ( int j = 0; j < ( a ); ++j )
#define fk( a ) for ( int k = 0; k < ( a ); ++k )
#define CLR( a, b ) memset( ( a ), ( b ), sizeof ( a ) )
#define clr( a ) CLR( ( a ), 0 )
#define pb push_back
#define mp make_pair
#define all( v ) ( v ).begin(), ( v ).end()

typedef unsigned int uint;
typedef unsigned long long ull;
typedef long long ll;
typedef vector < int > vi;
typedef pair < int, int > pii;

const int inf = ( 1 << 30 );

map < int, int > al;
int D, I, M, n;
int a[101];
int dp[101][505];

int mabs( int x )
{
	if ( x < 0 ) return ( -x );
	return ( x );
}

int tmp[505];

void upd( int k )
{
	if ( M == 0 ) return;
	fi( 256 )
		tmp[i] = dp[k][i]; 	
	fi( 256 )
	{
		fj( 256 )
		{
			int delta = mabs( i - j );
			int z = delta / M;
			if ( delta % M > 0 )
				++z;
			tmp[i] = min( tmp[i], dp[k][j] + z * I );
		}	
	}
	fi( 256 )
		dp[k][i] = tmp[i];
}

void solve()
{
	scanf("%d%d%d%d", &D, &I, &M, &n );
	fi( n )
		scanf("%d", a + i );
	int ret = D * n;
	fj( n )
	{
		fi( 256 )		
		{
			dp[j][i] = D * j + mabs( i - a[0] );
		}
	}
	upd( 0 );
	fk( n ) if ( k )
	{
		fj( k )
		{
			int delta = k - j - 1;
			int del = delta * D;
			int cur = 0;
			al.clear();
			int lef = -M;
			int rig = M;
			for ( int i = lef; i <= rig; ++i )
			{
				if ( i < 0 || i > 255 ) continue;
				al[ dp[j][i] ]++;
			}
			fi( 256 )
			{
				pii p = *al.begin();
				int val = p.first;
				dp[k][i] = min( dp[k][i], val + del + mabs( i - a[k] ) );
				if ( lef >= 0 )
				{
					al[dp[j][lef]]--;
					if ( al[ dp[j][lef] ] == 0 )
						al.erase( dp[j][lef] );
				}
				++lef;
				++rig;
				if ( rig <= 255 )
					al[dp[j][rig]]++;														
			}
		}
		upd( k );
	}
	fi( n )
	{
		int ost = n - i - 1;
		fj( 256 )
			ret = min( ret, dp[i][j] + D * ost );
	}
	printf("%d\n", ret );
}

int main()
{
	initf();
	int t;
	scanf("%d", &t );
	fi( t )
	{
	    printf("Case #%d: ", i + 1 );
		solve();
	}
	return ( 0 );
}
