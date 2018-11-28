#include <math.h>
#include <stdio.h>

const double EPS = 1E-7;

typedef struct tagPoint {
	int x;
	int y;
	
} Point;

int N = 0;
int M = 0;
int A = 0;
bool flag = false;
Point p[3];

int gcd(int a, int b) {
	return (0 == b) ? a : gcd(b, a % b);
}

int nok(int a, int b) {
	return a / gcd(a, b) * b;
}

double square(Point A, Point B, Point C) {
	int x1 = B.x - A.x;
	int y1 = B.y - A.y;
	int x2 = C.x - A.x;
	int y2 = C.y - A.y;

	return (double)abs(x1 * y2 - x2 * y1) / 2.;
}

bool eq(double a, double b) {
	return fabs(a - b) <= EPS;
}

bool check() {
	return eq((double)A / 2., square(p[0], p[1], p[2]));
}

void print() {
	printf("%d %d %d %d %d %d\n", p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y);
}

void find(int k) {
	if (flag) {return;}
	if (2 == k) {
		if (flag = check()) {
			print();
		}
		return;
	}

	for (int i = 0; i <= N; ++i) {
		for (int j = 0; j <= M; ++j) {
			p[k].x = i;
			p[k].y = j;
			find(k + 1);
		}
	}
}

void solve(void) {
	/*p[0].x = 1;	p[0].y = 1;
	p[1].x = 4;	p[1].y = 1;
	p[2].x = 1;	p[2].y = 4;
	printf("--%.2lf\n", square(p[0], p[1], p[2]));*/
	scanf("%d %d %d", &N, &M, &A);
	flag = false;
	find(0);
	if (!flag) {puts("IMPOSSIBLE");}
}

int main(void) {
	freopen("b.in", "rt", stdin);
	freopen("b.out", "wt", stdout);

	int T = 0;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
	}

	return 0;
}
