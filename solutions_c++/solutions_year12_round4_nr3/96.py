#include <memory.h>
#include <stdio.h>

int n;
int x[2010];

int h[2010];

int getheight(int x1, int h1, int x2, int h2, int x)
{
	long long h = h1 + ((long long)(h2-h1) * (x-x1) + x2-x1-1) / (x2-x1);
	return h;
}

int main()
{
	int i, j;

	int t, tt=0;
	scanf("%d", &t);
	while (t--) {
		scanf("%d", &n);
		for (i=0; i<n-1; i++) {
			scanf("%d", &x[i]); x[i]--;
		}

		bool flag = true;

		memset(h, -1, sizeof(h));
		h[0] = h[n-1] = 1e9;
		for (i=0; i<n-1; i++) {
			if (h[i]==-1) h[i] = h[i-1] / 2;
			for (j=i+1; j<n; j++) {
				if (h[j]!=-1) break;
			}

			if (x[i] > j) {
				flag = false;
				break;
			}
			if (x[i] < j) h[x[i]] = getheight(i, h[i], j, h[j], x[i]);
		}

		printf("Case #%d: ", ++tt);
		if (!flag) printf("Impossible\n");
		else {
			for (j=0; j<n; j++) printf("%d ", h[j]);
			printf("\n");
		}
	}

	return 0;
}
