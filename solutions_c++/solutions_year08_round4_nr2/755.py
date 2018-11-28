#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <string>
#include <cctype>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <sstream>
#include <deque>
#include <memory>
using namespace std;
typedef vector<int> vi;
typedef long long li;
typedef pair<int,int> pi;
#define all(c) c.begin(), c.end()
#define fr(i, n) for(i = 0; i < n; ++i)
#define pb push_back
#define mp make_pair
#define INT 2147483647
#define X first
#define Y second
#define sc(a) scanf("%d", &(a))

#define eps 10e-7
bool g(int i, int j, int k, int x, int y, int z) {
	li a, b, c, d;
	a = j - i;
	b = y - x;
	c = k - j;
	d = z - y;
	return a * d == c * b; 
}

double dis(int i, int j, int x, int y) {
	int a = abs(i - j);
	int b = abs(x - y);
	return (double) sqrt((double) a * a + (double) b * b);
}

double calc(int i, int j, int k, int x, int y, int z) {
	double a, b, c;
	a = dis(i, j, x, y);
	b = dis(j, k, y, z);
	c = dis(k, i, z, x);
	if(a + b - eps < c || a + c - eps < b || b + c - eps < a) return -1;
	double p = (a + b + c) / 2.0;
	return sqrt(p * (p - a) * (p - b) * (p - c));
}

int main() {
	freopen("e:\\code\\b\\b-small.in", "r", stdin);
	freopen("e:\\code\\b\\b-small.out", "w", stdout);
	int i, j, k, n, m, t, T, A, x, y, z;
	sc(T);
	double a;
	fr(t, T) {
		int f = 0;
		scanf("%d %d %d", &n, &m, &A);
		a = (double) A / 2.0;
		for (i = 0; i <= 0; ++i) {		
			for (j = 0; j <= n; ++j) {
				for (k = 0; k <= n; ++k) {
					for (x = 0; x <= 0; ++x) {		
						for (y = 0; y <= m; ++y) {
							for (z = 0; z <= m; ++z) {
								if (i == j && x == y) continue;
								if (j == k && y == z) continue;
								if (i == k && x == z) continue;
								if (g(i, j, k, x, y, z)) continue;
								double cur = calc(i, j, k, x, y, z);
								if ((fabs(cur + 1) < eps)) continue;
								if (fabs(cur - a) < eps) {
									f = 1;
									goto RRR;
								}
							}
						}
					}
				}
			}
		}
RRR:
		printf("Case #%d: ", t + 1);
		if (f) {
			printf("%d %d %d %d %d %d\n", i, x, j, y, k, z);
		}
		else printf("IMPOSSIBLE\n");	
	}
	return 0;
}
		
