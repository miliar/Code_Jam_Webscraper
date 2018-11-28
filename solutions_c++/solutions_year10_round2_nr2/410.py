#include<stdio.h>
#include<algorithm>
using namespace std ;
#define fo(i, n) for (i=0 ; i<n ; i++)

FILE *in = fopen ("input.in", "r") ;
FILE *out = fopen ("output.out", "w") ;

int C ;
int V[60] ;
int X[60] ;
int B, T, K, N ;

int main()
{
	fscanf (in, "%d", &C) ;

	int i, z, slow, ret, done ;

	fo(z, C) 
	{
		ret = 0 ;
		slow = 0 ;
		done = 0 ;

		fscanf (in, "%d %d %d %d", &N, &K, &B, &T) ;

		fo(i, N)
			fscanf (in, "%d", &X[i]) ;
		fo(i, N)
			fscanf (in, "%d", &V[i]) ;

		for (i=N-1 ; i>=0 ; i--)
		{
			if (V[i] * T >= B - X[i])
			{
				done++ ;
				ret+= slow ;
			}
			else
				slow ++ ;

			if (done>=K)
				break ;
		}
		fprintf (out, "Case #%d: ", z+1) ;

		if (done>=K)
			fprintf (out, "%d\n", ret) ;
		else
			fprintf (out, "IMPOSSIBLE\n") ;

	}	

	return 0 ;
}