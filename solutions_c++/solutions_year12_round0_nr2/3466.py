#include <cstdio>
#include <cstring>

int main ()
{
	freopen ("largeoutb.txt","w",stdout);
	freopen ("B-large.in","r",stdin);

	int tc, i, j, num, surp, best, total, x, googlers;

	scanf ("%d", &tc);

	for (i = 1; i <= tc; i++)	{

		scanf ("%d %d %d", &num, &surp, &best);
		//printf ("%d %d %d ", num, surp, best);
		googlers	=	0;

		for (j = 0; j < num; j++)	{

			scanf ("%d", &total);
			//printf("%d ", total);
			x	=	total / 3;

			if (total >= 0 && best == 0)	{

				googlers++;

			}	else if (total > 0)	{

				switch (total % 3)	{

					case 0:
						if (best <= x)
							googlers++;
						else if (best - x == 1 && surp > 0)	{
							surp--;
							googlers++;
						}
						break;

					case 1:
						if (best - x <= 1)
							googlers++;
						break;

					case 2:
						if (best - x <= 1)
							googlers++;
						else if (best - x ==2 && surp > 0)	{
							googlers++;
							surp--;
						}
						break;
				}

			}

		}

		printf ("Case #%d: %d\n", i, googlers);

	}

	return 0;

}