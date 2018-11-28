#define _CRT_SECURE_NO_DEPRECATE

#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>

using namespace std;

#define pb push_back
#define pf push_front
#define mp make_pair
#define fi(a, b) for(i=a; i<=b; i++)
#define fj(a, b) for(j=a; j<=b; j++)
#define fo(a, b) for(o=a; o<=b; o++)
#define fdi(a, b) for(i=a; i>=b; i--)
#define fdj(a, b) for(j=a; j>=b; j--)
#define fdo(a, b) for(o=a; o>=b; o--)
#define ZERO(x) memset(x, 0, sizeof(x))
#define COPY(x,y) memcpy(x, y, sizeof(y))
#define LEN(x) (int)x.length()
#define SIZE(x) (int)x.size()

typedef long long int64;

#define MAX 600

int testq;
int test;

int n, m, d;

double matr[MAX][MAX];
char str[MAX];

void Read() {
	int i, j;
	scanf("%d %d %d", &m, &n, &d);

	d = 0;

	ZERO(matr);
	fj(1, m) {
		scanf("%s", str + 1);
		fi(1, n) {
			matr[j][i] = d + str[i] - '0';
		}
	}
}

int ans;

double eps = 1e-8;

bool Eq(double x, double y) {
	return fabs(x - y) < eps;
}

double sum[MAX][MAX];
double sumx[MAX][MAX];
double sumy[MAX][MAX];

void Init() {
	int i, j;
	ZERO(sum);
	ZERO(sumx);
	ZERO(sumy);
	fj(1, m) {
		fi(1, n) {
			sum[j][i] = sum[j][i - 1] + sum[j - 1][i] - sum[j - 1][i - 1] + matr[j][i];
		}
	}

	fj(1, m) {
		fi(1, n) {
			sumx[j][i] = sumx[j][i - 1] + sumx[j - 1][i] - sumx[j - 1][i - 1] + i * matr[j][i];
		}
	}

	fj(1, m) {
		fi(1, n) {
			sumy[j][i] = sumy[j][i - 1] + sumy[j - 1][i] - sumy[j - 1][i - 1] + j * matr[j][i];
		}
	}
}

double Sum(int x1, int y1, int x2, int y2) {
	return sum[y2][x2] - sum[y1 - 1][x2] - sum[y2][x1 - 1] + sum[y1 - 1][x1 - 1];
}

double SumX(int x1, int y1, int x2, int y2) {
	return sumx[y2][x2] - sumx[y1 - 1][x2] - sumx[y2][x1 - 1] + sumx[y1 - 1][x1 - 1];
}

double SumY(int x1, int y1, int x2, int y2) {
	return sumy[y2][x2] - sumy[y1 - 1][x2] - sumy[y2][x1 - 1] + sumy[y1 - 1][x1 - 1];
}

void Try(int x, int y, int s) {
	int x1, y1, x2, y2;
	int i, j;
	double cx, cy;
	double mx, my;
	x1 = x;
	y1 = y;

	x2 = x + s - 1;
	y2 = y + s - 1;

	if (x1 < 1 || x2 > n) return;
	if (y1 < 1 || y2 > m) return;

	cx = (x + s / 2. - 0.5);
	cy = (y + s / 2. - 0.5);

	mx = 0;
	my = 0;

	/*fi(x1, x2) {
		mx += i * Sum(i, y1, i, y2);
	}

	fj(y1, y2) {
		my += j * Sum(x1, j, x2, j);	
	}*/

	mx += SumX(x1, y1, x2, y2);
	my += SumY(x1, y1, x2, y2);

	mx += -cx * Sum(x1, y1, x2, y2);
	my += -cy * Sum(x1, y1, x2, y2);

	i = x1;
	j = y1;
	mx -= (i - cx) * matr[j][i];
	my -= (j - cy) * matr[j][i];

	i = x2;
	j = y1;
	mx -= (i - cx) * matr[j][i];
	my -= (j - cy) * matr[j][i];

	i = x1;
	j = y2;
	mx -= (i - cx) * matr[j][i];
	my -= (j - cy) * matr[j][i];

	i = x2;
	j = y2;
	mx -= (i - cx) * matr[j][i];
	my -= (j - cy) * matr[j][i];

	if (Eq(mx, 0) && Eq(my, 0)) {
		ans = max(ans, s);
	}
}

void Solve() {
	int i, j, o;
	ans = -1;

	Init();

	fdo(min(n, m), 3) {
		fj(1, m) {
			fi(1, n) {
				Try(i, j, o);
				if (ans != -1) break;
			}
			if (ans != -1) break;
		}
		if (ans != -1) break;
	}

	if (ans == -1) {
		printf("IMPOSSIBLE\n");
	} else {
		printf("%d\n", ans);
	}
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d", &testq);
	for (test = 1; test <= testq; test++) {
		Read();
		printf("Case #%d: ", test);
		Solve();
		fflush(stdout);
	}
	return 0;
}