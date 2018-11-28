#include <stdio.h>
#include <stdlib.h>
#include <string.h>
const int MAXN = 800;
int a[MAXN], b[MAXN];
int n;
int compare(const void *a, const void *b)
{
	int c = abs(*(int *)a), d = abs(*(int *)b);
	return c - d;
}
int main()
{
	int t;
	scanf("%d", &t);
	for (int cases = 1; cases <= t; cases++)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%d", &a[i]);
		for (int i = 0; i < n; i++)
			scanf("%d", &b[i]);
		qsort(a, n, sizeof(int), compare);
		qsort(b, n, sizeof(int), compare);
		bool flag = false;
		int sum = 0;
		for (int i = n - 1; i >= 0; i--) {
			if (a[i] * b[i] < 0) {
				
				sum += a[i] * b[i];
//				printf("%d %d %d\n", a[i], b[i], sum);
			} else {
				if (abs(a[i]) < abs(b[i])) {
					bool found = false;
					for (int j = i - 1; j >= 0; j--)
					{
						if (a[j] * b[i] < 0) {
							int t = a[j];
							for (int k = j + 1; k <= i; k++)
								a[k - 1] = a[k];
							a[i] = t;
							found = true;
							break;
						}
					}
					if (!found) {
						int t = a[0];
						for (int k = 1; k <= i; k++)
							a[k - 1] = a[k];
						a[i] = t;
					}
					sum += a[i] * b[i];
					//printf("%d %d %d\n", a[i], b[i], sum);
				} else {
					bool found = false;
					for (int j = i - 1; j >= 0; j--)
					{
						if (a[i] * b[j] < 0) {
							int t = b[j];
							for (int k = j + 1; k <= i; k++)
								b[k - 1] = b[k];
							b[i] = t;
							found = true;
							break;
						}
					}
					if (!found) {
						int t = b[0];
						for (int k = 1; k <= i; k++)
							b[k - 1] = b[k];
						b[i] = t;
					}
					sum += a[i] * b[i];
					//printf("%d %d %d\n", a[i], b[i], sum);
				}	
			}
		}
		printf("Case #%d: %d\n", cases, sum);
	}
}
