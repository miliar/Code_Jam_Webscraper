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

int A[100][100];
int B[100][100];
int M[100][100];
int S[100][100];
bool V[100][100];
int H, W;
int nx = 0;

int go() {
	char m[10000];
	CLR(m,0);
	char n='a';
	REP(h, H) {REP(w, W) {
		int x=B[h][w];
		if(m[x]==0)m[x]=n++;
		cout << m[x] << " "; 
	}cout << endl;}
	return 0;
}

void update(int h, int w, int c) {
	B[h][w] = c;
	V[h][w] = true;
	if (h>0&&!V[h-1][w]&&(S[h-1][w]==3||S[h][w]==0)) update(h-1,w,c);
	if (w>0&&!V[h][w-1]&&(S[h][w-1]==2||S[h][w]==1)) update(h,w-1,c);
	if (w<W-1&&!V[h][w+1]&&(S[h][w+1]==1||S[h][w]==2)) update(h,w+1,c);
	if (h<H-1&&!V[h+1][w]&&(S[h+1][w]==0||S[h][w]==3)) update(h+1,w,c);
}

void sett() {
	REP(h, H) REP(w, W) {
		if (h>0&&(S[h-1][w]==3||S[h][w]==0)) {B[h][w] = B[h-1][w];}
		if (w>0&&(S[h][w-1]==2||S[h][w]==1)) {
			if(B[h][w]!=-1){
				CLR(V, false);
				V[h][w] = true;
				update(h,w-1,B[h][w]);
			}
			else B[h][w] = B[h][w-1];
		}
		if(B[h][w]==-1)B[h][w] = nx++;
	}

}

int solve() {
    CLR(A, 0);
    CLR(B, -1);
    CLR(M, 20000);
    CLR(S, 10);
    cin >> H >> W;
	REP(h, H) REP(w, W) {
		cin >> A[h][w];
		M[h][w] = A[h][w];
		if(h>0 && M[h][w]>A[h-1][w]){ M[h][w] = A[h-1][w]; S[h][w] = 0; }
		if(w>0 && M[h][w]>A[h][w-1]){ M[h][w] = A[h][w-1]; S[h][w] = 1; }
		if(w>0 && M[h][w-1]>A[h][w]){ M[h][w-1] = A[h][w]; S[h][w-1] = 2; }
		if(h>0 && M[h-1][w]>A[h][w]){ M[h-1][w] = A[h][w]; S[h-1][w] = 3; }
	}
	nx=0;
	sett();
    return go();
}

int main(int argc, char ** argv) { ios::sync_with_stdio(false);
    COND = argc >= 2 && argv[1][0] == 'q' ? (int)1e9 : 0;
    int T; cin >> T;
    FOR (c, 1, T) {
        printf("Case #%d:\n", c); solve();
    }
    return 0;
}
