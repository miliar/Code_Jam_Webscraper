# include <stdio.h>
# include <math.h>


# define FOR(i,a,b) for (int i = a ; i < b ; i++)


int vnum ;
int c, d ;
int p[220] ;
int v[220] ;


int test (double t)
{
	
	int vv ;
	double pos = p[0] - t ;
	
	FOR(i, 0, c)
	{
		vv = v[i] ;
		if ((p[i] - pos) > t) pos = p[i] - t ; 
		while (vv--)
		{
			if (pos > (p[i] + t)) return 0 ;
			pos += d ;
		}
	}
	return 1 ;
}


double work()
{
	double l = 0, r = vnum * d ;
	double mid ;
	while (1)
	{
		mid = (l + r) / 2.0 ;
		if (test (mid)) r = mid ;
		else l = mid ;
		if ((r - l) <= 1e-7) break ;
	}
	return mid ;
}


int main ()
{
	int T, nCase = 1 ;
//	freopen ("B-small-attempt1.in", "r", stdin) ;
//	freopen ("b.txt", "w", stdout) ;
	scanf ("%d", &T) ;
	while (T--)
	{
		vnum = 0 ;
		scanf ("%d%d", &c, &d) ;
		FOR(i,0,c)
		{
			scanf ("%d%d", &p[i], &v[i]) ;
			vnum += v[i] ;
		}
		printf ("Case #%d: %lf\n", nCase++, work()) ;
	}
	return 0 ;
}

