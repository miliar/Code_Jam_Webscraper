#include <cstdio>

int L, D, N;

char W[6000][32];
char P[256];

int main(int argc, char *argv[])
{
	scanf("%d %d %d", &L, &D, &N);
	for (int i = 0; i < D; ++i)
		scanf("%s", &W[i][0]);

	for (int i = 0; i < N; ++i)
	{
		scanf("%s", P);
		int wCnt = 0;
		for (int j = 0; j < D; ++j)
		{
			char *cP = P;
			bool isOK = true;
			for (int k = 0; isOK && k < L; ++k)
			{
				if (*cP == '(')
				{
					bool isMOK = false;
					cP++;
					while (*cP != ')')
					{
						if (*cP == W[j][k])
							isMOK = true;
						cP++;
					}
					cP++;
					isOK &= isMOK;
				}
				else
				{
					isOK &= *cP++ == W[j][k];
				}
			}
			if (isOK)
				wCnt++;
		}
		printf("Case #%d: %d\n", i + 1, wCnt);
	}

	return 0;

}