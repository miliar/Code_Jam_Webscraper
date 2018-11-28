# include <stdio.h>

# define MIN(a,b) ((a) < (b) ? (a) : (b))


long long ci[1010] ;
long long dis[1000001] ;


long long l, t, n, c ;
long long sum ;


long long calc (long long a, long long b)
{
	long long tt = 0 , i ;
	
	for (i = 0 ; i < n ; i++)
	{
		if (i != a && i != b) tt += dis[i] * 2 ;
		else
		{
			if (tt >= t) tt += dis[i] ;
			else if (tt + dis[i] * 2 <= t) tt += dis[i] * 2 ;
			else {
				tt += (dis[i] + (t - tt) / 2) ;
			}
		}
	}
	return tt ;
}


long long work ()
{
	long long i, j ;
	long long min = sum ;
	if (l == 0 || t > sum)
	{
		return sum ;
	}
	
	if (l == 1) 
	{
		for (i = 0 ; i < n ; i ++)
		{
			min = calc (i, -1) ;
			sum = MIN(sum, min) ;
		}
		return sum ;
	}
	
	for (i = 0 ; i < n ; i++)
	{
		for (j = i + 1 ; j < n ;j++)
		{
			min = calc (i, j) ;
			sum = MIN(sum, min) ;
		}
	}
	return sum ;
}


int main ()
{
	long long i, T, nCase = 1 ;
	long long pos = 0 ;
	freopen ("B-small-attempt2.in", "r", stdin) ;
	freopen ("B.txt", "w", stdout) ;
	scanf ("%I64d", &T) ;
	while (T--)
	{
		scanf ("%I64d%I64d%I64d%I64d", &l, &t, &n, &c) ;
	//	printf ("%I64d, %I64d, %I64d, %I64d\n", l, t, n, c) ;
		for (i = 0 ; i < c ;i++) scanf ("%I64d", ci+i) ;
		pos = 0 ;
		sum = 0 ;
		for (i = 0 ; i < n ; i++)
		{
			dis[i] = ci[pos++] ;
			sum += dis[i] * 2 ;
			if (pos == c) pos = 0 ; 
		}
		
		
		printf ("Case #%I64d: %I64d\n", nCase++, work ()) ;
	//	printf ("%I64d, %I64d, %I64d, %I64d\n", l, t, n, c) ;
	}
	return 0 ;
}

