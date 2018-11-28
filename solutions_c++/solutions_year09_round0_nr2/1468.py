#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;

const int dx[]={-1,0,0,+1};
const int dy[]={0,-1,+1,0};

struct point {
	int x, y, z;
	point(){}
	point(int _x, int _y, int _z) : x(_x), y(_y), z(_z) {}
	};

int T, H, W, br;
int a[128][128];
point b[128*128];
int c[128][128];

bool operator<(const point& p1, const point& p2){
	return p1.z < p2.z;
	}

inline bool can(const int& x, const int& y){
	if( x<0 || y<0 || x>=H || y>=W ) return false;
	return true;
	}

void solve () {
	sort ( b, b+br );
	memset (c,-1,sizeof(c));
	int cnt = 1;
	for(int i=br-1; i>=0; --i){
		if( c[b[i].x][b[i].y] < 0 ){
			vector< point > v;
			v.push_back( point(b[i]) );
			while( 1 ){
				point mini = point(-1,-1,1<<30);
				if( v.back().x<0 || c[ v.back().x ][ v.back().y ] > 0 ) break;
				for(int k=0; k<4; ++k){
					int nx, ny;
					nx = v.back().x + dx[k];
					ny = v.back().y + dy[k];
					if( can(nx,ny) && mini.z>a[nx][ny] && a[nx][ny]<a[nx-dx[k]][ny-dy[k]] ) mini = point (nx,ny,a[nx][ny]);
					}
				v.push_back( mini );
				}
			if( v.back().z == 1<<30 ){
				for(int k=0; k<v.size()-1; ++k) c[v[k].x][v[k].y] = cnt;
				++cnt;
				}
			else{
				for(int k=0; k<v.size()-1; ++k) c[v[k].x][v[k].y] = c[v.back().x][v.back().y];
				}
			}
		}
	char cc = 'a';
	char ccc[32];
	memset (ccc,'.',sizeof(ccc));
	for(int i=0; i<H; ++i) for(int j=0; j<W; ++j) if( ccc[c[i][j]]=='.' ) ccc[c[i][j]] = cc++;
	for(int i=0; i<H; ++i){
		printf ("%c",ccc[c[i][0]]);
		for(int j=1; j<W; ++j) printf (" %c",ccc[c[i][j]]);
		printf ("\n");
		}
}

void input () {
	scanf ("%d",&T);
	for(int t=0; t<T; ++t){
		br = 0;
		scanf ("%d%d",&H,&W);
		for(int i=0; i<H; ++i) for(int j=0; j<W; ++j) {
			scanf ("%d",&a[i][j]);
			b[ br++ ] = point ( i, j, a[i][j] );
			}
		printf ("Case #%d:\n",t+1);
		solve ();
		}
}

int main (void) {
	input ();
}


