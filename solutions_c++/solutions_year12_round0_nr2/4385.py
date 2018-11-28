#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define _(a,b) memset( a, b, sizeof( a ) )
using namespace std;

int ri() { int a; scanf( "%d", &a ); return a; }
double rf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100000]; string rs() { scanf( "%s", sbuf ); return sbuf; }
long long rll() { long long a; scanf( "%lld", &a ); return a; }
int gg, mt, Mt, Y, maybe;
int main(void)
{
	int i, j, k, t, tt;
	freopen( "b-large.in", "r", stdin );
	freopen( "b-large.out", "w", stdout );
	scanf( "%d\n", &tt );
	for( t = 1; t <= tt; ++ t )
 	{
		Y = 0;
		maybe = 0;
		int N = ri();
		int S = ri();
		int P = ri();
		mt = 3*P-4;
		Mt = 3*P-2;
		mt = (mt > 0 ? mt : 0);
		Mt = (Mt > 0 ? Mt : 0);
		fi(N)
		{
			gg = ri();
			if (gg >= Mt)
			{
				Y++;
			}
			else
			{
				if (gg>=mt && P!=1)
				{
					maybe++;
				}

			}
		}
		printf ("Case #%d: %d\n", t, Y+min(maybe, S));
	}
	return (0);
}

