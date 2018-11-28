#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;

int main() {
	int i, j, k;


	freopen("A-large.in", "r", stdin);
	freopen("result2.out", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; ++t) {
		int n, k;
		scanf("%d%d", &n, &k);
		int per = (1<<n) - 1;

		bool ans = false;

		int m = k / (1<<n);

		if (per == k || (m + 1) * (1<<n) - 1 == k) {
			ans = true;
		}


		printf ("Case #%d: ", t);
		printf ("%s\n", ans ? "ON" : "OFF");
	}


	return 0;
}
