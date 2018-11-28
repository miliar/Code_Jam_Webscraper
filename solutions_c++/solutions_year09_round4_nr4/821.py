#define _CRT_SECURE_NO_WARNINGS

#include <math.h>
#include <stdio.h>
#include <minmax.h>

const int MAXN = 50;

typedef struct circleTag {
	int x;
	int y;
	int r;
} circle;

int N = 0;
circle c[MAXN];

void init(void) {
}

void read(void) {
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		scanf("%d %d %d", &c[i].x, &c[i].y, &c[i].r);
	}
}

double dist(int i, int j) {
	return (sqrt((double)(c[i].x - c[j].x)*(c[i].x - c[j].x) + (c[i].y - c[j].y)*(c[i].y - c[j].y)) + c[i].r + c[j].r) / 2;
}

double solve(void) {
	if (1 == N) {return c[0].r;}
	if (2 == N) {return max(c[0].r, c[1].r);}
	double res = max(c[0].r, dist(1, 2));
	res = min(res, max(c[2].r, dist(0, 1)));
	res = min(res, max(c[1].r, dist(0, 2)));
	return res;
}

int main(void) {
	freopen("d.in", "rt", stdin);
	freopen("d.out", "wt", stdout);

	int T = 0;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		printf("Case #%d: ", i + 1);
		init();
		read();
		printf("%.7lf\n", solve());
	}

	return 0;
}
