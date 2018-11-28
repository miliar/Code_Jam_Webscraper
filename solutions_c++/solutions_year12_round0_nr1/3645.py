#include <stdio.h>
#include <string.h>

char msk[30] = "yhesocvxduiglbkrztnwjpfmaq";

int main()
{
	int i, j, l, cas;
	char str[1000];
	scanf("%d", &cas);
	gets(str);
	for (i = 1; i <= cas; i++)
	{
		printf("Case #%d: ", i);
		gets(str);
		for (j = 0, l = strlen(str); j < l; j++)
			if (str[j] == ' ')
				printf(" ");
			else
				printf("%c", msk[str[j] - 'a']);
		printf("\n");
	}
	return 0;
}
