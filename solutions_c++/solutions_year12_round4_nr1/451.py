#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
using namespace std;

int x[100005], len[100005];
int myLen[100005];
bool f[100005];
int n, dist;

bool canReach (int ind1, int ind2) {
	return x[ind1] + myLen[ind1] >= x[ind2];
}

void solve () {
	int i, j;
	int newMyLen;

	scanf("%d", &n);
	
	for (i = 0;i < n;i++) {
		scanf("%d%d", &x[i], &len[i]);
	}

	for (i = 0;i < n;i++) {
		f[i] = false;
		myLen[i] = 0;
	}

	scanf("%d", &dist);

	f[0] = true;
	myLen[0] = x[0];

	for (i = 0;i < n;i++) {
		if (!f[i])
			continue;

		for (j = i + 1;j < n;j++) {
			if (!canReach(i, j))
				continue ;

			f[j] = true;

			newMyLen = min(x[j] - x[i], len[j]);
			myLen[j] = max(newMyLen, myLen[j]);
		}
	}

	for (i = 0;i < n;i++) {
		if (f[i]) {
			if (x[i] + myLen[i] >= dist) {
				printf("YES");
				return ;
			}
		}
	}

	printf("NO");
}

int main () {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int test, t;

	scanf("%d\n", &test);
	for (t = 0;t < test;t++) {
		if (t)
			printf("\n");
		printf("Case #%d: ", t + 1);
		solve();
	}
	return 0;
}