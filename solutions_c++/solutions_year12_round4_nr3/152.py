#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define DEBUG(x) cout << ">>> " << #x << " = " << (x) << endl;
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,a) for(int i=0;i<(a);++i)

#define INF (1<<29)
typedef long long ll;

#define MAXN 20

int T, N;
int S[MAXN];
int res[MAXN];

int main() {
	scanf("%d", &T);
	REP(t,T) {
		scanf("%d", &N);
		REP(i,N-1) {scanf("%d", S+i); --S[i];}
		S[N-1] = N-1;
		bool pos = true;
		FORD(i,N-1,0) {
			int m = 0, M = 1000000000;
			//DEBUG(i);
			//DEBUG(S[i]);
			FOR(j,i+1,S[i]-1) {
				//DEBUG(j);
				m = max(m, (int)ceil(res[S[i]]-(double)(res[S[i]]-res[j])*(S[i]-i)/(S[i]-j)));
			}
			//DEBUG("a");
			FOR(j,S[i]+1,N-1) {
				//DEBUG(j);
				M = min(M, (int)floor(res[S[i]]-(double)(res[j]-res[S[i]])*(S[i]-i)/(j-S[i])));
			}
			//DEBUG(m);
			//DEBUG(M);
			if (m > M) { pos = false; break; }
			if (abs(500000000-m) < abs(500000000-M)) res[i] = m+1;
			else res[i] = M-1;
			if (i >= N-2) res[i] = 500000000;
			//DEBUG(res[i]);
		}
		printf("Case #%d:", t+1);
		if (pos) {
			REP(i,N) printf(" %d", res[i]);
			printf("\n");
		} else printf(" Impossible\n");
	}
	return 0;
}
