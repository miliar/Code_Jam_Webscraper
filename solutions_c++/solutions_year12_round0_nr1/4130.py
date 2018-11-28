#include<stdio.h>
char map[30]="yhesocvxduiglbkrztnwjpfmaq";
char s[200];
int main()
{
	int t,tt;
	scanf("%d",&tt);
	gets(s);
	for(t=1;t<=tt;t++)
	{
		gets(s);
		for(int i=0;s[i]!='\0';i++)
		{
			if(s[i]!=' ') s[i] = map[s[i]-'a'];
		}
		printf("Case #%d: %s\n",t,s);
	}
	return 0;
}
