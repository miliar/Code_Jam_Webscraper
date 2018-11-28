#include<stdio.h>
#include<string.h>

int csN, csK, L, cnt[1024], sum;
char P[32] = "welcome to code jam", S[1024];

int main()
{
	int i, j, k;
	scanf("%d", &csN);
	gets(S);
	for(csK = 1; csK <= csN; ++csK)
	{
		gets(S);
		memset(cnt, 0, sizeof(cnt));
		L = strlen(S);
		for(i = 0; i < L; ++i)
			if(S[i] == P[0]) cnt[i] = 1;
		for(i = 1; P[i]; ++i)
		{
			for(sum = j = 0; j < L; ++j)
			{
				k = (sum+cnt[j]) % 10000;
				if(S[j] == P[i]) cnt[j] = sum;
				else cnt[j] = 0;
				sum = k;
			}
		}
		for(sum = i = 0; i < L; ++i)
			sum = (sum+cnt[i]) % 10000;
		printf("Case #%d: %04d\n", csK, sum);
	}
}
