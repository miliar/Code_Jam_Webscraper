#include<iostream>
#include<string>
#include<vector>
#include<cstdio>
#include<map>
#include<set>
#include<queue>
#include<algorithm>
using namespace std;

vector<string> M;

int SN[16][16][4];

char visited[16][16][512][512];


class E{
public:
	E( int x_, int y_, int G1_, int G2_, int dist_ ) : x(x_), y(y_), G1(G1_), G2(G2_), dist(dist_) {}
	bool operator<(const E &e2) const { return dist > e2.dist; }
	int x, y, G1, G2;
	int dist;
};

int dx[] = {1,0,-1,0};
int dy[] = {0,1,0,-1};

int GX[10000];
int GY[10000];
int GD[10000];

int main( void )
{
	int N;
	cin >> N;
	for( int CC = 0; CC < N; CC ++ ){
		int X, Y;
		cin >> Y >> X;
		M.clear();
		int Xs, Ys;
		int Xg, Yg;
		for( int i = 0; i < Y; i ++ ){
			string s;
			cin >> s;
			for( int j = 0; j < X; j ++ ){
				if( s[j] == 'O' ){ Xs = j, Ys = i; }
				if( s[j] == 'X' ){ Xg = j, Yg = i; }
			}
			M.push_back( s );
		}

		GX[0] = -100;
		GY[0] = -100;
		GD[0] = -100;

		int ng = 1;
		map< pair< pair<int,int>, int>, int > ww;
		for( int y = 0; y < Y; y ++ ){
			for( int x = 0; x < X; x ++ ){
				if( M[y][x] == '#' ) continue;
				for( int d = 0; d < 4; d ++ ){
					int xx = x, yy = y;
					for( ; 0 <= xx && xx < X && 0 <= yy && yy < Y && M[yy][xx] != '#'; xx += dx[d], yy += dy[d] );
					xx -= dx[d], yy -= dy[d];
					pair< pair<int,int>, int> aa( pair<int,int>(xx,yy), d );
					if( ww[aa] == 0 ){ GX[ng] = xx, GY[ng] = yy, GD[ng] = d; ww[aa] = ng ++; }
					SN[x][y][d] = ww[aa];
				}
			}
		}
		cerr << ng << endl;

		memset( visited, 0x00, sizeof(visited) );

		priority_queue<E> wl;
		wl.push( E(Xs, Ys, 0, 0, 0) );

		int ans = -1;
		while( !wl.empty() ){
			E e = wl.top();
			wl.pop();
			int x = e.x, y = e.y;
			if( x == Xg && y == Yg ){ ans = e.dist; break; }

			if( visited[x][y][e.G1][e.G2] ) continue;

			visited[x][y][e.G1][e.G2] = 1;

			for( int d = 0; d < 4; d ++ ){
				int gg = SN[x][y][d];
				if( gg != e.G1 )
					wl.push( E( x, y, min(e.G1,gg), max(e.G1,gg), e.dist ) );
				if( gg != e.G2 )
					wl.push( E( x, y, min(e.G2,gg), max(e.G2,gg), e.dist ) );

				int xx = x + dx[d];
				int yy = y + dy[d];
				if( x == GX[e.G1] && y == GY[e.G1] && d == GD[e.G1] )
					xx = GX[e.G2], yy = GY[e.G2];
				if( x == GX[e.G2] && y == GY[e.G2] && d == GD[e.G2] )
					xx = GX[e.G1], yy = GY[e.G1];
				if( 0 <= xx && xx < X && 0 <= yy && yy < Y && M[yy][xx] != '#' )
					wl.push( E( xx, yy, e.G1, e.G2, e.dist + 1 ) );
			}
		}

		if( ans < 0 )
			printf( "Case #%d: THE CAKE IS A LIE\n", CC + 1 );
		else
			printf( "Case #%d: %d\n", CC + 1, ans );
	}
	return 0;
}
