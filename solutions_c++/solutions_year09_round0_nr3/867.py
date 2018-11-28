#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int n,a[510][22];
char s[510];
const char str[22]="\0welcome to code jam";
int main()
{
	int _,t;
	gets(s);_=atoi(s);
	for(t=1; t<=_; t++)
	{
		gets(s+1);
		n=strlen(s+1);
		memset(a,0,sizeof(a));
		a[0][0]=1;
		for(int i=1; i<=n; i++)
			for(int j=0; j<=19; j++)
			{
				a[i][j]+=a[i-1][j];
				if(a[i][j]>=10000)a[i][j]-=10000;
				if(s[i]==str[j])
				{
					a[i][j]+=a[i-1][j-1];
					if(a[i][j]>=10000)a[i][j]-=10000;
				}
			}
		printf("Case #%d: %04d\n",t,a[n][19]);
	}
	return 0;
}