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

char word[6000][20];
char s[10000];
int u[6000];

int main() {
	int l, d, n;
	scanf("%d %d %d", &l, &d, &n);
	for (int i = 0; i < d; ++i) {
		scanf("%s", word[i]);
	}
	int tt = 0;
	for (int i = 0; i < n; ++i) {
		++tt;
		scanf("%s", s);
		for (int j = 0; j < d; ++j) {
			u[j] = tt;
		}
		for (int j = 0, t = 0; j < l; ++j, ++t) {
			int x = 0;
			if (isalpha(s[t])) x = 1 << (s[t] - 'a');
			else {
				++t;
				while (s[t] != ')') {
					x |= 1 << (s[t] - 'a');
					++t;
				}
			}
			for (int k = 0; k < d; ++k) if (u[k] == tt) {
				if (!(x & (1 << (word[k][j] - 'a')))) {
					u[k] = -1;
				}
			}
		}
		int result = 0;
		for (int j = 0; j < d; ++j) if (u[j] == tt) {
			++result;
		}
		printf("Case #%d: %d\n", tt, result);
	}
	return 0;
}
