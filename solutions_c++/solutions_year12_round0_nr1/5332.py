#include <stdio.h>
#include <string.h>

#define N 128

char map[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char string[N];

int main()
{
	int c, n, i, len;
	scanf("%d\n", &n);
	c = 0;
	while(c < n)
	{
		gets(string);
		len = strlen(string);
		for(i = 0; i < len; i++)
		{
			if(string[i] == ' ') continue;
			string[i] = map[string[i] - 'a'];
		}
		printf("Case #%d: %s\n", c + 1, string);
		c++;
	}
	return 0;
}