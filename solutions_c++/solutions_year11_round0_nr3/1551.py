# include <algorithm>
# include <stdio.h>


int main ()
{
	int Case, T, n, num, minnum, sum, xor ;
	freopen ("c.in", "r", stdin) ;
	freopen ("c.out", "w", stdout) ;
	scanf ("%d", &T) ;
	for (Case = 1 ; Case <= T ; Case ++)
	{
		minnum = 0x0fffffff ;
		sum = xor = 0 ;

		scanf ("%d", &n) ;
		while (n--)
		{
			scanf ("%d", &num) ;
			if (num < minnum) minnum = num ;
			sum += num ;
			xor ^= num ;
		}

		if (xor != 0)
			printf ("Case #%d: NO\n", Case) ;
		else
			printf ("Case #%d: %d\n", Case, sum - minnum) ;
	}
	return 0 ;
}
