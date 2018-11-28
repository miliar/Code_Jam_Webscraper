#include <iostream>

using namespace std;

int main()
{
	freopen( "B-large.in", "rt", stdin );
	freopen( "B-large-output.txt", "wt", stdout );

	int T = 0;
	cin >> T;

	for( int i = 0; i < T; i++ )
	{
		int N = 0;
		cin >> N;

		int S = 0;
		cin >> S;

		int p = 0;
		cin >> p;

		double t[110] = {0};
		for( int j = 0; j < N; j++ )
		{
			cin >> t[j];
		}

		int count = 0;
		for( int j = 0; j < N; j++ )
		{
			if( t[j] / 3 >= p )
			{
				count++;
				continue;
			}

			int a = ceil( (t[j] - p)/2 );
			int b = floor( (t[j] - p)/2 );

			if( ( p - b > 2 ) || a < 0 || b < 0 )
				continue;

			if( p - b == 2 )
			{
				if( S >= 1 )
				{
					S--;
					count++;
				}
			}

			if( p - b < 2 )
				count++;
		}

		cout << "Case #" << i+1 << ": " << count << endl;
	}

	return 0;
}