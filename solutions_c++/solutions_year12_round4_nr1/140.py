#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdarg>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <functional>
#include <iterator>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define forn(i, n) for (int i = 0; i < (n); i++)
#define forit(it, v) for (typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define eprintf(...) { fprintf(stderr, __VA_ARGS__); fflush(stderr); }
#define sz(v) ((int)((v).size()))
typedef pair<int, int> ii;
typedef long long LL;

#define N 100500
int n;
int d[N], l[N];
int a[N];

int main() {
	int __;
	scanf("%d", &__);
	forn(_, __) {
		scanf("%d", &n);
		forn(i, n) scanf("%d%d", &d[i], &l[i]);
		int D;
		scanf("%d", &D);
		memset(a, 0, sizeof a);
		a[0] = d[0];
		bool ans = false;
		forn(i, n) {
			if (!a[i]) break;
			if (a[i]+d[i] >= D) { ans = true; break; }
			for (int j = i + 1; j < n && d[j] <= d[i] + a[i]; j++) {
				a[j] = max(a[j], min(l[j], d[j] - d[i]));
			}
		}
		printf("Case #%d: ", _+1);
		puts(ans ? "YES" : "NO");
	}
	return 0;
}
