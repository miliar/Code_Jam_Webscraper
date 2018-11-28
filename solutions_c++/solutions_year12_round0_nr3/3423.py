#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main()
{
	char strBuf[17], *pStr, *delim = " ";
	int T = atoi(gets(strBuf));
	while(T > 50 || T < 1)
		T = atoi(gets(strBuf));
	for(int i = 0; i < T; i++)
	{
		int Lim[2];
		gets(strBuf);
		pStr = strtok(strBuf, delim);
		for(int j = 0; j < 2; j++)
		{
			Lim[j] = atoi(pStr);
			pStr = strtok(0, delim);
		}
		int y = 0;
		for(int j = Lim[0]; j <= Lim[1]; j++)
		{
			int digit = 0, t = j;
			while(t)
			{
				digit++;
				t /= 10;
			}
			char *nStr = new char[digit+1];
			itoa(j, nStr, 10);
			for(int k = 1; k < digit; k++)
			{
				char *tStr = new char[digit+1];
				tStr[digit] = 0;
				for(int c = 0; c < digit; c++)
				{
					tStr[c] = (c+k)<digit?nStr[c+k]:nStr[abs(digit-c-k)];
				}
				if(tStr[0] != '0' && atoi(tStr) <= Lim[1] && atoi(tStr) > j)
				{
					y++;
					//printf("%d %d\n", j, atoi(tStr));
				}
				delete[] tStr;
			}
			delete[] nStr;
		}
		printf("Case #%d: %d\n", i+1, y);
	}
	return 0;
}