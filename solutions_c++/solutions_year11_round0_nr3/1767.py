#include<iostream>
#include<vector>
#include<set>
#include<map>
using namespace std;


int main()
{
	freopen( "data_in.txt" , "r" , stdin );
	freopen( "data_out.txt" , "w" , stdout );

	int T , N;

	cin >> T;

	for( int t = 1 ; t <= T ; t ++ )
	{
		cout << "Case #" << t << ": ";

		cin >> N;

		vector<int> candy( N ); 
		for( int n = 0 ; n < N ; n ++ )
			cin >> candy[ n ];

		int total_sum = 0;
		for( int n = 0 ; n < N ; n ++ )
			total_sum ^= candy[ n ]; 

		if( total_sum != 0 )
			cout << "NO\n";
		else
		{
			total_sum = candy[ 0 ];
			int min = candy[ 0 ];
			for( int n = 1 ; n < N ; n ++ )
			{
				total_sum += candy[ n ];
				if( candy[ n ] < min )
					min = candy[ n ];
			}
			cout << total_sum - min << "\n";
		}
	}

	return 0;
}