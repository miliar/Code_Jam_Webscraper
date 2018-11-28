#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>

const char ms[20] = "welcome to code jam";

char str[1 << 10];
int N,L,ans[1 << 10][20];

int main()
{
	int i,j,k,t;
	//freopen("C-large.in","r",stdin);
	//freopen("3.txt","w",stdout);
	scanf("%d\n",&N);
	for(t = 1;t <= N;t++)
	{
		gets(str);
		memset(ans,0,sizeof(ans));
		ans[0][0] = 1;
		L = 0;
		for(i = 0;str[i];i++)
		{
			for(j = 0;j < 20;j++)
				ans[L + 1][j] = (ans[L + 1][j] + ans[L][j]) % 10000;
			for(j = 0;j < 19;j++)
			{
				if(str[i] == ms[j])
					ans[L + 1][j + 1] = (ans[L + 1][j + 1] + ans[L][j]) % 10000;
			}
			L++;
		}
		printf("Case #%d: %04d\n",t,ans[L][19]);
	}
	//system("PAUSE");
	return 0;
}
		
