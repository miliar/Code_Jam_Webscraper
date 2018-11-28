#include<iostream>
#include<algorithm>
using namespace std;

const int maxn = 1000 + 10;

int n, ind[maxn];
double x, b[maxn], e[maxn], w[maxn], s, r, t;
void init()
{
	scanf("%lf %lf %lf %lf %d", &x, &s, &r, &t, &n);
	double tx = x;
	for (int i = 0; i < n; i++) {
		scanf("%lf %lf %lf", b + i, e + i, w + i);
		tx -= e[i] - b[i];
	}
	b[n] = 0; e[n] = tx; w[n++] = 0;
}

bool cmp(const int v0, const int v1) 
{
	return w[v0] < w[v1];
}

void solve()
{
	for (int i = 0; i < n; i++) ind[i] = i;
	sort(ind, ind + n, cmp);	
	double ans = 0;
	for (int i = 0; i < n; i++) {
		int cur = ind[i];
		double l = e[cur] - b[cur];
		if (t > 1e-8) {
			double ts = l / (w[cur] + r);
			if (t >= ts) {
				t -= ts;
				ans += ts;
			} else {
				ans += t + (l - (w[cur] + r) * t) / (w[cur] + s);
				t = 0;
			}
		} else {
			ans += l / (w[cur] + s);
		}
	}
	printf("%.9lf\n", ans);
}

int main()
{
	int t, T;
	for (scanf("%d\n", &T), t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		init();
		solve();
	}
}