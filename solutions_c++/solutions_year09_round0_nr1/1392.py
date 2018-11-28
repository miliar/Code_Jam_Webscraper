#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
using namespace std;

#define VV vector
#define PB push_back
#define ll long long
#define ld long double
#define REP(i,n) FOR(i,0,(n)-1)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FORE(a,b) for(VAR(a,(b).begin()),VAR(_b,(b).end());a!=_b;++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SS(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))
#define VI VV<int>
#define VS VV<string>
int COND = 1;
#define DB(x) { if (COND > 0) { COND--; REP (xxx, 1) cerr << __LINE__ << " " << #x << " " << x << endl; cerr.flush(); } }
//--

//int A[1][1];

char d[5000][15];
int L, D, N;
int go() {
	return 0;
}

int solve() {
	char w[1000];
	cin >> w;
	DB(w);
	int n = 0;
	bool b = false;
	bool m[5000];
	bool bm[5000];
	CLR(m, true);
	REP(i, 1000) {
		char c = w[i];
		if (w[i] == 0) break;
		if (c == '(') {b = true; CLR(bm, false); continue;}
		if (c == ')') {
			b = false;
			REP(i, D) if(!bm[i]) m[i] = false;
			n++;
			continue;
		}
		if (b){
			REP(i, D) if(d[i][n]==c) bm[i] = true;
		}else{
			REP(i, D) if(d[i][n]!=c) m[i] = false;
		}
		if(!b)n++;
	}
	int cnt = 0;
	REP(i,D) if(m[i]) cnt++;
    return cnt;
}

int main(int argc, char ** argv) { ios::sync_with_stdio(false);
    COND = argc >= 2 && argv[1][0] == 'q' ? (int)1e9 : 0;
    cin >> L >> D >> N;
	REP (i, D) REP (j, L) cin >> d[i][j];
    FOR (c, 1, N) {
        printf("Case #%d: %d\n", c, solve());
    }
    return 0;
}
