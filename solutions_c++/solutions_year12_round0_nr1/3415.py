#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main()
{
	char translate[] = "yhesocvxduiglbkrztnwjpfmaq";
	char g[102];
	
	int t, i, j;
	
	scanf("%d",&t);
	getchar();
	fflush(stdin);
	
	for(i=0; i<t; i++)
	{
		gets(g);
		printf("Case #%d: ", i+1);
		for(j=0; j<strlen(g); j++)
			if(isalnum(g[j]))
				putchar(translate[g[j]-97]);
			else
				putchar(g[j]);
		putchar('\n');
	}
	
	return 0;
}
