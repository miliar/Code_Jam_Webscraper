#include <stdio.h>
#include <string.h>

int main()
{
    int i, j, n;
	scanf("%d\n", &n);
	for(i = 1; i <= n; i++)
	{
		char g[2000];
		gets(g);
		for(j = 0; j < strlen(g); j++)
		{
			switch(g[j])
			{
			case 'a': g[j] = 'y'; break;
			case 'b': g[j] = 'h'; break;
			case 'c': g[j] = 'e'; break;
			case 'd': g[j] = 's'; break;
			case 'e': g[j] = 'o'; break;
			case 'f': g[j] = 'c'; break;
			case 'g': g[j] = 'v'; break;
			case 'h': g[j] = 'x'; break;
			case 'i': g[j] = 'd'; break;
			case 'j': g[j] = 'u'; break;
			case 'k': g[j] = 'i'; break;
			case 'l': g[j] = 'g'; break;
			case 'm': g[j] = 'l'; break;
			case 'n': g[j] = 'b'; break;
			case 'o': g[j] = 'k'; break;
			case 'p': g[j] = 'r'; break;
			case 'q': g[j] = 'z'; break;
			case 'r': g[j] = 't'; break;
			case 's': g[j] = 'n'; break;
			case 't': g[j] = 'w'; break;
			case 'u': g[j] = 'j'; break;
			case 'v': g[j] = 'p'; break;
			case 'w': g[j] = 'f'; break;
			case 'x': g[j] = 'm'; break;
			case 'y': g[j] = 'a'; break;
			case 'z': g[j] = 'q'; break;
			default: break;
			}
		}
		printf("Case #%d: ", i);
		puts(g);
		//putchar('\n');
	}
	return 0;
}