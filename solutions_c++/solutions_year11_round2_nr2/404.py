#include <cstdio>
#include <cstring>
#include <algorithm>

namespace gcj {
	using namespace std;

	const int maxn = 6;
	typedef long long lld;

	struct node{
		lld p;
		lld v;
	};
	bool cmp(const node& l, const node& r) {
		return l.p < r.p;
	}

	node venders[maxn];

	void solve() {
		int t, n, _case = 0;
		scanf("%d", &t);
		while (t --) {
			_case ++;
			int d, c;
			scanf("%d %d", &c, &d);
			for (int i = 0; i < c; i ++)
				scanf("%lld %lld", &venders[i].p, &venders[i].v);

			sort(venders, venders + c, cmp);
			lld tmp, tl, last;
			lld sum = (venders[0].v - 1) * d;
			for (int i = 1; i < c; i ++) {
				tmp = (venders[i].v - 1) * d;
				tl = venders[i].p - venders[i].v * d;
				if (tmp > sum) {
					last = venders[i - 1].p - (tmp - sum);
					if(tl >= last)
						sum = tmp;
					else
						sum = tmp + last - tl;
				} else {
					last = venders[i - 1].p;
					if (tl >= last) {
						lld _m = min(tl - last, sum - tmp);
						venders[i].p -= _m;
					} else {
						sum += last - tl;
					}
				}
			}

			printf("Case #%d: %.1lf\n", _case, sum / 2.0);
		}
	}

}


int main() {
	freopen("D:/GCJ/Round2/B-large.in", "r", stdin);
	freopen("D:/GCJ/Round2/B-large.out", "w", stdout);

	gcj::solve();
	return 0;
}
