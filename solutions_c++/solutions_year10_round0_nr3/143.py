#include <cstdio>
#include <cstring>
#include <deque>

using namespace std;

const __int64 MAX_N = 1010;

struct node {
	__int64 p, r, s;
};

node b[MAX_N];
__int64 a[MAX_N];
__int64 v[MAX_N];
__int64 r, k, n;
__int64 cas, ret;

int main() {
	freopen("D:\\c.in", "r", stdin);
	freopen("D:\\c.out", "w", stdout);
	scanf("%d", &cas);
	for (__int64 cc = 1; cc <= cas; ++cc) {
		scanf("%I64d%I64d%I64d", &r, &k, &n);
		deque <__int64> dq;
		for (__int64 i = 1; i <= n; ++i) {
			scanf("%I64d", a + i);
			dq.push_back(a[i]);
		}
		__int64 pos = 1, t = 1;
		ret = 0;
		memset(v, 0, sizeof(v));
		while (t <= r) {
			__int64 sum = 0;
			if (!v[pos]) {
				b[t].p = pos;
				v[pos] = t;
			} else {
				__int64 l = t - v[pos];
				sum = b[t - 1].s - b[v[pos] - 1].s;
				ret = b[v[pos] - 1].s;
				ret += (r - (v[pos] - 1)) / l * sum;
				if ((r - (v[pos] - 1)) % l) {
					ret += b[v[pos] - 1 + (r - (v[pos] - 1)) % l].s - b[v[pos] - 1].s;
				}
				break;
			}
			for (__int64 i = 1; i <= n && sum + dq.front() <= k; ++i) {
				sum += dq.front();
				dq.push_back(dq.front());
				dq.pop_front();
				pos = pos % n + 1;
			}
			b[t].s = b[t - 1].s + sum;
			b[t].r = t++;
		}
		if (!ret) {
			ret = b[t - 1].s;
		}
		printf("Case #%I64d: %I64d\n", cc, ret);
	}
	return 0;
}
