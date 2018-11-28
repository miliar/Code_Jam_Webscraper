#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char converter(char c)
{
	switch(c)
	{
	case 'a': return 'y'; break;
	case 'b': return 'h'; break;
	case 'c': return 'e'; break;
	case 'd': return 's'; break;
	case 'e': return 'o'; break;
	case 'f': return 'c'; break;
	case 'g': return 'v'; break;
	case 'h': return 'x'; break;
	case 'i': return 'd'; break;
	case 'j': return 'u'; break;
	case 'k': return 'i'; break;
	case 'l': return 'g'; break;
	case 'm': return 'l'; break;
	case 'n': return 'b'; break;
	case 'o': return 'k'; break;
	case 'p': return 'r'; break;
	case 'q': return 'z'; break;
	case 'r': return 't'; break;
	case 's': return 'n'; break;
	case 't': return 'w'; break;
	case 'u': return 'j'; break;
	case 'v': return 'p'; break;
	case 'w': return 'f'; break;
	case 'x': return 'm'; break;
	case 'y': return 'a'; break;
	case 'z': return 'q'; break;
	case ' ': return ' '; break;
	}
}

int main()
{
	int T, i, j;
	char riadok[101];
	scanf("%d", &T);
	getchar();
	for(i=0; i<T; i++)
	{
		gets(riadok);
		printf("Case #%d: ", i+1);
		for(j=0; j<strlen(riadok); j++) putchar(converter(riadok[j]));
		putchar('\n');
	}
}