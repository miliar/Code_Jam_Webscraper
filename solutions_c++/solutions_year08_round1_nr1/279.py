#include <cstdio>
#include <algorithm>
#include <functional>

using namespace std;

long long arr[1024];
long long arr2[1024];

long long run()
{
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		scanf("%lld", arr + i);
	}
	for (int i = 0; i < n; ++i) {
		scanf("%lld", arr2 + i);
	}
	sort(arr, arr + n);
	sort(arr2, arr2 + n, greater<long long>());
	long long sum = 0;
	for (int i = 0; i < n; ++i) {
		sum += arr[i] * arr2[i];
	}
	return sum;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: %lld\n", i, run());
	}
	return 0;
}