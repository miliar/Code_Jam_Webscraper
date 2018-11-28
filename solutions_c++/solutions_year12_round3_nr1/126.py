// solution by Peter Ondruska

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <climits>
#include <cstring>

#include <iostream>
#include <sstream>
#include <complex>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <stack>
#include <bitset>
#include <utility>
#include <numeric>
#include <functional>
#include <algorithm>
using namespace std;

typedef pair<int,int> PII;
typedef long long ll;

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORTO(i,a,b)  for(int i=(a);i<=(b);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)
#define FORDTO(i,a,b) for(int i=(a);i>=(b);i--)
#define FOREACH(it,t) for(typeof(t.begin()) it=t.begin(); it!=t.end(); ++it)

#define DEBUG(x) cout<<'>'<<#x<<':'<<(x)<<endl
#define SIZE(X) int(X.size())

#define MAXN 1047
int N, D[MAXN][MAXN];

bitset<1001> W[MAXN];

bool DFS(int v) {
	if (W[v][v]) return false;
	FORTO(i,1,N) if (D[v][i]) {
		if (DFS(i)) return true;
		if ((W[v] & W[i]).any()) return true;
		W[v] |= W[i];
	}
	W[v][v] = true;
	return false;
}

int main() {
    int T;
    scanf("%d", &T);
    FORTO(t,1,T) {
		scanf("%d", &N);
		FORTO(i,1,N) FORTO(j,1,N) D[i][j] = 0;
		FORTO(i,1,N) {
			int A, M; scanf("%d", &M);
			FOR(j,M) { scanf("%d", &A); D[A][i] = 1; }
		}
		FORTO(i,1,N) W[i].reset();
		bool yes = false;
		FORTO(v,1,N) if (DFS(v)) {
			yes = true;
			break;
		}
		printf("Case #%d: %s\n", t, yes ? "Yes" : "No");
    }
	return 0;
}
