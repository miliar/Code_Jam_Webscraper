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

char s[1000];
int a[1000];

int main() {
	int T; scanf("%d", &T);
	for (int tt = 0; tt < T; ++tt) {
		int result = 0;
		int n; scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%s", s);
			a[i] = -1;
			for (int j = 0; j < n; ++j) {
				if (s[j] == '1') a[i] = j;
			}
		}
		for (int i = 0; i < n; ++i) {
			for (int j = i; j < n; ++j) {
				if (a[j] <= i) {
					int k = j;
					while (k > i) {
						swap(a[k], a[k - 1]);
						--k;
						++result;
					}
					break;
				}
			}
		}
		printf("Case #%d: %d\n", tt + 1, result);
	}
	return 0;
}
