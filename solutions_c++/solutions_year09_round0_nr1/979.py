#include<stdio.h>

int csK, csN, L, D, P[16], ans;
char W[8192][16];

int main()
{
	int i, j, k;
	char str[131072];
	scanf("%d %d %d", &L, &D, &csN);
	for(i = 0; i < D; ++i)
		scanf("%s", W[i]);
	for(csK = 1; csK <= csN; ++csK)
	{
		scanf("%s", str);
		for(i = 0; i < L; ++i) P[i] = 0;
		for(i = j = 0; i < L; ++i)
		{
			if('a' <= str[j] && str[j] <= 'z')
				P[i] = 1 << (str[j++]-'a');
			else
			{
				while(str[j] != '\0' && str[++j] != ')')
				{
					P[i] |= 1 << (str[j]-'a');
				}
				if(str[j] == '\0') break;
				++j;
			}
		}
		if(i < L || str[j] != '\0') ans = 0;
		else
		{
			for(ans = i = 0; i < D; ++i)
			{
				for(j = 0; j < L; ++j)
					if((P[j]&(1<<(W[i][j]-'a'))) == 0) break;
				if(j == L) ++ans;
			}
		}
		printf("Case #%d: %d\n", csK, ans);
	}
}
