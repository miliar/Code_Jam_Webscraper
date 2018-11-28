#include<iostream>
#include<queue>
using namespace std;

#define maxn 110

int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};


int is[maxn][maxn];
int val[maxn][maxn];
int ans[maxn][maxn];
int n, m, num;

inline bool ch( int x, int y ) {
	return x >= 0 && x < n && y >= 0 && y < m;
}

struct node {
	int x, y;
};
int BFS( int sx, int sy ) {
	queue< node > hd;
	node now, next;
	now.x = sx, now.y = sy;
	hd.push( now );
	while( !hd.empty() ) {
		now = hd.front();
		if( is[ now.x ][ now.y ] != -1 ) 
			return is[ now.x ][ now.y ];
		int minh = val[now.x][now.y];
		int key = -1;
		for( int i = 0; i < 4; i ++ ) {
			int x = now.x + dx[i];
			int y = now.y + dy[i];
			if( ch(x,y) && val[x][y] < minh ) {
				minh = val[x][y];
				key = i;
			}
		}
		next.x = now.x + dx[ key ];
		next.y = now.y + dy[ key ];
		hd.push( next );
		hd.pop();
	}
	while(1);
	return -1;
}

void FloodFill( int sx, int sy ) {
	queue< node > hd;
	node now, next;
	now.x = sx, now.y = sy;
	hd.push( now );
	while( !hd.empty() ) {
		now = hd.front();
		for( int i = 0; i < 4; i ++ ) {
			int x = now.x + dx[i];
			int y = now.y + dy[i];
			if( ch(x, y) && is[x][y] == is[sx][sy] && ans[x][y] == -1 ) {
				ans[x][y] = ans[sx][sy];
				next.x = x, next.y = y;
				hd.push( next );
			}
		}
		hd.pop();
	}
}

int main() {
	freopen("D:\\in.in", "r", stdin );
	freopen("D:\\laout.out","w", stdout);
	int T;
	while( scanf("%d", &T) != EOF ) {
		for( int ca = 1; ca <= T; ca ++ ) {
			scanf("%d %d",&n, &m);
			for( int i = 0; i < n; i ++ ) for( int j = 0; j < m; j ++ )
				scanf("%d", &val[i][j]);
			memset( is, -1, sizeof(is));
			num = 0;
			for( int i = 0; i < n; i ++ ) for( int j = 0; j < m; j ++) {
				bool flag = 1;
				for( int k = 0; k < 4; k ++ ) {
					int x = i + dx[k];
					int y = j + dy[k];
					if( ch(x, y) && val[x][y] < val[i][j] ) 
						flag = 0;
				}
				if( flag ) is[i][j] = num ++;
			}

			for( int i = 0; i < n; i ++ ) for( int j = 0; j < m; j ++ ) 
				is[i][j] = BFS(i, j);
			memset( ans, -1, sizeof(ans) );
			int Time = 0;
			for( int i = 0; i < n; i ++ ) for( int j = 0; j < m; j ++ ) {
				if( ans[i][j] == -1 ) {
					ans[i][j] = Time;
					FloodFill( i, j );
					Time ++;
				}
			}
			printf("Case #%d:\n", ca );
			for( int i = 0; i < n; i ++ ) {
				for( int j = 0; j < m; j ++ ) {
					if( j ) printf(" ");
					printf("%c", ans[i][j] + 'a');
				}
				printf("\n");
			}
		}
	}
	return 0;
}