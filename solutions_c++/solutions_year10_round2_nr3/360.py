#include <iostream>
#include <numeric>
using namespace std;

const long long int MODBASE = 100003 ;

long long int nchoosek( int n, int m )
{
	long long int	ans=1;
	if( n<m )
	{
		ans = 0 ;
	}
	else
	{
		for( int i = 0 ; i < m ; i++ )
		{
			ans = (ans*(n-i)/(i+1))%MODBASE;
		}
	}
	
	return ans ;
}

int main()
{
	const int N = 500 ;
	long long int	dp[ N+1 ][ N+1 ] = { 0 };
	int		n = 0 ;
	int		t= 0 ;
	
	for( int i = 2 ; i <= N ; i++ )
	{
		dp[i][1]=1;
		
		for( int j = 2 ; j < i ; j++ )
		{
			for( int k = 1 ; k<j ; k++ )
			{
				dp[ i ][ j ] = ( dp[ i ][ j ] + dp[ j ][ k ]*nchoosek(i-j-1,j-k-1) )%MODBASE ;
			}
		}
	}
	
	cin >> t ;
	for( int cas = 1 ; cas <= t ; cas++ )
	{
		cin >> n ;
		cout << "Case #" << cas << ": " << accumulate( dp[ n ], dp[ n ]+n, (long long int)0 ) % MODBASE << endl ;
	}
	
	return 0 ;
}
