#include <iostream>
#include <cassert>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstdlib>

using namespace std;

const int N = 1005;
int T, n;
double ansx[N], ansy[N];
double W, H;
pair<double, int> pii[N];
double r[N];

double sqr(double x)
{ return x * x; }

bool isok(double x, double y, int n)
{
	for (int i = 0; i < n; ++i) {
		double d2 = sqr(x - ansx[pii[i].second]) + sqr(y - ansy[pii[i].second]);
		if (d2 < sqr(pii[i].first + pii[n].first)) return false;
	}
	return true;
}

double get_r(double t)
{
	return (double)(rand() % 32768) * t / 32768;
}

void work()
{
	static int ttt = 0;
	printf("Case #%d:", ++ttt);
	scanf("%d%lf%lf", &n, &W, &H);
	for (int i = 0; i < n; ++i) {
		scanf("%lf", &r[i]);
		pii[i].first = r[i];
		pii[i].second = i;
	}
	sort(pii, pii + n, greater<pair<double, int> >());
	while (1) {
		bool find = true;
		for (int i = 0; i < n; ++i) {
			bool find_thisround = false;
			for (int iter = 0; iter < 100; ++iter) {
				double tx = get_r(W);
				double ty = get_r(H);
				ansx[pii[i].second] = tx;
				ansy[pii[i].second] = ty;
				if (isok(tx, ty, i)) { find_thisround = true; break; }
			}
			if (!find_thisround) find = false;
		}
		if (find) break;
	}
	for (int i = 0; i < n; ++i) printf(" %0.5lf %0.5lf", ansx[i], ansy[i]);
	
	for (int i = 0; i < n; ++i) for (int j = 0; j < n; ++j) if (i != j) {
		double d2 = sqr(ansx[i] - ansx[j]) + sqr(ansy[i] - ansy[j]);
		if (d2 < r[i] * r[i] + 1e-3 || d2 < r[j] * r[j] + 1e-3) {
			printf("%d %d %0.3lf %0.3lf %0.3lf\n", i, j, d2, r[i] * r[i], r[j] * r[j]);
			assert(false);
		}
	}
	
	printf("\n");
}

void generate()
{
	freopen("B.in", "w", stdout);
	T = 50;
	n = 120;
	printf("%d\n", T);
	for (int t = 0; t < T; ++t) {
		double sum = 0;
		for (int i = 0; i < n; ++i) {
			r[i] = get_r(100000);
			sum += r[i] * r[i];
		}
		sum *= 5.1;
		
		printf("%d %d %d\n", n, (int)sqrt(sum), (int)sqrt(sum));
		for (int i = 0; i < n; ++i) printf("%d ", (int)r[i]);
		printf("\n");
	}
	fclose(stdout);
	exit(0);
}

int main()
{
	//generate();
	scanf("%d", &T);
	while (T--) work();
}