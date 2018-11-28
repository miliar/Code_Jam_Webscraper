#include <stdio.h>

FILE *in , *out ; 
long long pow2[40 ] ; 
int main()
{
	int testcase ; 
	in = fopen("input.txt","r");
	out = fopen("output.txt","w");
	fscanf(in,"%d",&testcase);

	pow2[0] = 1 ;
	for ( int i = 1 ; i <= 30 ; i ++ ) 
	{
		pow2[i] = pow2[i-1] *2 ;
		//printf("%d\n",pow2[i]);
	}
	for( int tk = 1 ;  tk <= testcase ; tk ++ ) 
	{
		int n , k ;
		fscanf(in,"%d %d",&n,&k);
	
		if ( k % pow2[n] == pow2[n]-1 )
			fprintf(out,"Case #%d: ON\n",tk);
		else
			fprintf(out,"Case #%d: OFF\n",tk);
	}
	return 0;
}