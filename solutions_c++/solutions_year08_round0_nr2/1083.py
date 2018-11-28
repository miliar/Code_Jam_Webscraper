#include <cstdio>
#include <algorithm>

using namespace std;

void run(int ind)
{
	int t;
	scanf("%d", &t);
	int a, b;
	scanf("%d %d", &a, &b);
	int arr[4][128];
	for (int i = 0; i < a; ++i) {
		int t1, t2;
		scanf("%d:%d", &t1, &t2);
		arr[0][i] = t1 * 60 + t2;
		scanf("%d:%d", &t1, &t2);
		arr[1][i] = t1 * 60 + t2;
	}
	for (int i = 0; i < b; ++i) {
		int t1, t2;
		scanf("%d:%d", &t1, &t2);
		arr[2][i] = t1 * 60 + t2;
		scanf("%d:%d", &t1, &t2);
		arr[3][i] = t1 * 60 + t2;
	}
	sort(arr[0], arr[0] + a);
	sort(arr[1], arr[1] + a);
	sort(arr[2], arr[2] + b);
	sort(arr[3], arr[3] + b);
	int sum1 = a, sum2 = b;
	for (int i = 0, j = 0; i < a && j < b; ++i) {
		while (j < b && arr[2][j] < arr[1][i] + t) {
			++j;
		}
		if (j != b) {
			--sum2;
			++j;
		}
	}
	for (int i = 0, j = 0; i < a && j < b; ++j) {
		while (i < a && arr[0][i] < arr[3][j] + t) {
			++i;
		}
		if (i != a) {
			--sum1;
			++i;
		}
	}
	printf("Case #%d: %d %d\n", ind, sum1, sum2);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		run(i);
	}
	return 0;
}