#include<stdio.h>
#include<string.h>

int nrs, test, n, i, j, d[505][22];
char sir[505], caut[21] = {"awelcome to code jam"};

int main()
{
	freopen("ab.in", "rt", stdin);
	freopen("ab.out", "wt", stdout);

	//for (i = 1; i <= 18; i ++)
	//	printf("%c", caut[i]);

	scanf("%d\n", &nrs);
	for (test = 1; test <= nrs; test ++){
		fgets(sir + 1, 505, stdin);
		n = strlen(sir + 1);
		memset(d, 0, sizeof(d));

		for (i = 1; i <= n; i ++){
			d[i-1][0] = 1;
			for (j = 1; j <= 19; j ++){
				d[i][j] = d[i-1][j];

				if (sir[i] == caut[j])
					d[i][j] = (d[i][j] + d[i-1][j-1]) % 10000;
			}
		}

		printf("Case #%d: ", test);
		if (d[n][19] >= 1000)
			printf("%d\n", d[n][19]);
		else
			if (d[n][19] >= 100)
				printf("0%d\n", d[n][19]);
			else
				if (d[n][19] >= 10)
					printf("00%d\n", d[n][19]);
				else
					printf("000%d\n", d[n][19]);
	}

	return 0;
}

