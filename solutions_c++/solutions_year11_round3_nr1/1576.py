#include <stdio.h>

int main()
{
	int numCase, cases;
	
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int R, C, i, j;
	bool error;
	char data[50][51];

	for(scanf("%i", &cases), numCase = 1; numCase <= cases; numCase++)
	{
		scanf("%i %i", &R, &C);
		for(i = 0; i < R; i++)
			scanf("%s", data[i]);

		error = false;
		for(i = 0; i < R && !error; i++)
		{
			for(j = 0; j < C && !error; j++)
			{
				if(data[i][j] == '#')
				{
					if(i+1 < R && j+1 < C &&
						data[i+1][j] == '#' && data[i][j+1] == '#' && data[i+1][j+1] == '#')
					{
						data[i][j] = '/';
						data[i][j+1] = '\\';
						data[i+1][j] = '\\';
						data[i+1][j+1] = '/';
					}
					else
					{
						error = true;
						break;
					}
				}
			}
		}

		printf("Case #%i:\n", numCase);
		if(error) printf("Impossible\n");
		else
		{
			for(i = 0; i < R; i++)
			{
				for(j = 0; j < C; j++)
				{
					printf("%c", data[i][j]);
				}
				printf("\n");
			}
		}
	}
	
	return 0;
}