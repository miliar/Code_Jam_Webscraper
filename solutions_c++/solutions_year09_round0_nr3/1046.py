#include <stdio.h>
#include <string.h>
char ch[505],wel[20]="welcome to code jam";
int x[505][20];
int main()
{
	int kase,kk,i,k,j,l;
	scanf("%d\n",&kase);
	for(kk=1;kk<=kase;kk++)
	{
		gets(ch);
		l=strlen(ch);
		for(i=0;i<=l;i++)
			for(k=0;k<20;k++)
				x[i][k]=0;
		for(i=0;i<l;i++)
			if(ch[i]=='w')
			x[i][0]=1;
		for(i=1;i<=19;i++)
		{
			for(k=0;k<=l;k++)
			{
				if(ch[k]!=wel[i])
				continue;
				for(j=0;j<k;j++)
					x[k][i]+=x[j][i-1];
				x[k][i]%=10000;
			}
		}
		printf("Case #%d: %04d\n",kk,x[l][19]);
	}
	return 0;
}
