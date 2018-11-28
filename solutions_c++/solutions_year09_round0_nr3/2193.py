// Google C.cpp : 定义控制台应用程序的入口点。
//

//#include "stdafx.h"

#include <stdio.h>
#include <string.h>
#define M 10000

//0123456789012345678
//welcome to code jam

int main(void)
{
	freopen("C-large.in", "r", stdin);
	freopen("C-baoer.out", "w", stdout);

	char str[505];
	char ss[] = "welcome to code jam";
	int f[505][25];
	int n,len;
	int i,j,k=1;
	scanf("%d",&n);
	gets(str);
	while(n--)
	{
		gets(str);
		len = strlen(str);

		for(i=0; i<20; i++)
			f[0][i] = 0;

		for(i=1; i<=len; i++)
		{
			for(j=0; j<20; j++)
				f[i][j] = f[i-1][j];

			for(j=0; j<20; j++)
			{
				if(str[i-1] == ss[j] && j != 0)
				{
					f[i][j] = (f[i-1][j] + f[i-1][j-1]) % M;
				}
				else if(str[i-1] == ss[j] && j == 0)
				{
					f[i][j] = (f[i-1][j] + 1) % M;
				}
			}
		}
		printf("Case #%d: ", k++);
		int ans = f[len][18];
		if(ans<10)
			printf("000");
		else if(ans<100)
			printf("00");
		else if(ans<1000)
			printf("0");
		printf("%d\n",ans);
	}
	return 0;
}

