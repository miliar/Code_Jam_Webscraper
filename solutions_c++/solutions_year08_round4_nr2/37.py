#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <sstream>
#include <iostream>
#include <queue>
#include <set>
#include <map>

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define LD long double
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define DFOR(a,b) for(int a=b-1;a>=0;a--)
#define CLR(a,b) memset(a,b,sizeof(a))


using namespace std;

int n, m, a;

bool tryit(int x, int &p, int &q) {
	if (x == 0) {
		p = q = 0;
		return true;
	}
	for (int i = 1; i <= n && i <= x; i++) if (x % i == 0) {
		int j = x / i;
		if (j <= m) {
			p = i;
			q = j;
			return true;
		}
	}
	return false;
}

void solvecase() {
	scanf("%d%d%d", &n, &m, &a);
	for (int t = a; t <= n * m; t++) {
		int x1, y1, x2, y2;
		if (tryit(t-a, x1, y2) && tryit(t, x2, y1)) {
			printf("0 0 %d %d %d %d", x1, y1, x2, y2);
			return;
		}
	}
	printf("IMPOSSIBLE");


/*
	for (int x1 = 0; x1 <= n; x1++)
		for (int x2 = 0; x2 <= n; x2++) {
			for (int y1 = 0; y1 <= m; y1++) {
				int t = a + x2 * y1;
				if (x1 == 0) {
					if (t == 0) {
						int y2 = 0;
						printf("0 0 %d %d %d %d", x1, y1, x2, y2);
						return;
					}
				} else {
					if (t % x1 == 0) {
						int y2 = t / x1;
						if (y2 >= 0 && y2 <= m) {
							printf("0 0 %d %d %d %d", x1, y1, x2, y2);
							return;
						}
					}
				}
			}
		}
	printf("IMPOSSIBLE");	
	*/
}

void solve() {
	int n;
	scanf("%d\n", &n);
	FOR(i, n) {
		printf("Case #%d: ", i+1);
		solvecase();
		printf("\n");
	}
}

int main() {
	freopen("y", "rt", stdin);
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}