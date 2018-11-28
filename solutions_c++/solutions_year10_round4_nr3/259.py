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

int n, m;

struct Rect
{
	int x1, y1, x2, y2;
};

vector<Rect> r;
vector<int> w;
int minxy, maxx, maxy;

bool inter( int a, int b )
{
	int dx = min( r[a].x2 + 1, r[b].x2 + 1 ) - max( r[a].x1, r[b].x1 );
	int dy = min( r[a].y2 + 1, r[b].y2 + 1 ) - max( r[a].y1, r[b].y1 );
	return dx >= 0 && dy >= 0;
}

void go( int id )
{
	if ( w[id] )
		return;
	w[id] = 1;
	int i;
	minxy = min( minxy, r[id].x1 + r[id].y1 );
	maxx = max( maxx, r[id].x2 );
	maxy = max( maxy, r[id].y2 );
	fi( n )
	{
		if ( inter( id, i ) )
			go( i );
	}
}

int main( )
{
	prepare( );
	int i, j, k;
	int t, tn;
	cin >> tn;
	fr( t, tn )
	{
		printf( "Case #%d: ", t + 1 );
		int ans = 0;
		scanf( "%d", &n );
		r.resize( n );
		fi( n )
		{
			scanf( "%d %d %d %d", &r[i].x1, &r[i].y1, &r[i].x2, &r[i].y2 );
		}
		w = vector<int> ( n, 0 );
		m = 0;
		ans = 0;
		fi( n )
		{
			if ( !w[i] )
			{
				minxy = 1000000000;
				maxx = -1;
				maxy = -1;
				go( i );
				ans = max( ans, maxx + maxy - minxy + 1 );
			}
		}
		printf( "%d\n", ans );
	}
	return 0;
}