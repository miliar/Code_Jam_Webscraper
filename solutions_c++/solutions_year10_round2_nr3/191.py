#include<stdio.h>
#include<math.h>

__int64 c[1000][1000];
int maxn = 505;
__int64 pure[1000][1000];
__int64 pbase = 100003;

void init()
{
	int i, j, k;

	for (i = 0; i < maxn; i ++) {
		c[i][0] = c[i][i] = 1;
		for (j = 1; j < i; j ++) {
			c[i][j] = (c[i-1][j-1] + c[i-1][j])%pbase;
		}
	}

	pure[2][1] = 1;
	for (i = 3; i < maxn; i ++) {
		pure[i][1] = 1;
		for (j = 2; j < i; j ++) {
			pure[i][j] = 0;
			for (k = 1; k < j; k ++) {
				pure[i][j] += (pure[j][k] * c[i - j - 1][j - k - 1])%pbase;
				pure[i][j] %= pbase;
			}
		}
	}
}


int main()
{
	int i, j, k;
	int t, nowt;
	int n;
	__int64 count;

	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	init();
	scanf("%d", &t);
	nowt = 0;
	while (t --) {
		nowt ++;
		scanf("%d", &n);

		count = 0;
		for (i = 1; i < n; i ++) {
			count += pure[n][i];
			count %= pbase;
		}

		printf("Case #%d: %I64d\n", nowt, count);
	}

	return 0;
}



	