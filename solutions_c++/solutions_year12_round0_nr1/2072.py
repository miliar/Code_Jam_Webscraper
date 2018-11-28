#include <stdio.h>
#include <string.h>

char repl[] = {
	'y', 'h', 'e', 's', 'o', 'c', 'v', 
	'x', 'd', 'u', 'i', 'g', 'l', 'b',
	'k', 'r', 'z', 't', 'n', 'w', 'j',
	'p', 'f', 'm', 'a', 'q'
};

int main()
{
	int t;
	char str[128];

	scanf("%d\n", &t);

	for(int a=0; a<t; a++)
	{
		fgets(str, sizeof(str), stdin);
		
		int len = strlen(str);
		str[len] = '\0';

		printf("Case #%d: ", a+1);
		for(int i=0; i<len-1; i++) {
			printf("%c", str[i] == ' ' ? ' ' : repl[str[i]-'a']);
		}
		printf("\n");
	}
	return 0;
}
