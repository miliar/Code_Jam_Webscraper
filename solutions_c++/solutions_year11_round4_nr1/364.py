#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

typedef pair <int, int> PII;

const double EPS = 1e-8;

int T, X, S, R, n;
double t;
PII a[1001];

int main() {
	scanf("%d", &T);
	for (int caseNum = 1; caseNum <= T; ++caseNum) {
		scanf("%d%d%d%lf%d", &X, &S, &R, &t, &n);
		a[n] = make_pair(0, X);
		for (int i = 0; i < n; ++i) {
			int B, E, L, w;
			scanf("%d%d%d", &B, &E, &w);
			L = E - B;
			a[i] = make_pair(w, L);
			a[n].second -= L;
		}
		sort(a, a + n + 1);
		double res = 0.0;
		for (int i = 0; i <= n; ++i) {
			int w = a[i].first, L = a[i].second;
			if (t * (R + w) > L + EPS) {
				res += (double)L / (R + w);
				t -= (double)L / (R + w);
			} else {
				res += t;
				res += (double)(L - t * (R + w)) / (S + w);
				t = 0;
			}
		}
		printf("Case #%d: %.13lf\n", caseNum, res);
	}
	return 0;
}
