#include <stdio.h>
#include <string.h>

char mem[] = "welcome to code jam";
char inp[600];
int d[600][30], len;

void count()
{
	int i, j;

	len = strlen(inp);
	for(j = 1; j <= 19; j++)
		for(i = j; i <= len; i++)
		{
			d[i][j] = d[i-1][j];
			if(inp[i-1] == mem[j-1])
				d[i][j] = (d[i][j] + d[i-1][j-1]) % 10000;
		}
}

int main()
{
	int t, z = 1;

	for(t = 0; t < 600; t++)
		d[t][0] = 1;
	scanf("%d", &t);
	gets(inp);
	while(t > 0)
	{
		gets(inp);
		count();
		printf("Case #%d: %.4d\n", z++, d[len][19]);
		t--;
	}

	return 0;
}