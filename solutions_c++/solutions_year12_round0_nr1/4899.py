#include <stdio.h>

char s[27]="yhesocvxduiglbkrztnwjpfmaq";

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int C=0,T;
	scanf("%d",&T);
	while(++C<=T)
	{
		printf("Case #%d: ",C);
		char t[110];
		int ch;
		do
		{
			scanf("%s",t);
			for(char *p=t;*p;p++)putchar(s[*p-'a']);
			ch=getchar();
			if(ch==' ')putchar(' ');
		}while(ch==' ');
		putchar('\n');		
	}
	return 0;
}
