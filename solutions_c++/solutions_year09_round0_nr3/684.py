#include <stdio.h>
#include <string.h>

char a[20] = "welcome to code jam";

int main()
{
	int N;
	char b[1024];
	int table[20][1024];
	scanf("%d", &N);
	gets(b);
	for (int iter = 1; iter <= N; iter++) {
		gets(b);
		for (int i = 0; i<20; i++)
			for (int j = 0; j<1024; j++)
				table[i][j] = 0;
		for (int i = 0; i<1024; i++)
			table[0][i] = 1;
		for (int i = 1; i<=strlen(a); i++)
			for (int j = 1; j<=strlen(b); j++) {
				if (a[i-1] == b[j-1])
					table[i][j] = (table[i-1][j-1] + table[i][j-1])%10000;
				else
					table[i][j] = table[i][j-1];
			}
		printf("Case #%d: %04d\n", iter, table[strlen(a)][strlen(b)]);
	}
	return 0;
}
