#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
//#include <vector>
//#include <string>
//#include <map>
//#include <set>
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

#define MAXN 60
char ts[MAXN][MAXN+1];

int check(int i, int j)
{
	return ts[i][j] == '#' && ts[i][j+1] == '#'
		 && ts[i+1][j] == '#' && ts[i+1][j+1] == '#';
}

void put(int i, int j)
{
	ts[i][j] = '/';
	ts[i][j+1] = '\\';
	ts[i+1][j] = '\\';
	ts[i+1][j+1] = '/';
}


int solve(int R, int C)
{
	int i,j;
	int poss = 1;
	forn(i, 0, R-1)
		forn(j, 0, C-1)
	{
		if(ts[i][j] == '#')
		{
			if(check(i, j))
			{
				put(i, j);
			}
			else return 0;
		}
	}

	forn(i, 0, R)
		forn(j, 0, C)
	{
		if(ts[i][j] == '#')
			return 0;
	}
	return poss;
}

int main()
{
	int T;
	int i, poss;
	char more[10];
	int caseIndex = 1;
	int res = 0;
	cin >> T;
	int R, C;
	while (T--)
	{
		printf("Case #%d: ", caseIndex++);
		cin >> R >> C;
		gets(more);
		forn(i, 0, R)
			gets(ts[i]);
		poss = solve(R, C);
		
		cout << "\n";
		if(!poss)
			printf("Impossible\n");
		else
		{
			forn(i, 0, R)
				puts(ts[i]);
		}
	}
	return 0;
}