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

inline double rnd() { return rand()*1./RAND_MAX; }

int n, W, H;
double ansx[1024], ansy[1024];

#define sqr(a) ((a)*(a))
inline double sqdist(double x1, double y1, double x2, double y2) { return (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2); }
inline double sqdist(int i, int j) { return sqdist(ansx[i], ansy[i], ansx[j], ansy[j]); }

void solve(int caze, vector<ii>& a) {
	sort(a.rbegin(), a.rend());
int it = 0;
	forn(i, n) {
		while (1) {
it++;
			ansx[a[i].second] = rnd() * W;
			ansy[a[i].second] = rnd() * H;
			bool good = true;
			forn(j, i) {
 				if (sqdist(a[j].second, a[i].second) < sqr(a[j].first + a[i].first + 0.) + 1e-2) {
					good = false;
					break;
				}
			}
			if (good) break;
		}
	}
eprintf("%d: %d %d\n", caze, n, it);
}

int main() {
	int __;
	scanf("%d", &__);
	forn(_, __) {
		scanf("%d%d%d", &n, &W, &H);
		vector<ii> a(n);
		forn(i, n) {
			a[i].second = i;
			scanf("%d", &a[i].first);
		}
		solve(_+1, a);
		printf("Case #%d:", _+1);
		forn(i, n) printf(" %.9lf %.9lf", ansx[i], ansy[i]);
		puts("");
	}
	return 0;
}
