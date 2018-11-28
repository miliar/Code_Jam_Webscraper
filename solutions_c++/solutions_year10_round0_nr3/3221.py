#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;
int main()
{
	int Num_of_Cases;
	scanf_s("%d", &Num_of_Cases);

	for( int i = 0; i < Num_of_Cases; ++i )
	{
		int R, k, N;
		long int Cost = 0;
		scanf_s( "%d %d %d\n", &R, &k, &N );
		std::vector< int > g;
		int g_size;
		for( int j = 0; j < N; ++j )
		{
			std::cin >> g_size;
			g.push_back( g_size );
		}
		
		int rides = 0;
		int current_pos = 0;
		int next_pos = 0;

		while( rides < R )
		{
			int q_size = k;
			int start_pos = current_pos;
			while( q_size > 0 )
			{
				if( g[current_pos] > q_size )
					break;

				q_size = q_size - g[current_pos];
				Cost = Cost + g[current_pos];
				if( current_pos == N-1 )
					next_pos = 0;
				else
					next_pos = current_pos + 1;

				current_pos = next_pos;

				if( current_pos == start_pos )
					break;
			}
			++rides;
		}
		std::cout << "Case #" << i+1 << ": " << Cost << std::endl;
	}

}