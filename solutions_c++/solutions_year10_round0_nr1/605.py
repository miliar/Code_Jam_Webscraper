#include <iostream>
#include <bitset>
#include <cstdlib>
using namespace std;

int main()
{
	int		t = 0 ;
	int		n = 0 ;
	int		k = 0 ;
	
	
	cin >> t ;
	for( int casenum = 1 ; casenum <= t ; casenum++ )
	{
		cin >> n >> k ;
		
		if( k%(1<<n)+1 == 1<<n )
		{
			cout << "Case #" << casenum << ": ON" << endl ;
		}
		else
		{
			cout << "Case #" << casenum << ": OFF" << endl ;
		}
	}
	
	return 0 ;
}
