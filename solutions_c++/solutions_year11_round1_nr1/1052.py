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
using namespace std;

#ifdef _DEBUG
#define ASSERT(x)  {if(!(x)) __asm{ int 3};}
#else
#define ASSERT(x)
#endif

#define forn(a,b,c) for( a = ( b ); a < ( c ); ++ a )

#define reset(a,b) memset( a, b, sizeof( a ) )

template <class T> void out( T a, T b ) { bool first = true; for( T i = a; i != b; ++ i ) { if( !first ) printf( " " ); first = false; cout << * i; } printf( "\n" ); }
template <class T> void outl( T a, T b ) { for( T i = a; i != b; ++ i ) { cout << * i << "\n"; } }
typedef long long ll;

ll gcd(ll x, ll y)
{
	if(x < y)
		swap(x, y);
	if(y == 0)
		return x;
	return gcd(x%y, y);
}
int main()
{
	int T;
	int caseIndex = 1;
	int res = 0;
	ll N, pd, pg;
	ll x;
	cin >> T;
	ASSERT( pow((double)10, (double)15) <  pow((double)2, (double)62));
	while (T--)
	{
		cin >> N >> pd >> pg;
		x = gcd(100, pd);
		ASSERT(N >0 && x >0);
		int poss = 1;
		if(pd > 0 && pg == 0)
			poss = 0;
		if(pd < 100 && pg == 100)
			poss = 0;
		ASSERT(100 % x == 0 && pd % x == 0)
		printf("Case #%d: %s\n", caseIndex++, (N >= (100 / x)  && poss) ? "Possible" : "Broken");
	}
	return 0;
}