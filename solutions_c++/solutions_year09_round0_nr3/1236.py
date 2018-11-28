#include "stdio.h"
#include "string.h"
int dp[501],mid[501];
char x[501],y[20]="welcome to code jam";
int main()
{
	int t,c,i,k,j,l;
	scanf("%d",&t);
	getchar();
	for(c=1;c<=t;c++)
	{
		gets(x);
		l=strlen(x);
		for(i=0;i<=l;i++)
			if(x[i]=='w')dp[i]=1;
			else dp[i]=0;
		for(i=1;i<=19;i++)
		{
			for(k=0;k<=l;k++)
				mid[k]=0;
			for(k=0;k<=l;k++)
				if(x[k]==y[i])
					for(j=0;j<k;j++)
						mid[k]+=dp[j];
			for(k=0;k<=l;k++)
				dp[k]=mid[k]%10000;
		}
		printf("Case #%d: %04d\n",c,dp[l]);
	}
	return 0;
}