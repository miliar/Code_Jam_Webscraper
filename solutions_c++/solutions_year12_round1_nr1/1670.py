#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <functional>

using namespace std;

int main()
{
	int t;

	cin >> t;

	for ( int ti = 1; ti <= t; ti++ )
	{
		int a, b;
		cin >> a >> b;

		vector<double> p;

		for ( int i = 0; i < a; i++ )
		{
			double input;
			cin >> input;
			p.push_back( input );
		}

		double keymin = 100000 * 5.0;

		double prob = 1.0;
		string typed;

		// keep
		{
			for ( unsigned int i = 0; (int)i < a; i++ )
			{
				prob *= p[i];
			}

			int key1, key2;

			key1 = b - a + 1;
			key2 = ( b - a + 1 ) + ( b + 1 );

			double need1, need2;

			need1 = key1 * prob;
			need2 = key2 * ( 1.0 - prob );

			double min = need1 + need2;

			if ( min < keymin )
			{
				keymin = min;
			}
		}

		// press bs
		{
			for ( unsigned int bs = 1; (int)bs <= a; bs++ )
			{
				double prob = 1.0;

				for ( unsigned int i = 0; i < a - bs; i++ )
				{
					prob *= p[i];
				}

				int key1, key2;

				key1 = b - a + bs * 2 + 1;
				key2 = ( b - a + bs * 2 + 1 ) + ( b + 1 );

				double need1, need2;

				need1 = key1 * prob;
				need2 = key2 * ( 1.0 - prob );

				double min = need1 + need2;

				if ( min < keymin )
				{
					keymin = min;
				}
			}
		}

		// press enter
		{
			double need = b + 2.0;

			if ( need < keymin )
			{
				keymin = need;
			}
		}

		cout << "Case #" << ti << ": ";
		printf("%lf\n", keymin );
	}		
		
	return 0;
}