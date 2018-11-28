#include<iostream>
using namespace std;
char sta[50]="welcome to code jam";
int cn,ci,i,j,len;
char s[600];
int a[600][30];

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&cn);
	gets(s);
	for (ci=1;ci<=cn;ci++)
	{
		memset(s,0,sizeof(s));
		gets(s);
		len=strlen(s);
		a[0][0]=1;
		for (i=1;i<=19;i++) a[0][i]=0;
		if (s[0]=='w') a[0][1]=1;
		for (i=1;i<len;i++)
		{
			for (j=0;j<=19;j++) a[i][j]=a[i-1][j];
			for (j=0;j<19;j++)
			if (s[i]==sta[j]) a[i][j+1]=(a[i][j+1]+a[i-1][j])%10000;
		}
		printf("Case #%d: %04d\n",ci,a[len-1][19]);
	}
	return 0;
}
