#include <vector>
#include <iostream>
#include <fstream>

int main()
{
	int T, N, S, p, ret;
	std::ifstream file("test.txt");
	std::ofstream file2("result.txt");

	file >> T;
	for(int i = 0; i < T; ++i)
	{
		ret = 0;
		file >> N;
		file >> S;
		file >> p;
		for(int j = 0; j < N; ++j)
		{
			int a = 0;
			file >> a;
			if (a % 3 == 0)
			{
				if(a/3 >= p)
					++ret;

				else if(a/3 + 1 >= p && S > 0 && a != 0)
				{
					++ret;
					--S;
				}

			}

			else if(a % 3 == 1)
			{
				if(a/3 + 1 >= p)
					++ret;

				else if(a/3 + 1 >= p && S > 0)
				{
					++ret;
					--S;
				}
			}

			else
			{
				if(a/3 + 1 >= p)
					++ret;

				else if(a/3 + 2 >= p && S > 0)
				{
					++ret;
					--S;
				}
			}
		}

		file2 << "Case #" << i+1 << ": " << ret << std::endl;
	}
	return 0;
}
