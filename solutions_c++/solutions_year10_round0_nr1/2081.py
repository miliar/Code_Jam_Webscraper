#include<stdio.h>
#include<algorithm>
using namespace std ;
#define fo(i, n) for (i=0 ; i<n ; i++)


FILE *in = fopen ("input.in", "r") ;
FILE *out = fopen ("output.out", "w") ;


int main()
{
	int z, t, n, k, r ;

	fscanf (in, "%d", &t ) ;

	fo(z, t)
	{
		fscanf (in, "%d %d", &n, &k) ;

		k++ ;

		r = (1<<n) ;

		fprintf (out, "Case #%d: ", z+1) ;

		if (k%r)
			fprintf (out, "OFF\n") ;
		else
			fprintf (out, "ON\n") ;
	}

	return 0 ;
}