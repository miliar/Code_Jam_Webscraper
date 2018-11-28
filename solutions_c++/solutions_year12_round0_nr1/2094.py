#include<stdio.h>

int main()
{
	freopen("A1.in","r",stdin);
	freopen("A1.out","w",stdout);
	char s[] = "yhesocvxduiglbkrztnwjpfmaq";
	char g[1005];
	int t,cs=0,i;
	gets(g);
	sscanf(g,"%d",&t);
	while(t--)
	{
		gets(g);
		for(i=0;g[i];i++)
			if(g[i]!=' ')
				g[i] = s[g[i]-'a'];

		printf("Case #%d: %s\n",++cs,g);
	}
	return 0;
}