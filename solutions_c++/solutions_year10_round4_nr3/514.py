#include <vector>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <ctime>

using namespace std;

const __int64 M=10000000;

const int dx[6] = {-1,0,0,1,-1,1};
const int dy[6] = {0,-1,1,0,1,-1};

set<__int64> dat;
vector<__int64> v_p;
int t;


void read_it()
{
	dat.clear();
	int n;
	scanf( "%d", &n );
	for( int i = 0; i < n; ++i )
	{
		int x1, y1, x2, y2;
		scanf( "%d %d %d %d", &x1, &y1, &x2, &y2 );
		for( int x = x1; x <= x2; ++x )
			for( int y = y1; y <= y2; ++y )
			{
				__int64 s = x;
				s = s * M + y;
				v_p.push_back( s );
				dat.insert( s );
			}
	}
	t = 0;
}

int try_it( __int64 p )
{
	dat.erase( p );
	vector<__int64> v_now;
	v_now.push_back( p );
	__int64 maxx = p/M;
	__int64 maxy = p%M;
	__int64 minx = p/M;
	__int64 miny = p%M;

	int top = 0, tail = 0;
	while( top <= tail )
	{
		__int64 now = v_now[top];
		__int64 nowx = now/M;
		__int64 nowy = now%M;
		if( nowx > maxx )
			maxx = nowx;
		if( nowx < minx )
			minx = nowx;
		if( nowy > maxy )
			maxy = nowy;
		if( nowy < miny )
			miny = nowy;

		for( int i = 0; i < 6; ++i )
		{
			__int64 nxtx = nowx + dx[i];
			__int64 nxty = nowy + dy[i];
			__int64 nxt = nxtx * M + nxty;
			if( dat.find( nxt ) == dat.end() )
				continue;
			dat.erase( nxt );
			v_now.push_back( nxt );
			++tail;
		}
		++top;
	}

	int rst = 0;
	for( int i = 0; i < (int) v_now.size(); ++i )
	{
		__int64 now = v_now[i];
		int nowx = (int) now / M;
		int nowy = (int) now % M;
		int nowcnt = maxx-nowx + maxy-nowy + 1;
		if( nowcnt > rst )
			rst = nowcnt;
	}

	return rst;
}

int make_it()
{
	t = 0;
	for( int i = 0; i < (int) v_p.size(); ++i )
		if( dat.find( v_p[i] ) != dat.end() )
		{
			int now = try_it( v_p[i] );
			if( now > t )
				t = now;
		}
	return t;
}

int main()
{
	freopen( "out.txt", "w", stdout );
	freopen( "C-small-attempt2.in", "r", stdin );
	int t;
	scanf( "%d", &t );
	for( int i = 0; i < t; ++i )
	{
		read_it();
		printf( "Case #%d: %d\n", i+1, make_it() );
	}
	return 0;
}