# include <cstdio>
# include <cstdlib>
# include <vector>
# include <set>
# include <map>
# include <deque>
# include <algorithm>
# include <cctype>
# include <iostream>
# include <cstring>
# include <fstream>

# define FR(i, n)           for( int i = 0; i < n; i++)
# define FRin(i, m, n)     for( int i = m; i < n; i++)
# define FRrev(i, n)         for( int i = n; i >= 0; i-- )
# define PF    printf
# define SF    scanf
# define PB    push_back

using namespace std;

int main()
{
	int test;
	SF ( "%d", &test);
	
	ofstream out ( "out3s.txt", ios::out );
	FRin ( testi, 1, test + 1)
	{
		int n;
		SF ( "%d", &n);
		int min = 1;
		min <<= 30;
		int rxor = 0;
		int sum = 0;
		FR ( i, n)
		{
			int ci;
			SF ( "%d" , &ci );
			rxor ^= ci;
			if ( ci < min ) min = ci;
			sum += ci;
		}
		
		if ( rxor == 0 )
		{
			PF ( "Case #%d: %d\n", testi, sum - min );
			out << "Case #" << testi << ": " << sum - min << endl;
		}
		else
		{
			PF ( "Case #%d: NO\n", testi );
			out << "Case #" << testi << ": NO" << endl;
		}
	}
	return 0;
}

