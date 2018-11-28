#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <string>
#include <algorithm>
#include <string>
#include <cmath>
using namespace std;




int main( )
{
	freopen( "input.txt", "rt", stdin );
	freopen( "output.txt", "wt", stdout );

	int cases = 0;

	cin >> cases;

	for( int ct = 0; ct < cases; ++ct )
	{
		long long n, pd, pg;
		cin >> n >> pd >> pg;

		cout << "Case #" << ct + 1 << ": ";

		if( pd < 100 && pg == 100 ||
			pd > 0 && pg == 0 ) 
		{
			cout << "Broken" << endl;
			continue;
		}

		if( pd == 0 )
		{
			cout << "Possible" << endl;
			continue;
		}
	
		if( n >= 100 )
		{
			cout << "Possible" << endl;
			continue;
		}


		double rd = pd / 100.0;
	
		bool bFound = false;

		for( int i = 1; i <= n; ++i )
		{
			if( ( i * rd ) == floor( i * rd ) )
			{
				bFound = true;
				break;
			}	
		}

		if( bFound )
		{
	 		cout << "Possible" << endl;
		}
		else
		{
			cout << "Broken" << endl;
		}
	}

	return 0;
}