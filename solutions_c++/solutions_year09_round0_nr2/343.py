/*
TASK: 
LANG: C++
USER: smilitude1
*/


#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<algorithm>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<iterator>
using namespace std;

#define FORIT(i, m) for (__typeof((m).begin()) i=(m).begin(); i!=(m).end(); ++i)
#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(__typeof(b) i=(a); i<=(b); i++)

#define sz size()
#define pb push_back
#define ALL(x) x.begin(), x.end()

#define i64 long long
#define SET(t,v) memset((t), (v), sizeof(t))
#define REV(x) reverse( ALL( x ) )

#define IO freopen("B.in","r",stdin); freopen("B.out","w",stdout);
#define debug(x) cerr << __LINE__ <<" "<< #x " = " << x << endl

#define M 105

char ans[M][M];
int g[M][M], nr, nc;
int memo[M][M];

// N W E S
int dr[] = {-1,0,0,1};
int dc[] = {0,-1,1,0};

int solve( int r, int c ) {
	int& ret = memo[r][c];
	if( ret != -1 ) return ret;

	int d = -1;
	REP(i,4) {
		int rr = r + dr[i], cc = c + dc[i];
		if( rr < 0 || cc < 0 || rr >= nr || cc >= nc ) continue;
		if( g[rr][cc] < g[r][c] && ( d == -1 || g[rr][cc] < g[ r + dr[d] ][ c + dc[d] ] )) d = i;
	}

	if( d == -1 ) return ret = r * 1000 + c;
	return ret = solve( r + dr[d], c + dc[d] );
}


int main() {
	int t, ncase = 0;
	
	IO

	scanf("%d",&t);
	while( t-- ) {
		printf("Case #%d:\n", ++ncase);
		scanf("%d %d",&nr,&nc);
		REP(i,nr) REP(j,nc) scanf("%d",&g[i][j]);
		SET( memo, -1 );
		REP(i,nr) REP(j,nc) solve(i,j);
		char last = 'a';
		
		bool done[M][M]; SET( done, 0 );
		REP(i,nr) REP(j,nc) if( !done[i][j] ) {
			int v = memo[i][j];
			REP(x,nr) REP(y,nc) if( v == memo[x][y] ) done[x][y] = true, ans[x][y] = last;
			last ++;
		}
		
		REP(i,nr) {
			REP(j,nc) {
				if( j ) printf(" ");
				printf("%c",ans[i][j]);
			}
			printf("\n");
		}
	}

	return 0;
}
