#include <stdio.h>
#include <string.h>

const char M[] = "welcome to code jam";

char buff[1024];
int DP[20];

int main()
{
	int N;
	scanf("%d", &N);
	gets(buff);
	for (int n = 1; n <= N; n++)
	{
		gets(buff);
		memset(DP, 0, sizeof(DP));
		DP[0] = 1;
		for (char *p = buff; *p != '\0'; p++)
		{
			char ch = *p;
			for (int i = sizeof(M) - 2; i >= 0; i--)
			{
				if (ch == M[i])
				{
					DP[i+1] = (DP[i+1] + DP[i]) % 10000;
				}
			}
		}
		printf("Case #%d: %04d\n", n, DP[sizeof(M)-1]);
	}

	return 0;
}