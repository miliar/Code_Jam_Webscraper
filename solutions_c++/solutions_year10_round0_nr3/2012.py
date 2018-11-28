#include<iostream>
#include<stdio.h>
#include<algorithm>
using namespace std ;
#define fo(i, n) for (i=0 ; i <n ; i++)


int next[1001] ;
unsigned long long ret, profit[1001], g[1001] ;

FILE *in = fopen ("input.in", "r") ;
FILE *out = fopen ("output.out", "w") ;


int main()
{
	int t, R, K, N, i, k, z ;
	unsigned long long cur, j ;

	fscanf (in, "%d", &t) ;

	fo(z, t)
	{
		ret = 0 ;
		//cin >> R >> K >> N ;
		fscanf (in, "%d %d %d", &R, &K, &N) ;

		j = 0 ;
		fo(i, N)
		{
			//cin >> g[i] ;
			fscanf (in, "%d", &g[i]) ;
			j+= g[i] ;
		}
		if (j<= K)
			ret = (unsigned long long) R * j ;
		else
		{
			fo(i, N)
			{
				cur = g[i] ;
				j = i+1 ;
				while(1)
				{
					j = j%N ;

					if (cur + g[j] <=K)
						cur+= g[j], j++ ;
					else
						break ;
				}
				next[i] = j ;
				profit[i] = cur ;
			}

			cur = 0 ;
			fo(i, R)
			{
				ret+= profit[cur] ;
				cur = next[cur] ;
			}		
		}

		fprintf (out, "Case #%d: %lld\n", z+1, ret) ;
	}

	return 0 ;
}