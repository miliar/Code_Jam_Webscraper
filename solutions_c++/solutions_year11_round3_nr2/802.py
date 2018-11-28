#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <numeric>
#include <cassert>
using namespace std;





int main(int argc, char* argv[])
{
	freopen( "input.txt", "rt", stdin );
	freopen( "output.txt", "wt", stdout );
	long long cases = 0;
	cin >> cases;

	for( long long ct = 0; ct < cases; ++ct )
	{
		long long N = 0, L = 0, t, C;
		cin >> L >> t >> N >> C;

		vector<long long>  accs;
		vector<bool> hasBooster;

		for( long long i = 0; i < C; ++i )
		{
			long long a = 0;
			cin >> a;
			accs.push_back( a );
		}

		vector<long long> distances;

		long long k = 0;

		for( long long i = 0; i < N; ++i )
		{
			distances.push_back( accs[ k ] );
			 k = ( k + 1 ) % accs.size( );	
		}

		vector<long long> timesFromBeginning( N + 1 );

		timesFromBeginning[ 0 ] = 0;
		
		for( long long i = 1; i <= N;++i )
		{
			timesFromBeginning[ i ] += timesFromBeginning[ i - 1 ] + distances[ i - 1  ];
		}

		long long res = 2 * accumulate( distances.begin( ), distances.end( ), 0 );

		if( L == 1 )
		{
			for( long long i = 0; i < N; ++i )
			{
				hasBooster.clear( );
				hasBooster.resize( N, false );
				hasBooster[ i ] = true;

				long long time = 2 * timesFromBeginning[ i ];

				if( time >= t )
				{
					time += distances[ i ];
				}
				else if( time + distances[ i ] > t )
				{
					long long timeToComplete = t - time;

					long long travelled = timeToComplete / 2;

					assert( timeToComplete % 2 == 0 );

					long long boostTravelled = distances[ i ] - travelled;

					time = time + travelled * 2 + boostTravelled;
				}
				else
				{
					time += 2 * distances[ i ];
				}

				time = time + 2 * ( timesFromBeginning[ N ] - timesFromBeginning[ i + 1 ] );

				res = min( time, res );
			}
		}
		else if( L == 2 )
		{
			for( long long i = 0; i < N; ++i )
			{
				for( long long s = i + 1; s < N; ++s )
				{
					if( i != s )
					{
						long long time = 2 * timesFromBeginning[ i ];

						if( time >= t )
						{
							time += distances[ i ];
						}
						else if( time + distances[ i ] > t )
						{
							long long timeToComplete = t - time;

							long long travelled = timeToComplete / 2;

							assert( timeToComplete % 2 == 0 );

							long long boostTravelled = distances[ i ] - travelled;

							time = time + travelled * 2 + boostTravelled;
						}
						else
						{
							time += 2 * distances[ i ];
						}

						time = time + 2 * ( timesFromBeginning[ s ] - timesFromBeginning[ i + 1 ] );

						if( time >= t )
						{
							time += distances[ s ];
						}
						else if( time + distances[ s ] > t )
						{
							long long timeToComplete = t - time;

							long long travelled = timeToComplete / 2;

							assert( timeToComplete % 2 == 0 );

							long long boostTravelled = distances[ s ] - travelled;

							time = time + travelled * 2 + boostTravelled;
						}
						else
						{
							time += 2 * distances[ s ];
						}


						time = time + 2 * ( timesFromBeginning[ N ] - timesFromBeginning[ s + 1 ] );

						res = min( time, res );
					}
				}
			}
		}

		cout << "Case #" << ct + 1 << ": " << res << endl;
	}

}
