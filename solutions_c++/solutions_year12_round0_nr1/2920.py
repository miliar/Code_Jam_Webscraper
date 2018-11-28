#include <stdio.h>
#include <string.h>
char trans[]={'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
int main()
{
	int t, n, i, j;
	char str[101];

	scanf("%d\n", &t);
	for (i = 0; i < t; i++)
	{
		printf("Case #%d: ", i+1);
		gets(str);
		n = strlen(str);
		for (j = 0; j < n; j++)
		{
			if (str[j] >= 'a' && str[j] <= 'z')
				putchar(trans[str[j]-'a']);
			else
				putchar(' ');
		}
		puts("");
	}
	return 0;
}
