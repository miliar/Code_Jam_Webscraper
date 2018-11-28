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


const int nmax = 1 << 16;

int l[nmax];
int d[nmax];
int a[nmax];
int n, D;

void readTest() {
	scanf("%d", &n);
	for(int i = 0; i < n; ++i) {
		scanf("%d%d", &d[i], &l[i]);
	}
	scanf("%d", &D);
}

void solveTest() {

	memset(a, 0, sizeof(a));


	a[0] = d[0];
	for(int i = 0; i < n; ++i) {

		for(int j = i + 1; j < n; ++j) {

			int diff = d[j] - d[i];

			if (diff <= a[i]) {
				a[j] = max(a[j], min(diff, l[j]));
			} else {
				break;
			}

		}
	}

	for(int i = 0; i < n; ++i) {
		if (a[i] + d[i] >= D) {
			puts("YES");
			return;
		}
	}

	puts("NO");

}

int main()
{
	freopen("A.in", "rt", stdin);

	bool submit = true;

	if (submit) {
		freopen("AL.out", "wt", stdout);
	}

	int t;
	scanf("%d", &t);
	for(int tt = 0; tt < t; ++tt) {
		readTest();
		printf("Case #%d: ", tt + 1);
		solveTest();
		if (submit) {
			cerr << "Case " << tt + 1 << " done\n";
		}
	}
	return 0;
}