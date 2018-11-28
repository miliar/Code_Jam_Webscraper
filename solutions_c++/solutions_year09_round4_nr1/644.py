#include <string>
#include <cstring>
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
#include <fstream>
#include <queue>
#include <cassert>

using namespace std;

#define SIZE(X) (int)X.size()
#define ALL(X) X.begin(), X.end()

inline int nextInt() 
{
	register int ans = 0, sgn = 1;
	register char ch;
	while ((ch = getchar()) < '0') if (ch == '-') sgn = -1;
	do {
		ans *= 10;
		ans += (ch - '0');
	} while ((ch = getchar()) >= '0');
	return sgn * ans;
}
		  
vector < int > a[50];
bool done[50];
int far[50], i, j, k;

char mat[50][50];

int main(void) 
{
	int t;
	t = nextInt();
	for (i = 0; i < 50; ++i) a[i].resize(50);

	for (int tt = 1; tt <= t; ++tt) {
		int n = nextInt();
		int ret = 0;

		for (i = 1; i <= n; ++i) scanf(" %s", mat[i]);

		for (i = 1; i <= n; ++i) {
			far[i] = 1;
			for (j = 1; j <= n; ++j) {
				a[i][j] = mat[i][j - 1] - '0';
				if (a[i][j] == 1) far[i] = j;
			}
		}

		for (i = 1; i <= n; ++i) {
			if (far[i] <= i) continue;
			for (j = i + 1; j <= n; ++j) if (far[j] <= i) {
				for (k = j; k > i; --k) { 
					swap(a[k], a[k - 1]);
					int tmp = far[k];
					far[k] = far[k - 1];
					far[k - 1] = tmp;
					++ret;
				}
				break;
			}
		}

		printf("Case #%d: %d\n", tt, ret);
	}

	return 0;
}