#include "quiz.h"

void quiz_a::solve()
{
	int T;
	*this >> T;

	int N, K;

	begin_case(T)
	{
		*this >> N >> K;

		if( N == 1 && K == 1 )
		{
			write("ON");
			write_lf();
			continue;
		}

		int t = (int)(pow((long double)2, N));

		while( K - t >= 0 ) K -= t;

		if( K == t - 1 ) write("ON");
		else write("OFF");

		write_lf();
	}
	end_case
}
