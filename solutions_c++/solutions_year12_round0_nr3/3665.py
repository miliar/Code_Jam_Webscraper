#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <iostream>
#include <vector>
using namespace std;
int main()
{
	int t, a, b, n, m, o, flag, pair;
	char x[7], y[7];
	
	cin >> t;
	for (int i = 1; i <= t; i++ )
	{
		pair = 0;
		
		cout << "Case #" << i << ": ";
		cin >> a >> b;
		for (int j = a ; j <= b ; j++ )
		{
			for (int k = j ; k <= b ; k++ )
			{
				n = sprintf(y, "%d", k);
				sprintf(x, "%d", j);
				
				for (int l = 0; l < n; l++ )
				{
					if ( y[l] == x[0] )
					{
						o = l+1;
						m = 1;
						flag = 1;
						while ( m != n )
						{
							if ( o == n )
							{
								o = 0;
							}
							if ( y[o] != x[m] )
							{
								flag = 0;
								break;
							}
							o++;
							m++;
						}
						
						if ( flag )
						{
							if ( l != 0 )
							{
								pair++;
							}
							break;
						}
					}
				}
			}
		}
		cout << pair << endl;
	}
	return 0;
}