#include<stdio.h>
#include<memory.h>
const int MAXN = 1000 + 1;

int gcd( int a,int b )
{
    if( b == 0 )
        return a;
    return gcd( b, a%b );
}
int main()
{
    int t,ncase;
    t = ncase = 0;
	freopen( "B-small-attempt1.in", "r", stdin);
	freopen( "B-small-attempt0.out", "w", stdout);
    scanf( "%d",&ncase );
    while( ncase-- )
    {
       t++; 
       int n;
       int g;
	   int data[3];
	   
	   if( t == 3 )
		   t = t;
       scanf( "%d",&n );
       scanf( "%d", &g);
       int tmp = g;
	   int j,i;
       for( i=0,j=0;i<n-1;i++,j++ )
       {
           scanf("%d",&data[j]);
		   if( data[j] > g ) 
			   data[j] -=  g;
		   else if( data[j] < g )
			   data[j] = g - data[j];
		   else if( data[j] == g )
			   j--;
       }
       g = data[0];
       for( i = 0 ; i < j ; i++ )
           g = gcd( g, data[i] );
	   int res = tmp % g;
	   if( res != 0 )
		   res = g - res;
       printf( "Case #%d: %d\n", t, res );
    }
    return 0;
}
