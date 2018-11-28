#include<iostream>
using namespace std;

const int maxc = 200 + 10;
double a[maxc][2];
int n;
double d, tot;

void init()
{
	tot = 0;
	scanf("%d %lf", &n, &d);
	for (int i = 0; i < n; i++) {	
		scanf("%lf %lf", &a[i][0], &a[i][1]);
		tot += a[i][1];
	}
}

double count_(double left, int cur) 
{
	double right = a[cur][1] - left - 1;
	double ret = 0;
	double base = a[cur][0];
	if (left > 0) ret = max(ret, d * left);
	if (right > 0) ret = max(ret, d * right);
	double tot = left;
	for (int i = cur - 1; i >= 0; i--) {		
		tot += a[i][1];
		double dis = tot * d;
		if (dis > base - a[i][0]) ret = max(ret, dis - base + a[i][0]);
	}
	tot = right;
	for (int i = cur + 1; i < n; i++) {
		tot += a[i][1];
		double dis = tot * d;
		if (dis > a[i][0] - base) ret = max(ret, dis - a[i][0] + base);
	}
	return ret;
}

void solve()
{/*
	double ans = 1e100;
	for (int i = 0; i < n; i++) {
		int le = 0, ri = int(a[i][1] + 0.5) - 1, m1, m2;
		while (ri - le + 1 > 3) {
			m1 = le + (ri - le + 1) / 3;
			m2 = ri - (ri - le + 1) / 3;
			if (count_(m1, i) < count_(m2, i))
				ri = m2 - 1;
			else le = m1 + 1;
		}
		for (int j = le; j <= ri; j++)
			ans = min(ans, count_(j, i));
	}	
	printf("%.10lf", ans);
	*/
	double le = 0, ri = d * tot, mid;
	for (int i = 0; i < 200; i++) {//while (ri - le > 1e-7) {
		mid = (le + ri) / 2;
		double lastp = -1e20;
		bool flag = true;
		for (int i = 0; i < n; i++) {
			double v1 = max(lastp + d, a[i][0] - mid);
			v1 += (a[i][1] - 1) * d;
			if (v1 > a[i][0] && (v1 - a[i][0]) > mid) {
				flag = false;
				break;
			}
			lastp = v1;
		}		
		if (flag)
			ri = mid;
		else le = mid;
	}
	printf("%.10lf", le);
}

int main()
{
	int T, t;
	for (scanf("%d\n", &T) > 0, t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		init();
		solve();
		printf("\n");
	}
}