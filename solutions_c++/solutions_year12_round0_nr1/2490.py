#include <cstdio>
#include <cstring>
char c[]="abcdefghijklmnopqrstuvwxyz";
char t[]="yhesocvxduiglbkrztnwjpfmaq";
char s[500];
int main()
{
	int T,w=1;
	scanf("%d ",&T);
	while(T--)
	{
		gets(s);
		printf("Case #%d: ",w++);
		for(int i=0;i<strlen(s);i++)
			if(s[i]==' ')putchar(' ');
			else
				putchar(t[s[i]-'a']);
		puts("");
	}
}
