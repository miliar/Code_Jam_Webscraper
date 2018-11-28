#include <stdio.h>

int tc,TC;
char r[27]="yhesocvxduiglbkrztnwjpfmaq";
char a[128];

int main()
{
	int i;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	for(scanf("%d ",&TC),tc=1;tc<=TC;++tc)
	{
		gets(a);
		for(i=0;a[i];++i)
			if(a[i]!=' ') a[i]=r[a[i]-'a'];
		if(a[i-1]=='\n') a[i-1]=0;
		printf("Case #%d: %s\n",tc,a);

	}
	return 0;
}