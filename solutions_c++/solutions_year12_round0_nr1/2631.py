#include <stdio.h>
#include <ctype.h>
#include <string.h>

char mapping[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

void solve()
{
	int n;
	char input[101];
	char output[101];
	scanf("%d\n", &n);
	for(int i = 1; i <= n; i++)
	{
		gets(input);
		int j = 0;
		for(j = 0; j < strlen(input); j++)
		{
			if(isalpha(input[j]))
			{
				output[j] = mapping[input[j] - 'a'];
			} else 
			{
				output[j] = input[j];
			}
		}
		output[j] = '\0';
		printf("Case #%d: %s\n", i, output);
	}
}

int main()
{
	solve();
	return 0;
}