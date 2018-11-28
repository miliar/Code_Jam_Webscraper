#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

const int MAXN = 512;
const int MODULO = 100003;

int table[MAXN][MAXN];

// http://www.research.att.com/~njas/sequences/A007059
int f(int n, int m) {
	if (n > 0) {
		if (table[n][m] == -1) {
			table[n][m] = 0;
			for (int i = 1; i <= m; i++) {
				table[n][m] += f(n - i, m);
				if (table[n][m] > MODULO) {
					table[n][m] -= MODULO;
				}
			}
		}
		return table[n][m];
	} else if (n == 0) {
		return 1;
	} else {
		return 0;
	}
}

int main() {
	memset(table, 0xff, sizeof(table));
	int caseNum;
	scanf("%d", &caseNum);
	for (int caseIndex = 1; caseIndex <= caseNum; caseIndex++) {
		int n;
		scanf("%d", &n);
		int ans = 0;
		n--;
		for (int i = 0; i <= n; i++) {
			ans += f(i, n - i);
			if (ans > MODULO) {
				ans -= MODULO;
			}
		}
		printf("Case #%d: %d\n", caseIndex, ans);

	}
	return 0;
}
