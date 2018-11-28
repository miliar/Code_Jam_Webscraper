#include <cstdio>
#include <algorithm>
using namespace std;

#define FOR(i,a,b)  for(int i=(a),_n=(b);i<=_n;i++)
#define FORD(i,a,b) for(int i=(a),_n=(b);i>=_n;i--)
#define REP(i,n) FOR(i,0,n-1)
typedef long long int64;
#define two(X) (1<<(X))
#define two64(X) (((int64)1)<<(X))
#define contain(S,x) (((S)&two(x))>0)

const int inf = 1000000000;

int dr[] = {-1,+0,+0,+1};
int dc[] = {+0,-1,+1,+0};

int H,W;
int map[105][105];
char nextl;
char label[105][105];

char dfs( int r, int c ) {
	int d = -1;
	int altnow = map[r][c], alt=inf;
	REP(i,4) {
		int rr=r+dr[i], cc=c+dc[i];
		
		if ( rr>=0 && rr<H && cc>=0 && cc<W ) {
			if ( altnow>map[rr][cc] && alt>map[rr][cc] ) {
				alt=map[rr][cc], d=i;
			}
		}
	}
	if ( d==-1 ) {
		if ( label[r][c] == '0' ){
			label[r][c] = nextl; nextl++;
			return label[r][c];
		}
		else return label[r][c];
	}
	else {
		char la = dfs( r+dr[d], c+dc[d] );
		label[r][c] = la;
		return la;
	}
}

int main() {
	int ntc;
	scanf( "%d",&ntc );
	REP(tc,ntc) {
		scanf( "%d%d",&H,&W );
		REP(i,H) REP(j,W) {
			label[i][j] = '0';
			scanf( "%d", &map[i][j] );
		}

		nextl = 'a';
		REP(i,H) REP(j,W) if ( label[i][j]=='0' )
			dfs( i,j );
		
		printf( "Case #%d:\n", tc+1 );
		REP(i,H) {
			REP(j,W) {
				if ( j!=0 ) printf( " " );
				printf( "%c", label[i][j] );
			}
			printf( "\n" );
		}
	}
	return 0;
}
