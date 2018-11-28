#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>

#include <cstdio>
#include <cstring>
#include <cassert>
#include <cmath>
#include <ctime>

using namespace std;

typedef long long int64;
typedef long double ldouble;

#define PB(a) push_back(a)
#define MP(a, b) make_pair(a, b)

#define PROBLEM "D"

const int MAXN = 1024;
int a[MAXN];
bool mark[MAXN];

int main() {
	freopen(PROBLEM ".in", "rt", stdin);
	freopen(PROBLEM ".out", "wt", stdout);

	int T;
	scanf("%d\n", &T);

	for (int t = 1; t <= T; t++) {
		printf("Case #%d: ", t);

		memset(mark, 0, sizeof(mark));

		int n;
		scanf("%d", &n);
		int odd = 0;
		for (int i = 1; i <= n; i++) {
			scanf("%d", &a[i]);
			if (a[i] != i) odd++;
		}

		printf("%0.6lf", double(odd));

		printf("\n");
	}

	return 0;
}
