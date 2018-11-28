#include <cstdio>
#include <cstring>

using namespace std;

int t, n, k;
int arr[100];
int index, sum;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);

	scanf("%d", &t);
	for(int i = 0; i < t; ++i) {
		scanf("%d %d", &n, &k);

		memset(arr, 0, sizeof(arr));

		index = 0;
		while(k > 0) {
			arr[index++] = k % 2;
			k /= 2;
		}

		sum = 0;
		for(int j = 0; j < n; ++j)
			sum += arr[j];

		printf("Case #%d: %s\n", i + 1, (sum != n ? "OFF" : "ON"));
	}

	return 0;
}