#include <cstdio>

int T, qa, qb;
long long w, h, x1, x2, y1, y2, cx, cy, q[2][1000000], t[2], ans, cnt, zz;
bool v[1000000];

bool valid(int x, int y) {
	return 0 <= x && x < w && 0 <= y && y < h;
}

long long f(int x, int y, int vx, int vy) {
	long long ans = 1ll << 50, mx = 1ll << 50, my = 1ll << 50;
	if (vx > 0)
		mx = (w - 1 - x)/vx;
	if (vx < 0)
		mx = x/(-vx);
	if (vy > 0)
		my = (h - 1 - y)/vy;
	if (vy < 0)
		my = y/(-vy);
	if (mx < ans)
		ans = mx;
	if (my < ans)
		ans = my;
	return ans;
}

int main() {
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		scanf("%lld%lld", &w, &h);
		scanf("%lld%lld", &x1, &y1);
		scanf("%lld%lld", &x2, &y2);
		scanf("%lld%lld", &cx, &cy);
		if (x1*y2 == x2*y1) {
			ans = 0;
			if (!x1) {
				x1 ^= y1 ^= x1 ^= y1;
				x2 ^= y2 ^= x2 ^= y2;
				w ^= h ^= w ^= h;
				cx ^= cy ^= cx ^= cy;
			}
			for (int i = 0; i < w; ++i)
				v[i] = 0;
			qa = qb = 0;
			q[0][qb] = cx;
			q[1][qb] = cy;
			++qb;
			v[cx] = 1;
			while (qa < qb) {
				t[0] = q[0][qa];
				t[1] = q[1][qa];
				++qa;
				if (valid(t[0] + x1, t[1] + y1) && !v[t[0] + x1]) {
					q[0][qb] = t[0] + x1;
					q[1][qb] = t[1] + y1;
					++qb;
					v[t[0] + x1] = 1;
				}
				if (valid(t[0] + x2, t[1] + y2) && !v[t[0] + x2]) {
					q[0][qb] = t[0] + x2;
					q[1][qb] = t[1] + y2;
					++qb;
					v[t[0] + x2] = 1;
				}
			}
			for (int i = 0; i < w; ++i)
				if (v[i])
					++ans;
		} else {
			ans = 0;
			while (valid(cx, cy)) {
				ans += (zz = f(cx, cy, x2, y2) + 1);
				cx += x1;
				cy += y1;
				cnt = 0;
				while (!valid(cx, cy) && cnt < 1100000)
					cx += x2, cy += y2, ++cnt;
				if (zz <= cnt)
					break;
			}
		}
		printf("Case #%d: %lld\n", r, ans);
	}
	return 0;
}
