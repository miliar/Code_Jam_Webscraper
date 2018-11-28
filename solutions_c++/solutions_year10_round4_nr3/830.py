#include <stdio.h>
#include <string.h>


int data[101][101];

int main()
{
	int cases, i, j, k, numcase = 1, R, x1, y1, x2, y2;
	int second, bacteria;

	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);

	for(scanf("%i", &cases); numcase <= cases; numcase++)
	{
		scanf("%i", &R);

		second = 0;
		bacteria = 0;
		memset(data, 0, 40804);		
		for(i = 0; i < R; i++)
		{
			scanf("%i %i %i %i", &x1, &y1, &x2, &y2);
			for(j = y1; j <= y2; j++)
			{
				for(k = x1; k <= x2; k++)
				{
					if(data[j][k] == 0)
					{
						data[j][k] = 1;
						bacteria++;
					}
				}
			}
		}

		while(bacteria > 0)
		{
			for(j = 100; j >= 1; j--)
			{
				for(k = 100; k >= 1; k--)
				{
					if(data[j][k] == 0)
					{
						if(data[j-1][k] == 1 && data[j][k-1] == 1)
						{
							data[j][k] = 1;
							bacteria++;
						}
					}
					else
					{
						if(data[j-1][k] == 0 && data[j][k-1] == 0)
						{
							data[j][k] = 0;
							bacteria--;
						}
					}
				}
			}
			second++;
		}
		printf("Case #%i: %i\n", numcase, second);
	}

	return 0;
}\