#include <stdio.h>

const char mapping[]="yhesocvxduiglbkrztnwjpfmaq";

int main()
{
	int tc,t,i;
	char s[1024];
	gets(s);
	sscanf(s,"%d\n",&t);
	for (tc=0;tc<t;++tc)
	{
		gets(s);
		for (i=0;s[i];++i) if (s[i]!=' ') s[i]=mapping[s[i]-'a'];
		printf("Case #%d: ",tc+1);
		puts(s);
	}
	return 0;
}