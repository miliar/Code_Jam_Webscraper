#include "quiz.h"

void quiz_a::solve()
{
	int T;
	*this >> T;

	begin_case(T)
	{
		int N;
		int inter = 0;
	
		*this >> N;

		vector<int> a, b;

		a.resize(N);
		b.resize(N);

		for( int i = 0; i < N; ++i )
		{
			*this >> a[i] >> b[i];

			for( int j = 0; j < i; ++j )
			{
				if( !((a[i] < a[j] && b[i] < b[j] ) ||
					(a[i] > a[j] && b[i] > b[j] )) )
					++inter;
			}
		}

		write(inter);
		write_lf();		
	}
	end_case
}
