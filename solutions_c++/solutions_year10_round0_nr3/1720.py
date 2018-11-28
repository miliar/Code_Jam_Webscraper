#include <cstdio>

int arr[1000][2];
long long int money[1000];
int main(void) {
	int t, r, k, n;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		scanf("%d %d %d", &r, &k, &n);
		for (int j = 0; j < n; ++j)
			scanf("%d", &arr[j][0]), money[j] = 0;
		int ind = 0;
		while (money[0]+arr[ind][0] <= k) {
			money[0] += arr[ind++][0];
			if (ind >= n) ind -= n;
			if (ind == 0) break;
		}
		arr[0][1] = ind;
		for (int j = 1; j < n; ++j) {
			money[j] = money[j-1]-arr[j-1][0];
			ind = arr[j-1][1];
			while (money[j]+arr[ind][0] <= k) {
				money[j] += arr[ind++][0];
				if (ind >= n) ind -= n;
				if (ind == j) break;
			}
			arr[j][1] = ind;
		}
		long long int price = 0;
		ind = 0;
		for (int j = 0; j < r; ++j) {
			price += money[ind];
			ind = arr[ind][1];
		}
		printf("Case #%d: %lld\n", i, price);
	}
	return 0;
}