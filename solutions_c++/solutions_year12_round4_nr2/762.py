#include<vector>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int N = 1000;
int x[N], y[N];
struct Id {
	int x, y;
	bool operator<(const Id &t)const {
		return x < t.x;
	}
} a[N];
struct TPoint {
	int x1, y1, x2, y2;
} p;
vector<TPoint>b;
int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int i, j, n, t, tt, w, l, r, s, u, v;
	scanf("%d", &tt);
	for (t = 1; t <= tt; t++) {
		scanf("%d%d%d", &n, &w, &l);
		for (i = 0; i < n; i++) {
			scanf("%d", &a[i].x);
			a[i].y = i;
		}
		sort(a, a + n);

		b.clear();
		p.x1 = 0;
		p.y1 = 0;
		p.x2 = w;
		p.y2 = l;
		b.push_back(p);

		for (i = n - 1; i >= 0; i--) {
			for (j = 0; j < b.size(); j++) {
				r = b[j].x1;
				s = b[j].x2;
				u = b[j].y1;
				v = b[j].y2;
				if (r == 0)r -= a[i].x;
				if (s == w)s += a[i].x;
				if (u == 0)u -= a[i].x;
				if (v == l)v += a[i].x;

				if (s - r >= 2*a[i].x && v - u >= 2*a[i].x) {
					x[a[i].y] = r + a[i].x;
					y[a[i].y] = u + a[i].x;

					p.x1 = r + 2 * a[i].x;
					p.x2 = b[j].x2;
					p.y1 = b[j].y1;
					p.y2 = u + 2 * a[i].x;
					b.push_back(p);

					p.x1 = b[j].x1;
					p.x2 = r + 2 * a[i].x;
					p.y1 = u + 2 * a[i].x;
					p.y2 = b[j].y2;
					b.push_back(p);

					p.x1 = r + 2 * a[i].x;
					p.x2 = b[j].x2;
					p.y1 = u + 2 * a[i].x;
					p.y2 = b[j].y2;
					b.push_back(p);

					b.erase(b.begin() + j);

					break;
				}
			}
			if (j == b.size())puts("error");
//			printf("-%d-\n", i);
//			for (j = 0; j < b.size(); j++)
//				printf("%d %d %d %d\n", b[j].x1, b[j].x2, b[j].y1, b[j].y2);
		}
		printf("Case #%d:", t);
		for (i = 0; i < n; i++)
			printf(" %d %d", x[i], y[i]);
		printf("\n");
	}
	return 0;
}
