#include <string>
#include <vector>
#include <climits>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <list>
#include <stack>
#include <deque>
#include <iostream>
#include <cstdio>

using namespace std;

const int MAX = 1001;

int get_res(int * ti, int n, int s, int p) {
	int res = 0;
	for (int i = 0; i < n; ++i) {
		if (ti[i] / 3 >= p) {
			res++;
		} else if ((ti[i] % 3 != 0) && (ti[i] / 3) + 1 >= p) {
			res++;
		} else if (s > 0) {
			if (ti[i] >= 2 && ti[i] <= 28) {
				if ((ti[i] % 3 == 0) && (ti[i] / 3 + 1 <= 10) && ((ti[i] / 3) - 1 >= 0)
						&& ((ti[i] / 3) + 1 >= p)) {
					res++;
					s--;
				} else if ((ti[i] % 3 == 2) && (ti[i] / 3 + 2 <= 10) && ((ti[i] / 3 + 2) >= p)) {
					res++;
					s--;
				}
			}
		}
	}
	return res;
}

void run(int * ti, int c) {
	int n, s, p;
	scanf("%d%d%d", &n, &s, &p);
	for (int i = 0; i < n; ++i) {
		int x;
		scanf("%d", &x);
		ti[i] = x;
	}
	printf("Case #%d: ", c);
	printf("%d\n", get_res(ti, n, s, p));
}

int main() {
	int z;
	scanf("%d", &z);
	int ti[MAX];
	for (int i = 0; i < z; ++i) {
		run(ti, i + 1);
	}
}
