#include <stdio.h>

FILE *in , *out ; 


int testcase ; 
int r, k, n ;
int g[10000 ] ; 
int a[ 10000 ];
int b[ 10000 ] ; 

int v[ 10000 ] ; 

int cn = 0 ; 
int c[ 10000 ] ; 
int d[ 10000 ] ; 
__int64 summ[10000 ] ; 
int main()
{
	in = fopen("input.txt","r");
	out = fopen("output.txt","w");

	fscanf(in,"%d",&testcase ) ;
	for ( int tk = 1 ; tk <= testcase ; tk ++ ) 
	{
		fscanf(in,"%d %d %d",&r,&k,&n) ; 
		for ( int i = 0 ; i < n ; i ++ ) 
			fscanf(in,"%d",&g[i]);
		for ( int i = 0 ; i < n ; i ++ ) 
		{
			int sum = 0, j=i ; 
			a[i]=b[i] = -1 ; 
			for ( int q = 0 ; q < n ; q ++ ) 
			{
				if ( sum+g[j] > k )
				{
					a[i] = sum ; 
					b[i] = j ; 
					break;
				}
				sum += g[j] ; 					
				j++;
				if ( j >= n ) j -= n ;
			}
			if ( a[i] == -1 ) 
			{
				a[i] = sum ; 
				b[i] = j ; 
			}
		}

/*
		for ( int i = 0 ; i < n ; i ++ ) 
			printf("(%d , %d)\n",a[i],b[i]);
		printf("****\n");
*/

		for ( int i = 0 ; i< n ; i ++ ) 
			v[i] = 0 ; 

		cn = 0 ;
		
		int now = 0 ; 
		while(1)
		{
			if ( v[now] == 1 )
				break;
			c[ cn ] = now ; 
			d[ cn ] = a[now];
			v[now] = 1 ; 

			now = b[now] ; 
			cn ++ ; 
		}
/*
		for ( int i = 0 ; i < n ; i ++ ) 
			printf("(%d , %d)\n",c[i],d[i]);
		printf("----\n");
*/

		int nowk ;
		for ( int i = 0 ; i < cn ; i ++ ) 
		{
			if ( c[i] == now ) 
			{
				nowk = i ; 
			}
			if ( i == 0 ) summ[i] = d[i] ; 
			else summ[i] = summ[i-1]+d[i] ; 
		}



		__int64 result ;
		
		if ( nowk >= r-1 ) 
			result = summ[r-1] ;  
		else
		{
			result = summ[nowk-1];

			r -= nowk ; 

			result +=(        (summ[cn-1]-summ[nowk-1])*(r/(cn-nowk))     ) + (    summ[nowk-1+(r%(cn-nowk))]-summ[nowk-1]   ) ;
		}

		fprintf(out,"Case #%d: %I64d\n",tk,result);

	}
	return 0 ; 
}