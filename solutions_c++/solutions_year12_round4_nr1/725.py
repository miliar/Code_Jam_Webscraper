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

#define MAX 12345
int D[MAX], L[MAX], M[MAX];

int main() {
	int T; scanf("%d", &T);
    FORTO(t,1,T) {
		int N, R; scanf("%d", &N);
		FOR(i,N) scanf("%d %d", &D[i], &L[i]);
		scanf("%d", &R);
		M[0] = D[0];
		FORTO(i,1,N-1) {
			M[i] = 0;
			FOR(j,i) if (M[j] >= D[i]-D[j]) M[i] = max(M[i],D[i]-D[j]);
			M[i] = min(M[i],L[i]);
		}
		bool res = false;
		FOR(i,N) if (D[i]+M[i] >= R) res = true;
		printf("Case #%d: %s\n", t, res ? "YES" : "NO");
	}
	return 0;
}
