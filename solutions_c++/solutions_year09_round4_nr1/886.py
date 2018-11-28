#include <stdio.h>

#define MAX 999

int main()
{
	int T, iter, N, ans;
	int arr[100];
	char line[100];
	scanf("%d", &T);
	for (iter = 1; iter <= T; iter ++) {
		scanf("%d", &N);
		ans = 0;
		for (int i = 0; i<N; i++) {
			scanf("%s", line);
			for (arr[i] = N-1; arr[i]>=0 && line[arr[i]] == '0'; arr[i]--);
		}

		for (int i = 0; i<N; i++) {
			int j;
			for (j = i; j<N; j++)
				if (arr[j] <= i)	break;
			int itmp;
			for (; j>i; j--) {
				itmp = arr[j];
				arr[j] = arr[j-1];
				arr[j-1] = itmp;
				ans++;
			}
		}

		printf("Case #%d: %d\n", iter, ans);
	}
	return 0;
}
