#include <cstdio>
#include <set>
#include <cstring>

int res;
int mass[105];
int n;
int all;

void func(int step, int sum1, int sum2, int sum3) {
	if (step == n) {
		if (sum1 == sum2 && sum3 != all && res < sum3)
			res = sum3;
		return;
	}
	func(step + 1, sum1 ^ mass[step], sum2, sum3 + mass[step]);
	func(step + 1, sum1, sum2 ^ mass[step], sum3);
}

int main() {
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);

	int t;
	
	char str[10];
	scanf("%d", &t);

	for (int i = 0;i < t;++i) {
		res = -1;
		all = 0;
		scanf("%d", &n);
		for (int i = 0;i < n;++i)
			scanf("%d", mass + i), all += mass[i];
		func(0, 0, 0, 0);
		if (res == -1)
			printf("Case #%d: NO\n", i + 1);
		else
			printf("Case #%d: %d\n", i + 1, res);
	}

	return 0;
}