#include <iostream>
#include <boost/format.hpp>

struct Line
{
	int A, B;
};

int main(int argc, char *argv[])
{
	int T;

	std::cin >> T;
	
	for(int t = 0; t < T; ++t)
	{
		int N;
		std::cin >> N;
		std::vector<Line> l(N);

		
		for(int i = 0; i < N; ++i)
		{
			std::cin >> l[i].A >> l[i].B;
		}

		int isect = 0;

		for(int i = 0; i < N; ++i)
		{
			for(int j = 0; j < N; ++j)
			{
				if(i == j) continue;

				if(l[i].A < l[j].A && l[i].B > l[j].B)
				{
					++isect;
				}
			}
		}

		std::cout << boost::format("Case #%d: %d\n") % (t+1) % isect;
	}
}