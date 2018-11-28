#include<cstdio>
#include<algorithm>
#include<cstring>
#include<iostream>
#include<utility>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> PII;

#define MP make_pair
#define PB push_back
#define REP(i, n) for(int i=0, _n=(n); i<_n; ++i)
#define min(a, b) ((a)<(b)?(a):(b))
#define max(a, b) ((a)>(b)?(a):(b))

const int MAXN = 1010;

struct Corridor {
	int b, e, w;
} a[MAXN];
int n, x, s, r, t;

bool cmp(const Corridor &a, const Corridor &b)
{
	return a.w < b.w;
}

int main()
{
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt) {
		printf("Case #%d: ", tt);
		scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
		double ans = 0.0;
		double left = t;
		
		for (int i = 0; i < n; ++i)
			scanf("%d%d%d", &a[i].b, &a[i].e, &a[i].w);

		int last = 0;
		for (int i = 0; i < n; ++i) {
			double tmp;
			if (last < a[i].b) {
				tmp = a[i].b - last;
				if (tmp / r > left) {
					ans += left;
					ans += (tmp - left * r) / s;
					left = 0.0;
				} else {
					ans += tmp / r;
					left -= tmp / r;
				}
			}
			last = a[i].e;
		}

		if (x > last) {
			double tmp;
			tmp = x - last;
			if (tmp / r > left) {
				ans += left;
				ans += (tmp - left * r) / s;
				left = 0.0;
			} else {
				ans += tmp / r;
				left -= tmp / r;
			}
		}

		sort(a, a + n, cmp);

		for (int i = 0; i < n; ++i) {
			double tmp;
			//cout << a[i].b << ' ' << a[i].e << ' ' << a[i].w << endl;
			tmp = a[i].e - a[i].b;
			double spdr = a[i].w + r;
			double spds = a[i].w + s;
			if (tmp / spdr > left) {
				ans += left;
				ans += (tmp - left * spdr) / spds;
				left = 0.0;
			} else {
				ans += tmp / spdr;
				left -= tmp / spdr;
			}
//			cout << ans << endl;
		}
		last = 0;
		
		printf("%.6lf\n", ans);
		
	}
	return 0;
}
