#include <stdio.h>
#include <string.h>

#define MOD 10000

int N, M[512][32];
char s[512];
char W[32] = "welcome to code jam";

int main()
{
	int i, j, k, len, l;
	
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	l = strlen(W);
	
	scanf("%d\n", &N);
	for (i = 1; i <= N; ++i)
	{
		fgets(s, sizeof(s), stdin);
		len = strlen(s);
		for (j = 0; j < len; ++j)
			if (!((s[j] >= 'a' && s[j] <= 'z') || (s[j] == ' ')))
				break;
		len = j;
		
		memset(M, 0, sizeof(M));
		for (k = 0; k <= len; ++k)
			M[k][0] = 1;
		for (k = 1; k <= len; ++k)
			for (j = 1; j <= l; ++j)
			{
				M[k][j] = M[k-1][j];
				if (W[j-1] == s[k-1])
					M[k][j] += M[k-1][j-1];
				if (M[k][j] >= MOD)
					M[k][j] -= MOD;
			}
		
		printf("Case #%d: %04d\n", i, M[len][l] % MOD);
	}

	return 0;
}
