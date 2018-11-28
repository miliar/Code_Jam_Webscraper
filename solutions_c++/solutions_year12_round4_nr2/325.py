#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <ctime>
#include <cmath>
#include <stdio.h>
#include <set>
#include <map>
#include <stack>
#include <fstream>
#include <list>

#define SZ(a) (int(a.size()))
#define MEM(a, val) memset(a, val, sizeof(a))

typedef unsigned long long ULL;
typedef long long LL;
typedef long double dbl;

using namespace std;

struct circle {
	int r, num;
	int x, y;
};

circle f[1009];
int n, W, H;

bool comp_r(const circle &a, const circle &b) {
	return a.r > b.r;
}

bool comp_num(const circle &a, const circle &b) {
	return a.num < b.num;
}

inline LL dist(int X1, int Y1, int X2, int Y2) {
	return LL(X1 - X2) * LL(X1 - X2) + LL(Y2 - Y1) * LL(Y2 - Y1);
}

bool check(int X, int Y, int v) {
	for (int i = 0; i < v; ++i) {
		if (dist(X, Y, f[i].x, f[i].y) < LL(f[i].r + f[v].r) * LL(f[i].r + f[v].r)) {
			return false;
		}
	}
	return true;
}

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int I = 1; I <= T; ++I) {
		scanf("%d %d %d" , &n, &W, &H);
		for (int i = 0; i < n; ++i) {
			scanf("%d", &f[i].r);
			f[i].num = i;
		}
		sort(f, f + n, comp_r);
		int X, Y;
		int Yp = -f[0].r;
		int zn = 1;
		for (int i = 0; i < n; ++i) {
			Yp += zn * f[i].r;
			if (Yp < 0) {
				Yp = 0;
				zn *= -1;
			}
			if (Yp > H) {
				Yp = H;
				zn *= -1;
			}

			int r = W;
			int l = -1;
			while (l < r - 1) {
				int mid = (l + r)  / 2;
				if (check(mid, Yp, i)) {
					r = mid;
				}
				else {
					l = mid;
				}
			}
			f[i].x = r;
			f[i].y = Yp;
			Yp += zn * f[i].r;
		}
		sort(f, f + n, comp_num);
		printf("Case #%d:", I);
		for (int i = 0; i < n; ++i) {
			printf(" %d %d", f[i].x, f[i].y);
		}
		printf("\n");
	}
	return 0;
}