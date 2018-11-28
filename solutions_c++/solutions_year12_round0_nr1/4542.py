#include<stdio.h>
#include<stdlib.h>
#include<string.h>

char a[150]={};
char b[150]={};
char c[27]={};
char g[101]={};
int n=0;

int main(void)
{
	freopen("proA.in","r",stdin);
	freopen("proA.out","w",stdout);
	gets(a);
	gets(b);
	int len=strlen(a);
	for (int i=0;i<len;i++)
	{
		c[a[i]-'a']=b[i];
	}
	c['z'-'a']='q';
	c['q'-'a']='z';
	scanf("%d",&n);
	char tmp[4]={};
	gets(tmp);
	for (int i=1;i<=n;i++)
	{
		gets(g);
		len=strlen(g);
		printf("Case #%d: ",i);
		for (int j=0;j<len;j++)
		{
			if(g[j]==' ') printf(" ");
			else printf("%c",c[g[j]-'a']);
		}
		printf("\n");
		for (int i=0;i<len;i++)
		{
			g[i]='\0';
		}
	}
	return 0;
}
