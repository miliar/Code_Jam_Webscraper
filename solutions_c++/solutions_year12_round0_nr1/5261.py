#include <stdio.h>
#include <string.h>

int main()
{
	int t, test=1, i;
	char s[30]="yhesocvxduiglbkrztnwjpfmaq";
	char string[110];

	scanf("%d",&t);
	getchar();
	while(t--)
	{
		gets(string);
		for(i=0;string[i]!='\0';i++)
		{
			if(string[i]!=' ')
			{
				string[i] = s[string[i]-'a'];
			}
		}
		printf("Case #%d: %s\n", test++, string);
	}

	return 0;
}