#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<queue>
#include<cstring>
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
// C Small !
int m[120][120];

void spawn( int r, int c ) {
	if ( (m[r-1][c] == 1 || m[r-1][c] == 2) && (m[r][c-1] == 1 || m[r][c-1] == 2) ) m[r][c] = 3; // next to be spawn !
}

void die( int r, int c ) {
	if ( m[r-1][c] == 0 && m[r][c-1] == 0 ) m[r][c] = 2;
}

int finish() {
	int ret = 0;
	for(int i=1; i<=100; i++) for(int k=1; k <= 100; k++) ret += m[i][k];
	return (ret == 0);
}

int main() {
	OPEN("Csmall1");
	int ntc;
	scanf("%d", &ntc);
	for(int TC=1, R; TC <= ntc; TC++) {
		FILL( m, 0 );
		scanf("%d", &R);
		for(int i=0, x1, x2, y1, y2; i<R; i++) {
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			int rr1 = y1, rr2 = y2, rc1 = x1, rc2 = x2;
			// x = c ! y = r !
			for(int a = min(rr1, rr2), _to = max(rr1,rr2); a <= _to; a++) {
				for(int b = min(rc1, rc2), __to = max(rc1,rc2); b <= __to; b++) m[a][b] = 1;
			}
		}
		int ans = 0;
		while( !finish() ) {
		//	puts("");
			for(int i=1; i <= 100; i++) {
				for(int k=1; k <= 100; k++) {
					if ( m[i][k] == 0 ) spawn(i,k);
					else if ( m[i][k] == 1 ) die(i,k);
				}
			}
			for(int i=1; i <= 100; i++) {
				for(int k=1; k <= 100; k++) {
					if ( m[i][k] == 2 ) m[i][k] = 0;
					else if ( m[i][k] == 3 ) m[i][k] = 1;
				}
			}
		//	for(int i=1; i <= 10; i++) {
		//		for(int k=1; k <= 10; k++) printf(" %d ", m[i][k] );
		//		puts("");
		//	}
			ans++;
		}
		printf("Case #%d: %d\n", TC, ans);
	}

	return 0;
}
