#include <cstdio>
#include <cstring>

int main ()
{
	freopen ("outc.txt","w",stdout);
	freopen ("C-small-attempt4.in","r",stdin);

	int i, j, tc, a, b, arr [4], brr [4], count, num, numb, ll [4];

	scanf ("%d", &tc);

	for (i = 1; i <= tc; i++)	{

		count = 0;

		scanf ("%d %d", &a, &b);
		//printf("%d %d\n", a ,b);
		j		=	0;
		numb	=	b;

		if (b <= 10)	{

			printf ("Case #%d: %d\n", i, 0);
			continue;
		}

		while (b)	{

			brr [j] = b % 10;
			b		= b / 10;
			j++;
		}

		num = a;
		j = 0;
		while (a)	{

			ll [j++]	= a % 10;
			a	= a / 10;
		}
		a = num;
		for (num = a; num <= numb; num ++)	{

			a	=	num;
			j	=	0;

			while (a)	{

				arr [j] = a % 10;
				a		= a / 10;
				j++;
			}

			j	=	j -1;

			if (j > 1 && arr [j] == arr [j-1] && arr[j] == arr [0])
				continue;

			if ((arr [0] <= arr [j] && j <= 1) /*|| arr [0] == 0*/)
				continue;

			if (arr [1] == 0 && arr [0] ==0 && j > 1)
				continue;
		
			if (arr [0] > brr [j])
				continue;
			else if (arr [0] < ll [j])
				continue;
			else if (arr [0] == brr [j])	{

				if (arr [j] > brr [j - 1])
					continue;
				else if (j > 1 && arr [j] == brr [j - 1])	{

					if (arr [j - 1] > brr [j - 2])
						continue;
				}

			}
			
			if (arr [0] == ll [j])	{

				if (arr [j] < ll [j-1])
					continue;
				else if (j > 1 && arr [j] == ll [j-1])	{

					if (arr [j-1] < ll [j-2])
						continue;
				}

			}

			count++;
			//printf ("%d\n", num);
		}

		printf ("Case #%d: %d\n", i, count);
	}

	return 0;
}
		