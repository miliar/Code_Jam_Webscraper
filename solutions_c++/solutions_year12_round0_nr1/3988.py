#include<stdio.h>

char wrd[] = "abcdefghijklmnopqrstuvwxyz";
char mpw[] = "yhesocvxduiglbkrztnwjpfmaq";

int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.ans", "w", stdout);

	char str[111];
	int tst;

	scanf("%d", &tst);
	gets(str);
	for(int t=1; t<=tst; t++)
	{
		gets(str);
		printf("Case #%d: ", t);
		for(int i=0; str[i]; i++)
			if(str[i]==' ')
				printf(" ");
			else
				printf("%c", mpw[str[i]-'a']);
		puts("");
	}
	return 0;
}





