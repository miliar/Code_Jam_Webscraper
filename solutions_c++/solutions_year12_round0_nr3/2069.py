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

const int nmax = 1 << 21;

int c[nmax][12];

int dcnt(int x) {

	int ans = 0;

	while(x) {
		++ans;
		x /= 10;
	}

	return ans;

}

int p10(int d) {

	int ans = 1;

	for(int i = 0; i < d; ++i) {
		ans *= 10;
	}

	return ans;

}

void init() {

	memset(c, 0, sizeof(c));

	for(int i = 1; i < nmax; ++i) {

		int q = i;
		int t = i;

		int d = dcnt(i);
		int p = p10(d - 1);

		int n = 0;

		do{

			int x = t / 10;
			int y = t % 10;

			t = y * p + x;

			if (y != 0 && t < q) {
				++n;
				c[i][n] = t;
			}

		}while(t != q);

		c[i][0] = n;
	}

}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("C.in", "rt", stdin);
	freopen("C.out", "wt", stdout);
#endif

	init();

	int t;
	scanf("%d", &t);
	for(int tt = 0; tt < t; ++tt)
	{
		printf("Case #%d: ", tt + 1);
		cerr << "Case #" << tt + 1 << endl;
		
		int a, b;

		scanf("%d%d", &a, &b);

		int ans = 0;

		for(int i = a + 1; i <= b; ++i) {

			for(int j = 1; j <= c[i][0]; ++j) {

				if (c[i][j] >= a) {
					++ans;
				}
			}

		}

		printf("%d", ans);

		puts("");
	}
	return 0;
}