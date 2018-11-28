# include <Stdio.h>


# define FOR(i,a,b) for (int i = a ; i< b; i ++)


int frec[110] ;
int N, L, H ;


int test (int f)
{
	FOR(i,0,N)
		if ((frec[i] % f != 0) && (f % frec[i] != 0)) return 0 ;
	return 1 ;
}


int work ()
{
	if (L == 1) return 1 ;
	FOR(i,L,H+1)
		if (test (i)) return i ;
	
	return 0 ;
}

int main ()
{
	int T ;
	int nCase = 1 ;
	int frc ;
	
	freopen ("C-small-attempt0.in", "r", stdin) ;
	freopen ("C.txt", "w", stdout) ;
	
	
	scanf ("%d", &T) ;
	while (T--)
	{
		scanf ("%d%d%d", &N, &L, &H) ;
		FOR(i,0,N) scanf ("%d", frec + i) ;
		printf ("Case #%d: ", nCase++) ;
		frc = work() ;
		if (frc == 0) puts ("NO") ;
		else printf ("%d\n", frc) ;
	}
	return 0 ;
}

