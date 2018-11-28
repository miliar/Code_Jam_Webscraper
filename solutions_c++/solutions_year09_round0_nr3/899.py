#include <stdio.h>
#include <string.h>

char str[]="welcome to code jam";
int a[1000][20];

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int T,t,i,n,j;
	char s[1000];
	scanf("%d%c",&T,&s[0]);
	t=1;
	while(T--)
	{
		for(i=0;i<1000;i++)
			for(j=0;j<20;j++)
				a[i][j]=0;
		gets(s);
		n=strlen(s);
		if(s[0]=='w')
			a[0][1]=1;
		for(i=1;i<n;i++)
			if(s[i]=='w')
				a[i][1]=a[i-1][1]+1;
			else
				a[i][1]=a[i-1][1];
		for(i=1;i<n;i++)
			for(j=2;j<=19;j++)
				if(s[i]==str[j-1])
					a[i][j]=(a[i-1][j-1]+a[i-1][j])%10000;
				else
					a[i][j]=a[i-1][j];
		printf("Case #%d: %04d\n",t,a[n-1][19]);
		t++;
	}
	return 0;
}
/*
So you've registered. We sent you a welcoming email, to welcome you to code jam. But it's possible that you still don't feel welcomed to code jam. That's why we decided to name a problem "welcome to code jam." After solving this problem, we hope that you'll feel very welcome. Very welcome, that is, to code jam.
*/