#include <iostream>
#include <cstring>
#include <algorithm>

#include <cmath>

int map[102][102];
int basins[102][102];

char bname[27];

int getbasin(int x, int y)
{
	if (basins[x][y] != 0) return basins[x][y];
	
	int nmin = std::min
	(
		std::min(map[x-1][y], map[x+1][y]), 
		std::min(map[x][y-1], map[x][y+1])
	);
	
	if (map[x][y-1] == nmin) return getbasin(x, y-1);
	if (map[x-1][y] == nmin) return getbasin(x-1, y);
	if (map[x+1][y] == nmin) return getbasin(x+1, y);
	if (map[x][y+1] == nmin) return getbasin(x, y+1);
	
	return 0;
};

int main()
{
	int cases; std::cin >> cases;
	for (int test = 1; test <= cases; ++test)
	{
		std::fill(( int* )map, ( int* )map + 102 * 102, 99999);
		std::fill(( char* )basins, ( char* )basins + 102 * 102, 0);
	
		int w, h; std::cin >> h >> w;
		++w, ++h;
		
		for (int y = 1; y < h; ++y)
		for (int x = 1; x < w; ++x)
			std::cin >> map[x][y];
		
		int cbasin = 0;
		for (int y = 1; y < h; ++y)
		for (int x = 1; x < w; ++x)
		{
			if (
				   (y - 1 == 0 || map[x][y] <= map[x][y - 1])
				&& (y + 1 == h || map[x][y] <= map[x][y + 1])
				&& (x - 1 == 0 || map[x][y] <= map[x - 1][y])
				&& (x + 1 == w || map[x][y] <= map[x + 1][y])
			)
			basins[x][y] = ++cbasin;
		};
		
		for (int y = 1; y < h; ++y)
		for (int x = 1; x < w; ++x)
		basins[x][y] = getbasin(x, y); 
		
		char cn = 'a';
		std::fill(bname, bname + 27, 0);
		
		std::cout << "Case #" << test << ":" << std::endl;
		for (int y = 1; y < h; ++y)
		{	
			for (int x = 1; x < w; ++x)
			{
				int curb = basins[x][y];
				if (bname[curb] == 0) bname[curb] = cn++;
				std::cout << bname[curb] << ' ';
			}
			std::cout << std::endl;
		};
	};
};
