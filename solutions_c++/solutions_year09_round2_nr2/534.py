#include "stdio.h"
#include "string.h"
int T,t,i,j,k,l,c[10];
char n[30];

void work(int x)
{
	if(x==-1) {
		x=0; ++c[0];
		for(j=1;j<=9;j++)
			if(c[j]) {--c[j]; n[x++]=(char)(48+j);break;}
		for(l=strlen(n);l>0;l--)
			for(j=0;j<=9;j++)
				if(c[j]) {--c[j];n[x++]=(char)(48+j);break;}
		n[x]='\0';
		return;
	}
	int y=n[x]-'0';
	for(j=y+1;j<=9;j++)
		if (c[j])
		{
			--c[j]; ++c[y];
			n[x]=(char)(48+j);
			for(k=x+1;k<(int)strlen(n);k++)
				for(l=0;l<=9;l++)
					if(c[l])
					{
						--c[l];n[k]=(char)(48+l);break;
					}
			return;
		}
	++c[y];
	work(x-1);
}

int main(void)
{
	scanf("%d",&T);
	gets(n);
	for(t=1;t<=T;t++)
	{
		gets(n);
		printf("Case #%d: ", t);
		if(strlen(n)==1)
			printf("%s0\n",n);
		else
		{
			for(i=0;i<=9;i++) c[i]=0;
			c[n[strlen(n)-1]-48]++;
			work(strlen(n) - 2);
			printf("%s\n", n);
		}
	}
}
