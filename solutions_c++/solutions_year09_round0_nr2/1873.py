#include <iostream>
#include <cassert>
using namespace std;

int H, W;
int att[100][100];
bool issink[100][100];
bool canflow[100][100][4];
int group[100][100];

const int dr[] = {-1,0,0,1};
const int dc[] = {0,-1,1,0};

const string dir[] = { "NORTH", "WEST", "EAST", "SOUTH" };

inline bool inrange( int x, int bound ) {
	return 0 <= x && x < bound;
}
void construct() {
	memset(canflow, 0, sizeof canflow);
	memset(issink, 0, sizeof issink );
	for(int i=0;i<H;++i) for(int j=0;j<W;++j) {
		int si = -1, sj = -1, idx = -1;
		for(int k=0;k<4;++k) {
			int ni = dr[k] + i;
			int nj = dc[k] + j;
			if( ! inrange( ni, H ) ) continue;
			if( ! inrange( nj, W ) ) continue;
			if( att[i][j] <= att[ni][nj] ) continue;
			if( ( si==-1&&sj==-1 ) || att[si][sj] > att[ni][nj] ) {
				idx = k;
				si = ni;
				sj = nj;
			}
		}
		if( si == -1 && sj == -1 ) {
			issink[i][j] = true;
		}
		else {
			// cerr << "debug : " << "at " << i << "," << j << ", " << si << "," << sj << "=>" << dir[(idx+2)%4] << endl;
			canflow[si][sj][3-idx] = true;
		}
	}
}

void join(int i, int j, int label) {
	if( !inrange( i, H ) ) return;
	if( !inrange( j, W ) ) return;
	if( group[i][j] != -1 ) return;
	group[i][j] = label;
	for(int k=0;k<4;++k) if( canflow[i][j][k] ) join( i+dr[k], j+dc[k], label );
}

char symbol[100][100];
void doit() {
	memset(symbol, 0, sizeof symbol);
	int label = 0;
	memset( group, -1, sizeof group );
	for(int i=0;i<H;++i) for(int j=0;j<W;++j) if( issink[i][j] && group[i][j] == -1 ) {
		join( i, j, label++ );
	}
	char ch = 'a';
	while(1) {
		int target = -1;
		for(int i=0;i<H;++i) for(int j=0;j<W;++j) if( symbol[i][j] == 0 ) {
			target = group[i][j];
			goto maki;
		}
maki:;
		if( target == -1 ) break;
		for(int i=0;i<H;++i) for(int j=0;j<W;++j) if( group[i][j] == target ) symbol[i][j] = ch;
		++ch;
	}
}
int main() {
	int tn;
	cin >> tn;
	for(int cc=1;cc<=tn;++cc) {
		cin >> H >> W;
		for(int i=0;i<H;++i) for(int j=0;j<W;++j) {
			cin >> att[i][j];
		}
		construct();
		doit();
		cout << "Case #" << cc << ":" << endl;
		for(int i=0;i<H;++i) for(int j=0;j<W;++j) assert( islower( symbol[i][j] ) );
		for(int i=0;i<H;++i) { for(int j=0;j<W;++j) cout << symbol[i][j] << " "; cout << endl; }
		
	}
}
