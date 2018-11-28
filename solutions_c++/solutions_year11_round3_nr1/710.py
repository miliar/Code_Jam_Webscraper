# include <Stdio.h>


# define FOR(i,a,b) for (int i = a ; i <  b; i++)
int n, m ;
char graph[60][60] ;


int work ()
{
	int num = 0 ;
	FOR(i,0,n) FOR(j,0,m)
		if (graph[i][j] == '#') num++ ;
	if (num % 4 != 0) return 0 ;
	
	while (num)
	{
		FOR(i,0,n)	FOR(j,0,m)
		{
			if (graph[i][j] == '#')
			{
				if (i + 1 >= n) break ;
				if (j + 1 >= m) break ;
				graph[i][j] = '/' ;
				if (graph[i][j+1] != '#') return 0 ;
				graph[i][j+1] = '\\' ;
				if (graph[i+1][j] != '#') return 0 ;
				graph[i+1][j] = '\\' ;
				if (graph[i+1][j+1] != '#') return 0 ;
				graph[i+1][j+1] = '/' ;
				num -= 4 ;
			}
		}
		
	}
	return 1 ;
}

int main ()
{
	int T, nCase = 1 ;
	
	freopen ("A-large (1).in", "r", stdin) ;
	freopen ("a.txt", "w", stdout) ;
	scanf ("%d", &T) ;
	while (T--)
	{
		scanf ("%d%d", &n, &m) ;
		FOR(i,0,n) 
			scanf ("%s", graph[i]) ;
		
		printf ("Case #%d:\n", nCase++) ;
		if (work ()){
			FOR(i,0,n)puts (graph[i]) ;
		}
		else puts ("Impossible") ;
	}
	return 0 ;
}