#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <iterator>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

/* Prewritten code begins */
#define REP(i,n)    for(int i=0; i<(n); ++i)
#define FORD(i,a,b) for(int i=(a); i>=(b); --i)
#define IN(x,l)     (0<=(x)&&(x)<(l))
#define FOR(i,a,b)  for(int i=(a); i<=(b); ++i)
/* Prewritten code ends */

const int maxN = 55;
char s[maxN][maxN], R[maxN][maxN];
int N;
int dr[] = {0,1,1,1};
int dc[] = {1,0,-1,1};
void rot() {
	REP(i,N) REP(j,N) R[j][N-1-i] = s[i][j];
}
void gr() {
	REP(c,N) {
		int rr = N-1;
		FORD(r,N-1,0) if(R[r][c]!='.') R[rr--][c] = R[r][c];
		FORD(r,rr,0) R[r][c] = '.';
	}
//	REP(i,N) cout << R[i] << endl;
}
int check(char ch, int k) {
	REP(r,N) REP(c,N) if(R[r][c]==ch) {
		REP(i,4) if(IN(r+(k-1)*dr[i],N)&&IN(c+(k-1)*dc[i],N)) {
			FOR(j,1,k-1) if(R[r+j*dr[i]][c+j*dc[i]]!=ch) goto C;
			return 1;
C:;		}
	}
	return 0;
}
int main() {
	int T, K, isb, isr;
	scanf("%d",&T);
	FOR(cs,1,T) {
		scanf("%d%d",&N,&K);
		REP(i,N) scanf("%s",s[i]);
		rot();
		gr();
		isb = check('B',K);
		isr = check('R',K);
		printf("Case #%d: %s\n",cs,(isr&&isb)?"Both":isr?"Red":isb?"Blue":"Neither");
	}
	return 0;
}
