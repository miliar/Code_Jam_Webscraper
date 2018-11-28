#include<stdio.h>
#include<string.h>

int n, nleast, blen, tlimit;
int x[1000];
int v[1000];
bool succeed[1000];

int main()
{
	int i, j, k;
	int t, nowt;
	int succeedcount;
	double needtime;
	int left;
	int swapcount;

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	scanf("%d", &t);
	nowt = 0;
	while (t --) {
		nowt ++;
		scanf("%d%d%d%d", &n, &nleast, &blen, &tlimit);
		for (i = 0; i < n; i ++) {
			scanf("%d", &x[i]);
		}
		for (i = 0; i < n; i ++) {
			scanf("%d", &v[i]);
		}

		succeedcount = 0;
		left = 0;
		for (i = n - 1; i >= 0; i --) {
			if (succeedcount == nleast) 
			{
				left = i + 1;
				break;
			}
			needtime = (double) (blen - x[i]) / v[i];
			if (needtime <= tlimit) {
				succeedcount ++;
				succeed[i] = true;
			}
			else {
				succeed[i] = false;
			}
		}

		if (succeedcount < nleast) {
			printf("Case #%d: IMPOSSIBLE\n", nowt);
		}
		else {
			swapcount = 0;
			for (i = left; i < n; i ++) {
				if (succeed[i] == false) continue;
				for (j = i + 1; j < n; j ++) {
					if (succeed[j] == false) {
						swapcount ++;
					}
				}
			}

			printf("Case #%d: %d\n", nowt, swapcount);
		}
	}

	return 0;
}


