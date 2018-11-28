#include <iostream>
#include <cstdlib>
using namespace std;

int main()
{
	const int maxN = 1000 ;
	long long int		t = 0 ;
	
	cin >> t ;
	for( int casenum = 1 ; casenum <= t ; casenum++ )
	{
		long long int		r = 0 ;
		long long int		k = 0 ;
		long long int		n = 0 ;
		long long int		firstGroup = 0 ;
		long long int		EurosMade = 0 ;
		long long int		groups[ maxN ] = { 0 } ;
		long long int		ride[ maxN ] = { 0 } ;
		long long int		nextStart[ maxN ] = { 0 } ;
		
		cin >> r >> k >> n ;
		for( int i = 0 ; i < n ; i++ )
		{
			cin >> groups[ i ] ;
		}
		
		for( int i = 0 ; i < n ; i++ )
		{
			ride[ i ] = groups[ i ] ;
			nextStart[ i ] = (i+1)%n ;
			
			while( ride[ i ] + groups[ nextStart[ i ] ] <= k && 
				nextStart[ i ] != i )
			{
				ride[ i ] += groups[ nextStart[ i ] ] ;
				nextStart[ i ] = (nextStart[ i ]+1)%n ;
			}
		}
		
		for( int i = 0 ; i < r ; i++ )
		{
			EurosMade += ride[ firstGroup ] ;
			firstGroup = nextStart[ firstGroup ] ;
		}
		
		cout << "Case #" << casenum << ": " << EurosMade << endl ;
	}
	
	return 0 ;
}
