#include <stdio.h>
#include <math.h>
#include <utility>
#include <string>
#include <vector>
#include <queue>
#include <map>
using namespace std;

#define TRACE(x...)
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x << " = " << endl)

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define _foreach(it, b, e) for (typeof(b) it = (b); it != (e); ++it)
#define foreach(x...) _foreach(x)
#define rep(i, n) foreach(i, 0, n)

#define MSET(c, v) memset(c, v, sizeof(c))

const int INF = 0x3f3f3f3f; const int NEGINF = 0xC0C0C0C0;
const int NULO = -1;
double EPS = 1.e-10;

inline int cmp(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}
long long int X[60];
long long int V[60];
int main() {
	TRACE(setbuf(stdout, NULL));
	int T;
	scanf("%d", &T);
	rep(_42, T) {
		long long int N, K, B, T;
		scanf("%lld %lld %lld %lld", &N, &K, &B, &T);
		rep(i, N) scanf("%lld", &X[i]);
		rep(i, N) scanf("%lld", &V[i]);
		long long int nja = 0, nnao = 0, nsw = 0;
		for (int j = N-1; j >= 0; j--) {
			if (nja == K) continue;
			if (X[j] + V[j]*T >= B) {
				nja++;
				nsw += nnao;
			} else {
				nnao++;
			}
		}
		if (nja == K)	printf("Case #%d: %lld\n", _42+1, nsw);
		else printf("Case #%d: IMPOSSIBLE\n", _42+1);
	}
	return 0;
}
