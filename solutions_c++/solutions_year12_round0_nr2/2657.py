#include <iostream>
#include <vector>

using namespace std;

int main( void )
{
	int T;
	cin >> T;

	for( int count = 0; count < T; count++ )
	{
		int N;
		int S;
		int p;
		vector<int> ti;
		int result = 0;

		cin >> N;
		cin >> S;
		cin >> p;

		for( int n = 0; n < N; n++ )
		{
			int t;
			cin >> t;
			ti.push_back(t);
		}
		sort( ti.begin(), ti.end() );

//		for( int i = 0; i < ti.size(); i++ )
//			cout << ti[i] << " ";
//		cout << endl;

//		cout << "S = " << S << endl;
//		cout << "p = " << p << endl;

		for( int i = 0; i < ti.size(); i++ )
		{
			if( S != 0 )
			{
				if( 
					( ti[i] % 3 == 2 && ti[i] >= 2 && ( ti[i] + 4 ) / 3 >= p ) ||
					( ti[i] % 3 == 1 && ti[i] >= 4 && ( ti[i] + 2 ) / 3 >= p ) ||
					( ti[i] % 3 == 0 && ti[i] >= 3 && ( ti[i] + 3 ) / 3 >= p ))
				{
					result++;
					S--;
				}
			}
			else
			{
				if( ti[i] % 3 == 2 && ( ti[i] + 1 ) / 3 >= p )
						result++;

				if( ti[i] % 3 == 1 && ( ti[i] + 2 ) / 3 >= p )
						result++;

				if( ti[i] % 3 == 0 && ti[i] / 3 >= p )
						result++;
			}
		}

		cout << "Case #" << count + 1 << ": " << result << endl;
	}

	return EXIT_SUCCESS;
}