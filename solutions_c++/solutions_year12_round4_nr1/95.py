#include <memory.h>
#include <stdio.h>
using namespace std;

int n;
int D;
int d[10010], l[10010];

int x[10010];

int main()
{
	int i, j;

	int t, tt=0;
	scanf("%d", &t);
	while (t--) {
		scanf("%d", &n);
		for (i=0; i<n; i++) {
			scanf("%d %d", &d[i], &l[i]);
		}
		scanf("%d", &D);

		memset(x, -1, sizeof(x));
		x[0] = d[0];

		bool answer = false;
		for (i=0; i<n; i++) if (x[i]!=-1) {
			if (d[i] + x[i] >= D) {
				answer = true;
				break;
			}

			for (j=i+1; j<n; j++) {
				if (d[j] - d[i] <= x[i]) {
					int t = l[j] >= d[j]-d[i] ? d[j]-d[i] : l[j];
					if (x[j]==-1 || x[j] < t)
						x[j] = t;
				}
			}
		}

		printf("Case #%d: %s\n", ++tt, answer ? "YES" : "NO");
	}

	return 0;
}
