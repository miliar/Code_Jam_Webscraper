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

#ifdef OK_DEBUG
#define ASSERT(x)  {if(!(x)) __asm{ int 3};}
#define DPRINTF	printf
#else
#define ASSERT(x)
#define DPRINTF(...)
#endif

#define forn(a,b,c) for( a = ( b ); a < ( c ); ++ a )

#define reset(a,b) memset( a, b, sizeof( a ) )

template <class T> void out( T a, T b ) { bool first = true; for( T i = a; i != b; ++ i ) { if( !first ) printf( " " ); first = false; cout << * i; } printf( "\n" ); }
template <class T> void outl( T a, T b ) { for( T i = a; i != b; ++ i ) { cout << * i << "\n"; } }
typedef long long ll;

#define checkmax(x, v) {if(x < v) x = v;}
#define checkmin(x, v) {if(x > v) x = v;}

template <typename T>
T sum(T* start, T* end)
{
	T res = 0;
	T* i;
	forn(i, start, end)
		res +=  *i;
	return res;
}

template <typename T>
T max(T* start, T* end, T init_value)
{
	T res = init_value;
	T * i;
	forn(i, start, end)
	{
		checkmax(res, *i);
	}
	return res;
}

template <typename T>
T min(T* start, T* end, T init_value)
{
	T res = init_value;
	T * i;
	forn(i, start, end)
	{
		checkmin(res, *i);
	}
	return res;
}

ll gcd(ll x, ll y)
{
	if(x < y)
		swap(x, y);
	if(y == 0)
		return x;
	return gcd(x%y, y);
}
ll fs[10001];
#define INF ((ll)pow((double)10, (double)16))

ll lcm(ll x, ll y)
{
	ll r = x/gcd(x, y) * y;
	if(r < 0)
		r = INF;
	return r;
}

ll gcd_all(ll * start , ll * end)
{
	return 0;
}

ll lcm_all(ll * start, ll * end)
{
	ll g = gcd_all(start, end);
	ll res = *start/g;

	ll *i;
	forn(i, start+1, end)
	{
		res = res* (*i);
		if(res <= 0)
			return INF;
	}
	return res;
}

ll solve(int N, int L, int H)
{
	sort(fs, fs+N);
	

	ll gcd, lcm;
	ll left = L-1;
	ll right = H +1 ;
	ll mid;
	while(left <= right)
	{
		 mid = (left+right)/2;
		 ll* pos = lower_bound(fs, fs+N, mid);
		 ASSERT(pos >= fs && pos < fs+N);
		 lcm = lcm_all(fs, pos);
		 gcd = gcd_all(pos, fs+N);
		
		 
	}
}

int solve1(int N , int L, int H)
{
	int i,k;
	int poss = 0;
	forn(k, L, H+1)
	{
		int ok = 1;
		forn(i, 0, N)
		{
			if(k % fs[i] == 0 || fs[i] %k == 0)
			{
			}
			else 
			{
				ok = 0;
				break;
			}
		}
		if(ok)
		{
			poss = 1;
			break;
		}
	}
	if(poss)
		return k;
	else return -1;
}

int main()
{
	int T;
	int N, L, H;
	int caseIndex = 1;
	int res = 0;
	int i;
	ll n;
	cin >> T;
	ASSERT(INF > 0);
	while (T--)
	{
		printf("Case #%d: ", caseIndex++);
		cin >> N >> L >> H;
		forn(i, 0, N)
			cin >> fs[i];
		n = solve1(N, L, H);
		if(n >= 0)
			printf("%d\n", n);
		else printf("NO\n");
	}
	return 0;
}