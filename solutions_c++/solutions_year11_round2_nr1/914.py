# include <stdio.h>


# define FOR(i,a,b) for (int i = a ; i < b ; i++)


double WP[110], OWP[110], OOWP[110] ;
double RPI[110] ;
int n ;
int graph[110][110] ;


void wp()
{
	int cnt ;
	double sum ;
	FOR(i, 0, n)
	{
		cnt = 0 ;
		sum = 0 ;
		FOR(j, 0,n)
		{
			if (graph[i][j] == -1) continue ;
			sum += graph[i][j] ;
			cnt ++ ;
		}
		WP[i] = sum / cnt ;
	}
}

double wp2(int col, int num)
{
	double sum = 0 ;
	int cnt = 0 ;
	FOR(i,0,n)
	{
		if (i == num) continue ;
		if (graph[col][i] == -1) continue ;
		sum += graph[col][i] ;
		cnt ++ ;
	}
	return sum / cnt ;
}


void owp()
{
	double sum ;
	int cnt ;
	
	FOR(i,0,n)
	{
		cnt = 0 ;
		sum = 0 ;
		FOR(j,0,n){
			if (j == i) continue ;
			if (graph[i][j] == -1) continue ;
			sum += wp2(j, i) ;
			cnt ++ ;
		}
		OWP[i] = sum / cnt ;
	}
}

void oowp()
{
	int cnt = 0 ;
	double sum = 0 ;
	
	FOR(i,0,n)
	{
		cnt = 0 ;
		sum = 0 ;
		FOR(j, 0, n)
		{
			if (graph[i][j] == -1) continue ;
			sum += OWP[j] ;
			cnt++ ;
		}
		OOWP[i] = sum / cnt ;
	}
}



void rpi()
{
	FOR(i,0,n)
		RPI[i] = 0.25 * WP[i] + 0.5*OWP[i] + 0.25*OOWP[i] ;
}

void work ()
{
	wp () ;
	owp() ;
	oowp() ;
	rpi() ;
}

int value(char c)
{
	if (c == '.') return -1 ;
	if (c == '1') return 1 ;
	return 0 ;
}
int main ()
{
	int T ;
	int nCase = 1 ;
	char str[110] ;
	
	freopen ("A-large.in", "r", stdin) ;
	freopen ("a.txt", "w", stdout) ;
	scanf ("%d", &T) ;
	getchar () ;
	while (T--)
	{
		scanf ("%d", &n) ;
		getchar () ;
		FOR(i,0,n)
		{
			scanf ("%s", str) ;
			getchar () ;
			FOR(j,0,n) graph[i][j] = value(str[j]) ;	
		}
		work () ;
		printf ("Case #%d:\n", nCase++) ;
		
		FOR(i,0,n)
			printf ("%lf\n", RPI[i]) ;
	}
}
