#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

typedef pair<int, int> pii;
typedef long long llong;

#define mp make_pair
#define lowbit(x) ((x) & (-(x)))
#define pf(x) ((x) * (x))
#define two(x) (1 << (x))
#define twoL(x) ((llong) 1 << (x))
#define clr(x, c) memset(x, c, sizeof(x))

inline void ch_max(int &x, int y) {if (x < y) x = y;}
inline void ch_min(int &x, int y) {if (x > y) x = y;}

const double pi = acos(-1.0);
const double eps = 1e-9;


const int N = 10005;
int d[N], l[N], D;
int n;

int a[N];

int main() {
	freopen("GCJ\\A-large.in", "r", stdin);
	//freopen("GCJ\\in.txt", "r", stdin);
	freopen("GCJ\\out.txt", "w", stdout);
	int i, j, k, t, nc = 0;
	scanf("%d", &t);
	while (t--) {
		scanf("%d", &n);
		for (i = 0; i < n; ++i) {
			scanf("%d%d", &d[i], &l[i]);
		}
		scanf("%d", &D);
		clr(a, 0);
		a[0] = 2 * d[0];
		for (i = 1; i < n; ++i) {
			for (j = 0; j < i; ++j) {
				if (a[j] < d[i]) continue;
				ch_max(a[i], d[i] + min(d[i] - d[j], l[i]));
			}
		}
		int tmax = 0;
		for (i = 0; i < n; ++i) {
			tmax = max(tmax, a[i]);
		}
		if (tmax >= D) printf("Case #%d: YES\n", ++nc);
		else printf("Case #%d: NO\n", ++nc);
	}
	return 0;
}