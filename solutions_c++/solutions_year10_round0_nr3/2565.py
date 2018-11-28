#include <iostream>
#include <iterator>
#include <boost/format.hpp>
#include <cstdint>

int main(int argc, char *argv[])
{
	int T;

	std::cin >> T;
	for(int c = 0; c < T; ++c)
	{
		int R, k, N;
		std::vector<int> g;

		std::cin >> R >> k >> N;

		g.resize(N);

		std::copy_n(std::istream_iterator<int>(std::cin), N, g.begin());

		int64_t money = 0;
		int steps = 0;

		do
		{
			int pos = 0;
			while(pos != N)
			{
				int t = k;
				int start = pos;
				while(t >= g[pos])
				{
					t -= g[pos];
					money += g[pos];

					++pos;

					if(pos == N)
					{
						if(t < g[0])
						{
							break;
						}
						else
						{
							pos = 0;
						}
					}

					if(pos == start)
					{
						break;
					}
				}

				if(++steps == R)
				{
					break;
				}
			}

			if(pos == N)
			{
				int repeat = R/steps;
				money *= repeat;
				steps *= repeat;				
			}
		} while(steps < R);

		std::cout << boost::format("Case #%d: %ld\n") % (c+1) % money;
	}

	return 0;
}