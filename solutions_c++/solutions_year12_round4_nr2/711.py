#include <stdio.h>
#include <math.h>
#include <string.h>
#include <algorithm>
using namespace std;

struct Point {
	double x, y;
} c[1010], a[1010][1010];
int cs, ct;
int n;
double w, l;
double r[1010];
int s[1010];

double sqr(double x)
{
	return x * x;
}

double dis(Point a, Point b)
{
	return sqr(a.x - b.x) + sqr(a.y - b.y);
}

bool conflict(Point a, int k)
{
	for (int i = 0; i < k; i++)
		if (dis(a, c[s[i]]) + 1e-7 < sqr(r[s[k]] + r[s[i]])) return true;
	return false;
}

void test()
{
	int i, j;
	for (i = 0; i < n; i++)
	for (j = i + 1; j < n; j++) {
		if (dis(c[i], c[j]) < sqr(r[i] + r[j])) {
			fprintf(stderr, "**");
		}
	}
}

int main()
{
//	freopen("B-small-attempt1.in", "r", stdin);
	int i, j, k;
	scanf("%d", &cs);
	for (ct = 1; ct <= cs; ct++) {
		scanf("%d%lf%lf", &n, &w, &l);
		for (i = 0; i < n; i++)
			scanf("%lf", &r[i]);

		for (i = 0; i <= n; i++)
		for (j = 0; j <= n; j++) {
			a[i][j].x = w * i / n;
			a[i][j].y = l * j / n;
		}

		for (i = 0; i < n; i++)
			s[i] = i;
		bool succ;
		while (true) {
			random_shuffle(s, s + n);
			for (k = 0; k < n; k++) {
				succ = false;
				for (i = 0; i <= n; i++)
				for (j = 0; j <= n; j++)
				if (!conflict(a[i][j], k)) {
					c[s[k]] = a[i][j];
					succ = true;
					j = n + 1;
					i = n + 1;
				}
				if (!succ) break;
			}
			if (succ) {
				printf("Case #%d:", ct);
				for (k = 0; k < n; k++)
					printf(" %.6lf %.6lf", c[k].x, c[k].y);
				printf("\n");
				test();
				break;
			}
		}
	}	
	return 0;
}
