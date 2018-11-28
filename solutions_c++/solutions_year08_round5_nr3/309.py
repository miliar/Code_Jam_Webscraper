#pragma warning (disable:4786) 
#pragma warning (disable:4996) 
#include <time.h>
#include <algorithm> 
#include <iostream>  
#include <sstream> 
#include <string> 
#include <vector> 
#include <queue> 
#include <stack>
#include <set> 
#include <map> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 
#include <cassert>
using namespace std;

#define PB push_back
#define MP make_pair
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define FORSZ(i,a,v) FOR(i,a,SZ(v))
#define REPSZ(i,v) REP(i,SZ(v))
typedef long long ll; 
const double EPS = 1e-7;

void openfiles() {
	#ifndef ONLINE_JUDGE
		freopen("test.in","rt",stdin);
		freopen("test.out","wt",stdout);   
	#endif
}

bool valid(int state, char* G, int M) {
	REP(i,M) if (((state >> i) & 1) && G[i] == 'x') return false;
	FOR(i,1,M) 
		if (((state >> i) & 1) && ((state >> (i - 1)) & 1)) {
			//cout << i << endl;
			return false;
		}
	return true;
}

int ones(int state, int M) {
	int s = 0;
	REP(i,M) if ((state >> i) & 1) s++;
	return s;
}

void print(int state, int M) {
	REP(i,M) cout << ((state >> i) & 1);
	cout << endl;
}

int convert(int state, int M) {
	int nextstate = 0;
	REP(i,M) if ((state >> i) & 1) {
		if (i - 1 >= 0) nextstate |= (1 << (i - 1));
		if (i + 1 < M) nextstate |= (1 << (i + 1));
	}
	return nextstate;
}

void solve() {
	char G[100][100];
	int N, M;
	scanf("%d %d ",&N,&M);
	REP(i,N) gets(G[i]);
	/*REP(i,N) cout << G[i] << endl;*/

	int DP[20][2000];
	memset(DP, 0, sizeof(DP));
	for (int i = N; i > 0; i--) {
		// for every possible combination
		/*cout << "i = " << i << endl;*/
		for (int j = 0; j < (1 << M); j++) if (valid(j, G[i-1], M)) {
			// we see if we can put here the combination
			/*cout << j << endl;
			cout << "" << endl;*/
			for (int k = 0; k < (1 << M); k++) {
				if (j & k) continue;
				int next = convert(j, M);
				DP[i-1][next] = max(DP[i-1][next], DP[i][k] + ones(j, M));
				//cout << j << " " << k << endl;
				//cout << DP[i-1][next] << endl;
			}
		}
	}
	//REP(i,N) {
	//	cout << "i = " << i << endl;
	//	REP(j,1<<M) {
	//		print(j,M);
	//		cout << DP[i][j] << endl;
	//	}
	//}
	int best = 0;
	REP(i,1<<M) best = max(best, DP[0][i]);
	static int test = 0;
	printf("Case #%d: %d\n",++test,best);
}

int main() {
	openfiles();
	int n; scanf("%d",&n);
	REP(i,n) solve();

	return 0;
}