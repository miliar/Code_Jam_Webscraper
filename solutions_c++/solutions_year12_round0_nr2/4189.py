
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int numberOfCases;
	cin >> numberOfCases;

	for ( int nc = 0; nc < numberOfCases; nc++ )
	{
		int n, s, p;
		cin >> n >> s >> p;
		int num = 0, q = 0;
		for ( int j = 0; j < n; j++ )
		{
			int k;
			cin >> k;

			if ( k == 0 )
			{
				if ( p == 0 )
					num++;
			}
			else
			{
				if ( k%3 == 0 )
				{
					if ( k/3 >= p )
						num++;
					else
						if ( k/3+1 >= p )
							q++;
				}
				if ( k%3 == 2 )
				{
					if ( k/3 + 1 >= p )
						num++;
					else
						if ( k/3 + 2 >= p )
							q++;
				}
				if ( k%3 == 1 )
				{
					if ( k/3+1 >= p )
						num++;
				}
			}
		}

		num += min (s, q);

		cout << "Case #" << nc+1 << ": " << num << "\n";
	}

	return 0;
} 