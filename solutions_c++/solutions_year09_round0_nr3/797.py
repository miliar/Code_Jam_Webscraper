#include <stdio.h>
#include <string.h>

int main()
{	
	const char* pattern = "welcome to code jam";
	const size_t pat_len = 19;

	const int module = 10000;
	const int max_len = 600;
	char buffer[max_len];
	int dps[max_len][pat_len];

	int nCases = 0;
	scanf("%d",&nCases);
	getchar();
	for(int iCases = 1;iCases <= nCases;iCases ++)
	{
		memset(dps,0,sizeof(dps));
		gets(buffer);
		int len = strlen(buffer);
		dps[0][0] = (pattern[0] == buffer[0]);
		for(int i = 1;i < len;i ++)
		{
			dps[i][0] = (dps[i-1][0] + (pattern[0] == buffer[i]))%module;
			for(int k = 1;k < pat_len;k ++)
			{
				dps[i][k] = dps[i-1][k];
				if(buffer[i] == pattern[k]) dps[i][k] += dps[i-1][k-1];
				dps[i][k] %= module;
			}
		}
		printf("Case #%d: %04d\n",iCases,dps[len-1][pat_len-1]);
	}
	return 0;
}