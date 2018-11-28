#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <cmath>
#include <cassert>
#include <sstream>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace std;

#define fo(a,b,c) for( (a) = (b); (a) < (c); ++ (a) )
#define fr(a,b) fo( (a), 0, (b) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define all(v) (v).begin( ), (v).end( )
#define pb push_back
#define mp make_pair

int n, m;

struct mat_t
{
	long long a[2][2];
};

mat_t mul( const mat_t & a, const mat_t & b )
{
	mat_t ret;
	memset( ret.a, 0, sizeof( ret.a ) );

	int i, j, k;

	fi( 2 ) fj( 2 ) fk( 2 ) ( ret.a[i][j] += a.a[i][k] * b.a[k][j] ) %= 1000000000LL;

	return ret;
}

mat_t pow( const mat_t & a, long long pw )
{
	mat_t ret;
	memset( ret.a, 0, sizeof( ret.a ) );
	ret.a[0][0] = ret.a[1][1] = 1;

	mat_t x = a;

	for( long long i = 1; i <= pw; i <<= 1 )
	{
		if( pw & i ) ret = mul( ret, x );
		x = mul( x, x );
	}

	return ret;
}

// using windows calculator )
long long zu[] = 
{
	1,
	5,
	27,
	143,
	751,
	935,
	607,
	903,
	991,
	335,
	47,
	943,
	471,
	55,
	447,
	463,
	991,
	95,
	607,
	263,
	151,
	855,
	527,
	743,
	351,
	135,
	407,
	903,
	791,
	135,
	647,
	343,
	471
};

int main( )
{
	int i, j, k, t, tt;

	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );

	scanf( "%d", &t );
	for( tt = 1; tt <= t; ++ tt )
	{
		mat_t moo;

		moo.a[0][0] = 3;
		moo.a[0][1] = 1;
		moo.a[1][0] = 5;
		moo.a[1][1] = 3;

		long long pw;
		scanf( "%lld", &pw );
		moo = pow( moo, pw );

		long long a = moo.a[0][0];
		long long b = moo.a[0][1];

		a = 1;
		b = 0;
		fi( pw )
		{
			long long na = 3 * a + 5 * b;
			long long nb = a + 3 * b;

			na %= 1000000000000000000LL;
			nb %= 1000000000000000000LL;

			a = na;
			b = nb;
		}

		long long ans = zu[pw];

		printf( "Case #%d: %lld%lld%lld\n", tt, ans / 100 % 10, ans / 10 % 10, ans % 10 );
	}

	return 0;
}
