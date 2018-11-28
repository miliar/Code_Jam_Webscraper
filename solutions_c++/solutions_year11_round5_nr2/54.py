#include <stdio.h>

int n;
int card[10001];

int main ()
{
	int t, ct = 0;
	
	for (scanf ("%d", &t); t > 0; t --)
	{
		scanf ("%d", &n);
		
		for (int i = 0; i <= 10000; i ++)
			card[i] = 0;
			
		for (int i = 0; i < n; i ++)
		{
			int cardo;
			scanf ("%d", &cardo);
			card[cardo] ++;
		}
		
		int min = n;

		while (n)
		{
			int i;
			for (i = 10000; i > 0 && card[i] <= card[i - 1]; i --);
//			printf ("i = %d\n", i);
			card[i] --;
			n --;
			int l = 1;
			while (card[i + 1])
			{
				 i ++;
				 l ++;
				 card[i] --;
				 n --;
			}
			
//			printf ("l = %d\n", l);
			
			if (l < min) min = l;
		}
		
		printf ("Case #%d: %d\n", ++ ct, min);
	}

	return 0;
}
