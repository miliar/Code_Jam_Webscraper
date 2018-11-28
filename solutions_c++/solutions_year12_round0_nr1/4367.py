#include<stdio.h>
#include<string.h>
char a[26];
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.out","w",stdout);
	char b[3][100]={"ejp mysljylc kd kxveddknmc re jsicpdrysi","rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","de kr kd eoya kw aej tysr re ujdr lkgc jv"};
	char c[3][100]={"our language is impossible to understand","there are twenty six factorial possibilities","so it is okay if you want to just give up"};
	char s[1000];
	int n,cas=0;
	int i,j;
	a[25]='q';
	a[16]='z';
	for(i=0;i<3;i++)
	{
		for(j=0;j<strlen(b[i]);j++)
			if(b[i][j]!=' ')
				a[b[i][j]-'a']=c[i][j];
	}
	scanf("%d",&n);
	gets(s);
	while(n--)
	{
		gets(s);
		for(i=0;i<strlen(s);i++)
			if(s[i]!=' ')
				s[i]=a[s[i]-'a'];
		printf("Case #%d: %s\n",++cas,s);
	}
}