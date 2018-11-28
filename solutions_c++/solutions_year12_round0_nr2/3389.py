#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	char strBuf[400], *pStr;
	int T = atoi(gets(strBuf));
	while(T > 100 || T < 1)
		T = atoi(gets(strBuf));
	int N, S, p, *t;
	char *delim = " ";
	for(int i = 0; i < T; i++)
	{
		gets(strBuf);
		pStr = strtok(strBuf, delim);
		int j = 0;
		while(pStr)
		{
			switch(j)
			{
			case 0:
				N = atoi(pStr); t = new int[N]; break;
			case 1:
				S = atoi(pStr); break;
			case 2:
				p = atoi(pStr); break;
			default:
				t[j-3] = atoi(pStr); break;
			}
			j++;
			pStr = strtok(0, delim);
		}
		int Lim[2] = {3*p-4, 3*p-3}, sCount = 0, y = 0;
		Lim[0] = (Lim[0]<p)?p:Lim[0];
		for(j = 0; j < N; j++)
		{
			if(t[j] > Lim[1])
			{
				y++;
			}
			else if(t[j] <= Lim[1] && t[j] >= Lim[0] && sCount < S)
			{
				y++;
				sCount++;
			}
		}
		printf("Case #%d: %d\n", i+1, y);
	}
	delete[] t;
	return 0;
}