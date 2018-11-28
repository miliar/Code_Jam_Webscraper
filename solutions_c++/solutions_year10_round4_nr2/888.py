#include <stdio.h>
#include <math.h>


int data[10][1024];
int constraint[1024];

int main()
{
	int cases, numcase = 1;
	int P ,max, i, j, k, cost, tmpmax, c;
	bool bisa;

	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);

	for(scanf("%i", &cases); numcase <= cases; numcase++)
	{
		scanf("%i", &P);
		max = (int) pow(2.0, P);

		cost = 0;
		for(i = 0; i < max; i++)
			scanf("%i", &constraint[i]);

		for(c = 0, i = P - 1; i >= 0; i--, c++)
		{
			tmpmax = (int) pow(2.0, i);
			for(j = 0; j < tmpmax; j++)
				scanf("%i", &data[c][j]);
		}

		for(i = 1; i <= P; i++)
		{
			tmpmax = (int) pow(2.0, i);
			for(j = 0; j < max; j += tmpmax)
			{
				bisa = true;
				for(k = j; k < j + tmpmax; k++)
				{
					if(constraint[k] == 0)
					{
						bisa = false;
						break;
					}
				}

				if(bisa)
				{
					for(k = j; k < j + tmpmax; k++)
					{
						constraint[k]--;
					}
				}
				else
					cost++;
			}
		}

		printf("Case #%i: %i\n", numcase,cost);
	}

	return 0;
}