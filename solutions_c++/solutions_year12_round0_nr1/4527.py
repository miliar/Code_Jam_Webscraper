#include <cstdio>
#include <cstring>
const char p[]="yhesocvxduiglbkrztnwjpfmaq";
char s[105];

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T,t,i,n;
	scanf("%d\n",&T);
	for (t=1; t<=T; ++t)
	{
		gets(s);
		n=strlen(s);
		for (i=0; i<n; ++i)
			if (s[i]!=' ') s[i]=p[s[i]-97];
		printf("Case #%d: %s\n",t,s);
	}
	return 0;
}
