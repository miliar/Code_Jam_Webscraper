#include <stdio.h>
#include <string.h>
int dy[510][19];
const char* welcome = "welcome to code jam";
int main()
{
	char buffer[600];
	int n;

	scanf("%d\n", &n);
	for (int i = 0 ; i < n ; i++)
	{
		fgets(buffer + 1, 600, stdin);
		int j, k;
		for (j = 1 ; buffer[j] != '\n' && buffer[j] != '\0' ; j++)
			for (k = 0 ; k <= 18 ; k++)
			{
				dy[j][k] = dy[j - 1][k];
				if (buffer[j] == welcome[k])
				{
					if (k == 0)
						dy[j][k] = (dy[j][k] + 1) % 10000;
					else
						dy[j][k] = (dy[j][k] + dy[j - 1][k - 1]) % 10000;
				}
			}
		printf("Case #%d: %04d\n", i + 1, dy[j - 1][18]);
	}
	return 0;
}
