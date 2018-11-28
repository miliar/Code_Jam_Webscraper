#include <stdio.h>
#include <string.h>

int main()
{
	int arr[1001];
	int done[1001];
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; ++Case) {
		memset(arr, 0, sizeof(arr));
		memset(done, 0, sizeof(done));
		double R = 0.0;
		int N;
		scanf("%d", &N);
		for (int i = 1; i <= N; ++i) {
			scanf("%d", arr + i);
		}
		for (int i = 1; i <= N; ++i) {
			int len = 0;
			if (done[i])
				continue;
			int next = i;
			while (!done[next]) {
				done[next] = 1;
				++len;
				next = arr[next];
			}
			if (len > 1)
				R += len;
		}
		printf("Case #%d: %f\n", Case, R);
	}
	return 0;
}

