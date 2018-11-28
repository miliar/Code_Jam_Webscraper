#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std ;


int main()
{
	int i, j, k, l, g, t ;
	int T, R, K, N ;
	int groups[1000] ;

	FILE *in = fopen("test.in", "r") ;
	FILE *out = fopen("test.out", "w") ;

	fscanf(in, "%d", &T) ;
	for(g=1;g<=T;g++)
	{
		fprintf(out, "Case #%d: ", g) ;
		fscanf(in, "%d%d%d", &R, &K, &N) ;
		for(i=0;i<N;i++)	fscanf(in, "%d" ,&groups[i]) ;

		i = 0 ;
		j = 0 ;
		l = 0 ;
		while( j<R )
		{
			k = 0 ;
			t = i ;
			while( 1 )
			{
				if( k + groups[i] > K ) break ;
				k += groups[i] ;
				i = (i+1)%N ;
				if( t == i ) break ;
			}
			j++ ;
			l += k ;
		}

		fprintf(out, "%d\n", l) ;
	}

	return 0 ;
}
