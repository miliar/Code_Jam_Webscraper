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

#define N 2048
int n;
int a[N], ans[N];
int st[N], stp;

int main() {
	int __;
	scanf("%d", &__);
	forn(_, __) {
		scanf("%d", &n);
		forn(i, n-1) scanf("%d", &a[i]), a[i]--;
		bool shit = 0;
		forn(i, n-1) for (int j = i+1; j < a[i]; j++) shit |= (a[j] > a[i]);
		int it = 0;
		if (shit) goto ans;
		
		while (1) {
if (++it==50000000) { shit = 1; break; }
			forn(i, n) ans[i] = rand() % 300;
			bool good = 1;
			forn(i, n-1) {
				for (int j = i + 1; j < n; j++) if (j != a[i]) {
					if ((ans[a[i]]-ans[j])*(a[i]-i) <= (ans[a[i]]-ans[i])*(a[i]-j)) {
						good = 0;
						break;
					}
				}
			}
			if (good) break;
		}
		eprintf("%d: %d %d\n", _+1, n, it);
		
		ans: printf("Case #%d:", _+1);
		if (shit) puts(" Impossible");
		else {
			forn(i, n) printf(" %d", ans[i]);
			puts("");
		}
	}
	return 0;
}
