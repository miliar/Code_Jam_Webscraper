# include <stdio.h>


int work (int n, int pd, int pg)
{
	int i ;
	if (pd != 100 && pg == 100) return 0 ;
	if (pd != 0 && pg == 0) return 0 ;
	if (n >= 100) return 1 ;
	for (i = 1 ; i <= n ; i++)
		if ((i * pd % 100) == 0) return 1 ;
	return 0 ;
}


int main ()
{
	int T, n, pd, pg ;
	int Case = 0 ;
	
	freopen ("1.txt", "r", stdin) ;
	freopen ("1.out", "w", stdout) ;
	scanf ("%d", &T) ;
	while (T--)
	{
		scanf ("%d%d%d", &n, &pd, &pg) ;
		printf ("Case #%d: %s\n", 
			++Case, work(n,pd,pg) ? "Possible" : "Broken") ;
	}
	return 0 ;
}