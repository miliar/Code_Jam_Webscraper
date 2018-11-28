#include <iostream>
using namespace std;


int d[10001];
int l[10001];

int dp[10001];

int main() {
	int cases;
	scanf("%d", &cases);

	for (int k = 0; k < cases; k++) {
		int n;
		int dis;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d%d", &d[i], &l[i]);
			dp[i] = -1;
		}
		scanf("%d", &dis);

		// int cur = d[0] * 2;
		// int next = -1;
		// int nextdis = 0;
					dp[0] = d[0] * 2;


		for (int i = 0; i < n; i++) {


			for (int j = i+1; j < n; j ++) {
				if (d[j] > dp[i]) break;

				int tmp = l[j];
				if (d[j] - l[j] < d[i]) tmp = d[j] + d[j] - d[i];
				else tmp = d[j] + l[j];

				if (tmp > dp[j])
					dp[j] = tmp;
			}
		}

		bool flag = false;
		for (int i = 0; i < n; i++) {
			if (dp[i] >= dis) {
				flag = true;
				break;
			}
 		}

		printf("Case #%d: ", k+1);
		if (flag) printf("YES");
		else printf("NO");

		if (k < cases - 1) printf("\n");
	}
	return 0;
}
