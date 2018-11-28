#include<cstdio>
#include<string.h>

using namespace std;

int tt;
int n;
char G[30];

void init()
{
	const char *g="ejp mysljylc kd kxveddknmc re jsicpdrysi\
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\
de kr kd eoya kw aej tysr re ujdr lkgc jvqz";
	const char *s="our language is impossible to understand\
there are twenty six factorial possibilities\
so it is okay if you want to just give upzq";
	for(int i=0;i<(int)strlen(g);++i)
		if (g[i]>='a')
			G[g[i]-'a']=s[i];
}

char s[111];

int main()
{
	init();
	scanf("%d\n",&tt);
	for(int t=1;t<=tt;++t)
	{
		gets(s);
		for(int i=strlen(s)-1;i>=0;--i)
			if (s[i]!=' ')
				s[i]=G[s[i]-'a'];
		printf("Case #%d: ",t);
		puts(s);
	}
	return 0;
}
