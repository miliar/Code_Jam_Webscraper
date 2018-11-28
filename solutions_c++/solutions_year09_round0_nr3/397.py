#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cctype>
#include <cmath>

#include <iostream>
#include <sstream>
#include <string>
#include <iomanip>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

#define pb push_back
#define mp make_pair

#define min(x, y) ((x) < (y) ? (x) : (y))
#define max(x, y) ((x) > (y) ? (x) : (y))
#define abs(x) ((x) < 0 ? (-(x)) : (x))

typedef double dbl;
typedef long double ldbl;
typedef long long i64;

int d[2][1000];
char s[10000];
char t[] = "welcome to code jam";

int main() {
	int T; scanf("%d\n", &T);
	int m = strlen(t);
	for (int tt = 0; tt < T; ++tt) {
		gets(s);
		int n = strlen(s);
		for (int i = 0; i <= m; ++i) {
			d[0][i] = 0;
		}
		d[0][0] = 1;
		for (int i = 1; i <= n; ++i) {
			for (int j = 0; j <= m; ++j) {
				d[i & 1][j] = d[(i - 1) & 1][j];
			}
			for (int j = 1; j <= m; ++j) {
				if (s[i - 1] == t[j - 1]) {
					d[i & 1][j] += d[(i - 1) & 1][j - 1];
					d[i & 1][j] %= 10000;
				}
			}
		}
		printf("Case #%d: %04d\n", tt + 1, d[n & 1][m]);
	}
	return 0;
}
