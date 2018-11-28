#include <stdio.h>

FILE *in , *out ;  

int gcd( int x, int y ) 
{
	while(1)
	{
		if ( y == 0 ) 
			return x ;
		int temp = x%y ;
		x = y ;
		y = temp ; 
	}
}
int main()
{
	int testcase ; 
	in = fopen("input.txt","r");
	out = fopen("output.txt","w");
	fscanf(in,"%d",&testcase);
  
	int n ;
	int a[ 1010 ] ;
	int f ; 

	for ( int tk = 1 ; tk <= testcase ; tk ++ ) 
	{
		int result = 0 ;
		fscanf(in,"%d",&n);
		for ( int i = 0 ; i< n ; i ++ ) 
			fscanf(in,"%d",&a[i]);

		int temp ;
		for ( int i = 0 ; i < n-1 ; i ++ ) 
			for ( int j = i+1 ; j < n ; j ++ ) 
			{
				if ( a[i] > a[j] ) 
				{
					temp =a[i];
					a[i] = a[j] ; 
					a[j] = temp ; 
				}
			}
		temp = a[1]-a[0] ; 
		for ( int i = 0 ; i < n-2 ; i ++ ) 
		{
			temp= gcd(temp,a[i+2]-a[i+1]) ;  
		}
		result = temp -  a[0]%temp ;
		if ( result == temp ) result = 0 ;

		fprintf(out,"Case #%d: %d\n",tk ,result) ;
	}
	return 0;
}