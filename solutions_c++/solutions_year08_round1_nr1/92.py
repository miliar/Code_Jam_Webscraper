#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

int a[1000];
int b[1000];
int n;

int main()
{
	int i, j, k;
	int t;
	int nowt;
	__int64 sum;

	freopen("A-large.in.txt", "r", stdin);
	freopen("A-large.out.txt", "w", stdout);

	scanf("%d", &t);
	nowt = 0;
	while (t--) {
		nowt ++;
		scanf("%d", &n);
		for (i = 0; i < n; i ++) {
			scanf("%d", &a[i]);
		}
		for (i = 0; i < n; i ++) {
			scanf("%d", &b[i]);
		}

		sort(a, a+n);
		sort(b, b+n);

		sum = 0;
		for (i = 0; i < n; i ++) {
			sum += (__int64)a[i] * b[n-1-i];
		}

		printf("Case #%d: %I64d\n", nowt, sum);
	}

	return 0;
}