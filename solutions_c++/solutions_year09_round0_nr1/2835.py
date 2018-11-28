// PracticeA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "string.h"

long L, D, N;
char allWords[5005][16];
char testerPattern[50000];


int _tmain(int argc, _TCHAR* argv[])
{
	freopen("c:\\in.txt","r",stdin);
	freopen("c:\\outBig.txt","w",stdout);
	long count, testerLen, k, DLen, l;
	bool flag, tempFlag;
	scanf("%ld%ld%ld",&L, &D, &N);

	for(long i = 0;i<D;i++)
		scanf("%s",allWords[i]);

	for(int n=1;n<=N;n++)
	{
		scanf("%s",testerPattern);
		count = 0;
		for(int d = 0;d<D;d++)
		{
			k = 0;
			testerLen = strlen(testerPattern);
			DLen = strlen(allWords[d]);

			flag = true;
			for(l = 0;l<DLen;l++)
			{
				if(testerPattern[k] == '(')
				{
					k++;
					tempFlag = false;
					while(testerPattern[k] != ')')
					{
						if(testerPattern[k] == allWords[d][l])
						{
							tempFlag = true;
						}
						k++;
					}
					if(tempFlag == false)
					{
						flag = false;
						break;
					}
				}
				else
				{
					if(testerPattern[k] != allWords[d][l])
					{
						flag = false;
						break;
					}
				}
				k++;
			}
			if(k != testerLen)
				flag = false;
			if(flag)
				count++;
		}
		printf("Case #%ld: %ld\n",n, count);
	}

	return 0;
}

