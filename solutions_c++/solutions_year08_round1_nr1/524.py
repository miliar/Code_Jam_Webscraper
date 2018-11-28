#include <stdio.h>
#include <algorithm>
#include <vector>
#include <functional>
using namespace std;
int main ()
{
	freopen( "A-large.in" , "r" , stdin );
	freopen( "out" , "w" , stdout );
	int T , i , j , test = 0 , n;
	scanf( "%d" , & T );
	while( T -- ) 
	{
		test++;
		scanf ( "%d" , &n );
		vector <long long> a(n) , b(n);
		for(i = 0; i < n; i++) 
			scanf ("%I64d" , &a[i] );
		for(i = 0; i < n; i++)
			scanf( "%I64d" , &b[i]);
		sort( a.begin() , a.end() );
		sort( b.begin() , b.end() , greater<long long>() );
		long long res = 0;
		for(i = 0; i < n; i++)
			res += a[i] * b[i];
		printf( "Case #%d: %I64d\n" ,test ,  res  );
	}
	return 0;
}