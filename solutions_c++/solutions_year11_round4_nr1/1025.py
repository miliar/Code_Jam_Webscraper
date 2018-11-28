#include <iostream>
#include <cstdio>

using namespace std;
const int MXN = 1010;
struct TT {
	int b, e, w;
} g[MXN];
int x, s, r, t, n;
bool cmp(TT a, TT b)
{
	return a.w < b.w;
}
double walk(int len, int w)
{
	double t1 = double(len) / (s + w);
	double t2 = double(len) / (r + w);
	return t1;
}
double run(int len, int w) 
{
	double t1 = double(len) / (s + w);
	double t2 = double(len) / (r + w);
	return t2;
}
double run_t(int len, int w, double t) 
{
	double l1 = (r + w) * t;
	double t2 = double(len - l1) / (s + w);
	return t2 + t;
}
int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int _t = 1; _t <= T; ++_t) {
		
		
		scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
		double sum = t;
		int tot = 0;
		for (int i = 0; i < n; ++i) {
			scanf("%d%d%d", &g[i].b, &g[i].e, &g[i].w);
			tot += g[i].e - g[i].b;
		}
		sort(g, g + n, cmp);
		double ans = 0;
		tot = x - tot;
		//cout << tot << endl;
		double h = run(tot, 0);
		if (h > sum) h = sum;
		ans = run_t(tot, 0, h);
		sum -= h;
		for (int i = 0; i < n; ++i) {
			double h = run(g[i].e - g[i].b, g[i].w);
			if (h > sum) h = sum;
			sum -= h;
			ans += run_t(g[i].e - g[i].b, g[i].w, h);
		}
		
		printf("Case #%d: %.10lf\n", _t, ans);
	}
}
