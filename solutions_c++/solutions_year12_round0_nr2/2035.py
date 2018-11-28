#define _CRT_SECURE_NO_WARNINGS

#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
#include <numeric>

using namespace std;

#define INF (2000000000)

const int nmax = 1 << 7;
const int w = 10;

int mx[nmax];
int amx[nmax];

void init() {


	memset(mx, 0, sizeof(mx));
	memset(amx, -1, sizeof(amx));

	for(int i = 0; i <= w; ++i) {
		for(int j = 0; j <= w; ++j) {
			for(int k = 0; k <= w; ++k) {

				if (abs(i - j) > 2 ||
					abs(k - j) > 2 ||
					abs(i - k) > 2) {
					continue;
				}

				int s = i + j + k;
				int t = max(i, max(j, k));

				if (abs(i - j) == 2 ||
					abs(k - j) == 2 ||
					abs(i - k) == 2) {
					amx[s] = max(amx[s], t);
				} else {
					mx[s] = max(mx[s], t);
				}
			}
		}
	}


}

int a[nmax];
int n, s, p;

void solveTest() {
	scanf("%d%d%d", &n, &s, &p);

	for(int i = 0; i < n; ++i) {
		scanf("%d", &a[i]);
	}

	int ans = 0;

	for(int i = 0; i < n; ++i) {

		if (mx[a[i]] >= p) {
			++ans;
		} else {
			if (amx[a[i]] >= p && s) {
				++ans;
				--s;
			}
		}
	}

	printf("%d", ans);
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("B.in", "rt", stdin);
	freopen("B.out", "wt", stdout);
#endif
	init();
	int t;
	scanf("%d", &t);
	for(int tt = 0; tt < t; ++tt)
	{
		printf("Case #%d: ", tt + 1);

		solveTest();

		puts("");
	}
	return 0;
}