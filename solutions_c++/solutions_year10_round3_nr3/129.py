#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<cstdio>
#include<cstdlib>
#include<cctype>
#include<cmath>

#define FOR(i,a,b) for(int i=(a),_n=(b); i<=_n; i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_n=(b);i>=_n; i--)
#define FILL(i,v) memset((i),(v),sizeof((i)))
#define DEBUG(x) cout <<"  >> "<<#x<<" => "<<x <<endl
#define ABS(x) ((x<0) ? –x : x)
#define ALL(x) x.begin(),x.end()
#define MAX(a,b) ((a<b) ? b : a)
#define MIN(a,b) ((a<b) ? a : b)
#define MP make_pair
#define PB push_back
#define INF 1000000000


using namespace std;
typedef long long LL;
const double EPS = 1.e-9;

void OPEN(string name) {
	string in = name + ".in";
	freopen(in.c_str(), "r", stdin);
	string out = name + ".out.txt";
	freopen(out.c_str(), "w", stdout);
}

string conv( int x ) {
	if ( !x ) return "";
	string ret = "";
	ret.push_back( '0' + (x%2) );
	return conv( x/2 ) + ret;
}

int trans(char x) {
	if ( 'A' <= x && x <= 'F' ) return 10+x-'A';
	else return x-'0';
}

string board[600];
char nBoard[300];
int nAns[520], M, N;
int vis[600][600];

int check(int r, int c, int K) {

	int nNow = (board[r][c] == '1'); // 0 = black, 1 = white
	int can = 1;
	for(int i=r, to = 0; can && to < K; to++, i++) {
		int NOW = nNow;
		for(int k=c, _to = 0; can && _to < K; _to++, k++) {
			if ( vis[i][k] ) can = 0;
			if ( can && (board[i][k]-'0') != NOW ) can = 0;
			if ( can ) NOW = !NOW;
		}
		nNow = !nNow;
	}
	if ( can ) {
		for(int i=r, to = 0; can && to < K; to++, i++) {
			for(int k=c, _to = 0; can && _to < K; _to++, k++) vis[i][k] = 1;
		}
	}
	return can;
}

int main() {
	OPEN("Csmall0");
	int ntc;
	scanf("%d", &ntc);
	for(int TC=1; TC <= ntc; TC++) {
		scanf("%d %d", &M, &N);
		for(int i=0; i<M; i++) {
			board[i] = "";
			scanf("%s", nBoard);
			for(int k=0; k < N/4; k++) {
				string ns = conv( trans(nBoard[k]) );
				if ( ns == "" ) ns = "0";
				while( ns.length()%4 != 0 ) ns = "0" + ns;
				board[i] += ns;
			}
		}
		FILL(vis, 0);
		FILL(nAns, 0);
		for(int K=MIN(M,N); K >= 1; K--) {
			for(int i=0; i+K<=M; i++) {
				for(int k=0; k+K<=N; k++) {
					if ( check(i, k, K) ) {
					//	if ( K > 1 ) printf(" %d : %d %d\n", K, i, k);
						nAns[K]++;
					}
				}
			}
		}
		int ans = 0;
		for(int K=MIN(M,N); K >= 1; K--) if ( nAns[K] > 0 ) ans++;
		printf("Case #%d: %d\n", TC, ans);
		for(int K=MIN(M,N); K >= 1; K--) if ( nAns[K] > 0 ) printf("%d %d\n", K, nAns[K] );
	}
	return 0;
}
