#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

const double pi = 3.1415926535;
const double eps = 1e-6;

struct TP {
	int x, y;
}P[11000];
double k[11000], jie[11000], su[11000];
int W, L, U, G;
double sol(double a, double b, double c)
{
	return (-b + sqrt(b * b + 4 * a * c)) / 2 / a;
}
int main()
{
    freopen ("a.in", "r", stdin);
    freopen ("a.out", "w", stdout);
	int T, ca = 0;
	for (scanf("%d", &T); T; T--) {
		scanf ("%d%d%d%d", &W, &L, &U, &G);
		for (int i = 0; i < L; i++) {
			scanf("%d%d", &P[i].x, &P[i].y);
			if (i) {
				double re = ((double)(P[i].y - P[i - 1].y)) / (P[i].x - P[i - 1].x) / 2.;
				for (int j = P[i - 1].x; j < P[i].x; j++) {
					k[j] = -re;
					jie[j] = -P[i - 1].y + k[j] * (j - P[i - 1].x) * 2.;
				}
			}
		}
		for (int i = 0; i < U; i++) {
			scanf("%d%d", &P[i].x, &P[i].y);
			if (i) {
				double re = ((double)(P[i].y - P[i - 1].y)) / (P[i].x - P[i - 1].x) / 2.;
				for (int j = P[i - 1].x; j < P[i].x; j++) {
					k[j] -= -re;
					jie[j] += P[i - 1].y + re * (j - P[i - 1].x) * 2.;
				}
			}
		}
		su[0] = 0;
		for (int i = 1; i <= W; i++)
			su[i] = su[i - 1] + 1. * k[i - 1] + jie[i - 1];
		int h = 1;
		double del = su[W] / (double)G;
		printf("Case #%d:\n", ++ca);
		for (int i = 1; i < G; i++) {
			while (su[h] + eps < del * i) h++;
			double t = del * i - su[h - 1];
			if (fabs(k[h - 1]) < eps)
				printf ("%.9lf\n", t / jie[h - 1] + h - 1);
			else
				printf ("%.9lf\n", sol(k[h - 1], jie[h - 1], t) + h - 1);
		}
	}
}
