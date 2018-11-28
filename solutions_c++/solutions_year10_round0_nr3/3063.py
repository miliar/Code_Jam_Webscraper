#include "quiz.h"

void quiz_c::solve()
{

	int T;
	*this >> T;

	int R, K, n;

	std::vector< int > people;

	begin_case(T)
	{
		*this >> R >> K >> n;

		read_vector( n, people );

		int c = 0;
		int cost = 0;

		for( int i = 0; i < R; ++i )
		{
			int rider = 0;

			for( int j = 0; j < n; ++j )
			{
				if( rider + people[c] > K )
					break;

				rider += people[c++];
				if( c == n ) c = 0;
			}

			cost += rider;
		}

		write(cost);
		write_lf();
	}
	end_case

}
