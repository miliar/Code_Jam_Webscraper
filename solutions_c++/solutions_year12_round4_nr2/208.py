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

int testq;
int test;

#define MAX 1100

int n, m, k;

double r[MAX];
double x[MAX], y[MAX];

void Read() {
	int i;
	scanf("%d %d %d", &k, &n, &m);
	fi(1, k) {
		scanf("%lf", &r[i]);
	}
}

bool Field(double x, double y) {
	if (x < 0 || x > n) return false;
	if (y < 0 || y > m) return false;
	return true;
}

double eps = 1e-8;

double sqr(double x) {
	return x * x;
}

double Dist(double x1, double y1, double x2, double y2) {
	return sqrt(sqr(x2 - x1) + sqr(y2 - y1));
}

void Solve() {
	int i, j;
	double vx, vy;
	double l;
	double g;
	int flag;
	fi(1, k) {
		x[i] = ((double)rand() / (double)RAND_MAX) * n;
		y[i] = ((double)rand() / (double)RAND_MAX) * m;
	}
	flag = 1;
	while (flag) {
		flag = 0;
		fi(1, k) {
			fj(i + 1, k) {
				if (Dist(x[i], y[i], x[j], y[j]) < r[i] + r[j] + eps) {
					flag = 1;
					vx = x[j] - x[i];		
					vy = y[j] - y[i];
					l = Dist(0, 0, vx, vy);
					vx /= l;
					vy /= l;

					g = (r[i] + r[j] - Dist(x[i], y[i], x[j], y[j]) + 2 * eps) / 2;

					x[i] -= vx * g;
					y[i] -= vy * g;

					x[j] += vx * g;
					y[j] += vy * g;

					if (!Field(x[i], y[i])) {
						x[i] = ((double)rand() / (double)RAND_MAX) * n;
						y[i] = ((double)rand() / (double)RAND_MAX) * m;
					}
					if (!Field(x[j], y[j])) {
						x[j] = ((double)rand() / (double)RAND_MAX) * n;
						y[j] = ((double)rand() / (double)RAND_MAX) * m;
					}
				}
			}
		}
	}
	fi(1, k) {
		printf("%.9lf %.9lf%c", x[i], y[i], " \n"[i == k]);
	}	
}

void Test() {
	int i;
	printf("1\n");
	printf("1000 125 125\n");
	fi(1, 1000) {
		printf("1 ");
	}
	printf("\n");
	exit(0);
}

int main(int argc, char **argv) {
	if (argc == 1) {
		freopen("input.txt","r",stdin);
	} else {
		freopen(argv[1], "r",stdin);
	}
	freopen("output.txt","w",stdout);

	//Test();
	scanf("%d", &testq);
	for (test = 1; test <= testq; test++) {
		Read();
		printf("Case #%d: ", test);
		Solve();
		fflush(stdout);
	}
	return 0;
}