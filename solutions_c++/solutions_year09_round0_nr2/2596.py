#include <iostream>
#include <vector>
using namespace std;

int H, W;
int map[100][100];
bool visited[100][100];
char ansmap[100][100];
char anscode;

int di[4][2] = { {-1,0}, {0,-1}, {0,1}, {1,0} };

struct point {
	int y,x;
};

vector<point> path;

void recur(int y, int x)
{



	
}

void process()
{
	for( int i=0; i<H; i++ ) {
		for( int j=0; j<W; j++ ) {
			visited[i][j]=false;
			ansmap[i][j]=' ';
		}
	}
	
	anscode='a';
	int y,x;

	for(int i=0; i<H; i++ ) {
		for( int j=0; j<W; j++ ) {
			path.clear();
			if(ansmap[i][j] == ' ') {
				y = i; x= j;
				while(true) {
					point p; p.y = y; p.x = x;
					path.push_back( p );
					
					int minalt = 100000;
					int nexty, nextx;
					for( int i=0; i<4; i++ ) {
						int ny = y+di[i][0];
						int nx = x+di[i][1];
						if( nx>=0 && nx <W && ny>=0 && ny < H ) {
							if( minalt > map[ny][nx] && map[y][x] > map[ny][nx]) {
								minalt = map[ny][nx];
								nexty = ny;
								nextx = nx;
							}
						}
					}

					if( minalt == 100000 ) {
						for(int i=0; i<path.size(); i++) {
							ansmap[path[i].y][path[i].x] = anscode;
						}
						anscode++;
						break;
					}
					else if (ansmap[nexty][nextx] != ' ') {
						point p;
						p.y = nexty; p.x = nextx;
						path.push_back( p );
						for(int i=0; i<path.size(); i++) {
							ansmap[path[i].y][path[i].x] = ansmap[nexty][nextx];
						}
						break;
					}
					else {
						y = nexty;
						x = nextx;
					}
				}
			}
		}
	}



	for( int i=0; i<H; i++ ) {
		for( int j=0; j<W; j++ ) {
			cout<<ansmap[i][j];
			if( j!=W-1 ) {
				cout<<" ";
			}
		}
		cout<<endl;
	}

}


int main()
{
	freopen("B-large.in","rt", stdin);
	freopen("B.out", "wt", stdout);
	int T;

	cin>>T;
	for( int i=0; i<T; i++ ) {
		cin>>H>>W;
		for( int j=0; j<H; j++ ) {
			for( int k=0; k<W; k++ ) {
				cin>>map[j][k];
			}
		}
		cout<<"Case #"<<i+1<<":"<<endl;
		process();
	}
	

}