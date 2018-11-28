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

char s[10000];

int main() {
	int T; scanf("%d", &T);
	for (int tt = 0; tt < T; ++tt) {
		scanf("%s", s);
		int n = strlen(s);
		bool f = true;
		for (int i = 1; i < n; ++i) {
			if (s[i] > s[i - 1]) {
				f = false;
				break;
			}
		}
		if (!f) {
			next_permutation(s, s + n);
		} else {
			sort(s, s + n);
			reverse(s, s + n);
			int m = n;
			while (s[m - 1] == '0') {
				--m;
			}
			int k = n - m + 1;
			s[m + k - 1] = s[m - 1];
			for (int i = 0; i < k; ++i) {
				s[m - 1 + i] = '0';
			}
			s[m + k] = 0;
			reverse(s, s + m + k);
		}
		printf("Case #%d: %s\n", tt + 1, s);
	}
	return 0;
}
