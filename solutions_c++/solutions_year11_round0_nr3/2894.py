# include <stdio.h>
# include <vector>
# include <stdlib.h>
# include <string>
# include <math.h>
using namespace std;

long long arr[1111] ,n,sum;

long long calc ( long long a , long long b )
{
	long long k = a > b ? a : b ;
	long ret=0LL;
	for ( int i=0 ; i<20 ; i++ )
	{
		if ( a & ( 1<<i ) && b & ( 1<<i ) )
			;
		else if ( a & ( 1<<i ) || b & ( 1<<i ) )
			ret |= ( 1<<i) ;
		else
			;
	}
	return ret;
}

long long solve ( long long ind , long long l , long long r , long long left )
{
	if ( ind == n )
	{
		if ( calc(l,0) == calc(r,0) && left != sum)
			return left ;
		return -1 ;
	}
	return max ( solve (ind+1 , calc(l,arr[ind]) , r , left+arr[ind] ) , solve ( ind+1 , l , calc(r,arr[ind]) , left ) ) ;
}

int main ()
{
	freopen ("in.txt","r",stdin);
	freopen ("out.txt","w",stdout);
	long long tc ; 
	scanf ("%lld",&tc);
	for ( long long k=1 ; k<=tc ; k++ )
	{
		sum=0;
		scanf ("%lld",&n);
		for ( long long i=0 ; i<n ; i++ )
		{
			scanf ("%lld",&arr[i]);
			sum += arr[i] ;
		}
		long long ans = solve ( 0 , 0 , 0 , 0 );
		if ( ans == -1 )
			printf ("Case #%lld: NO\n",k);
		else
			printf ("Case #%lld: %lld\n",k,ans);
	}
	//while(1);
}