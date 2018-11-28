#include<iostream>
#include<queue>
using namespace std;

struct Point{
    int x;
    int y;
    int high;
    bool operator < ( Point p ) const{
        if( p.high != high ) return p.high > high;
		if( p.x != x ) return p.x < x;
		return p.y < y;
    }
};

int h, w;
int board[105][105];
int ans[105][105];
int dir[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};
priority_queue< Point > r;
queue< Point > r1;
queue< Point > r2;
int ind;

void bfs( int x, int y ){
    int i, mi, u, o = -1, pro;
	bool f[105][105];
	Point p, q;
    p.x = x;
    p.y = y;
    r1.push( p );
	memset( f, false, sizeof ( f ) );
	f[p.x][p.y] = true;
    while( !r1.empty( ) ){
        p = r1.front( );r1.pop( );
        r2.push( p );
        mi = 1000000;
        for( i = 0; i < 4; i++ ){
            q.x = p.x + dir[i][0];
            q.y = p.y + dir[i][1];
            if( q.x < 0 || q.x >= h || q.y < 0 || q.y >= w || f[q.x][q.y] || board[p.x][p.y] <= board[q.x][q.y]  ) continue;
            if( board[q.x][q.y] < mi ){
                mi = board[q.x][q.y];
                u = i;
				if( ans[q.x][q.y] != 0 )
					o = ans[q.x][q.y];
				else o = -1;
            }
        }
        if( mi == 1000000 ) continue;
        q.x = p.x + dir[u][0];
        q.y = p.y + dir[u][1];
		f[q.x][q.y] = true;
        r1.push( q );
    }
    if( o != -1 )
        pro = o;
    else pro = ++ind;
    while( !r2.empty( ) ){
        p = r2.front( );r2.pop( );
        ans[p.x][p.y] = pro;
    }
}

int main( ){
    int i, j, t, cas;
    Point p;
//	freopen( "B-large.in", "r", stdin );
//	freopen( "B-large.out", "w", stdout );
    scanf( "%d", &t );
    for( cas = 1; cas <= t; cas++ ){
        scanf( "%d %d", &h, &w );
        for( i = 0; i < h; i++ ){
            for( j = 0; j < w; j++ )
                scanf( "%d", &board[i][j] );
        }
        ind = 0;
        memset( ans, 0, sizeof( ans ) );
		for( i = 0; i < h; i++ )
			for( j = 0; j < w; j++ ){
				if( ans[i][j] ) continue;
				bfs( i, j );
			}
		printf( "Case #%d:\n", cas );
        for( i = 0; i < h; i++ ){
            printf( "%c", ans[i][0] - 1 + 'a' );
            for( j = 1; j < w; j++ )
                printf( " %c", ans[i][j] - 1 + 'a' );
            printf( "\n" );
        }
        while( !r.empty( ) ) r.pop( );
        while( !r1.empty( ) ) r1.pop( );
        while( !r2.empty( ) ) r2.pop( );
    }
    return 0;
}
