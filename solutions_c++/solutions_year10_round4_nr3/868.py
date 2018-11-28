#include <iostream>
#include <boost/format.hpp>
#include <stdint.h>

int main(int argc, char *argv[])
{
	int C;

	std::cin >> C;

	int map[200][200] = {};

	for(int c = 0; c < C ; ++c)
	{
		int R;
		std::cin >> R;

		for(int r = 0; r < R; ++r)
		{
			int X1, Y1, X2, Y2;
			std::cin >> X1 >> Y1 >> X2 >> Y2;

			--X1; --Y1; --X2; --Y2;
			
			for(int i = std::min(X1,X2); i < std::max(X1,X2)+1; ++i)
			{
				for(int j = std::min(Y1,Y2); j < std::max(Y1,Y2)+1; ++j)
				{
					map[i][j] = 1;
				}
			}
		}

		uint64_t count = 1;
		while(1)
		{
			bool alive = false;
			for(int i = 0; i < 100; ++i)
			{
				for(int j = 0; j < 100; ++j)
				{
					bool N = false, W = false;
					if(i > 0)
					{
						W = (map[i-1][j] & 1) != 0;
					}
					if(j > 0)
					{
						N = (map[i][j-1] & 1) != 0;
					}

					if((map[i][j] & 1) != 0)
					{
						if(N || W)
						{
							map[i][j] |= 1 << 1;
							alive = true;
						}
					}
					else
					{
						if(N && W)
						{
							map[i][j] |= 1 << 1;
							alive = true;
						}
					}
				}
			}

			if(!alive)
			{
				break;
			}
			else
			{
				count++;
			}


			for(int i = 0; i < 100; ++i)
			{
				for(int j = 0; j < 100; ++j)
				{
					map[i][j] >>= 1;
				}
			}
		}

		std::cout << boost::format("Case #%d: %ld\n") % (c+1) % count;


	}

	return 0;
}