#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define N 510
char a[N];
int  ans[N][30];
void solve()
{
	int i, len, j;
	char t[]="welcome to code jam";
	gets(a);
	len=strlen(a);
	memset(ans,0,sizeof(ans));
	ans[0][0]=1;
	for(i=1;i<=len;i++)
	{
		ans[i][0]=ans[i-1][0];
		for(j=1;j<=19;j++)
		{
			ans[i][j]=ans[i-1][j];
			if(a[i-1]==t[j-1])
			{
				ans[i][j]+=ans[i-1][j-1];
				ans[i][j]%=10000;
			}
		}
	}
	printf("%04d\n",ans[len][19]%10000);
}
int main()
{
	//freopen("out.txt","w",stdout);
	int i, T;
	scanf("%d",&T);
	getchar();
	for(i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
