#include <vector>
#include <string>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <stdlib.h>
using namespace std;

int xdir[] = {0, 0, -1, 1, 0};
int ydir[] = {0, -1, 0, 0, 1};

int main()
{
	int t;
	cin >> t;
	for(int i = 0; i < t; ++i)
	{
		int h, w;
		cin >> h >> w;
		unsigned map[128][128];
		char bestdirs[128][128];
		char basinmap[128][128];
		memset(map, 0xff, sizeof(map));
		memset(bestdirs, 0xff, sizeof(bestdirs));
		memset(basinmap, 0xff, sizeof(basinmap));

		for(int y = 1; y <= h; ++y)
		{
			for(int x = 1; x <= w; ++x)
			{
				int v;
				cin >> v;
				map[y][x] = v;
			}
		}

		vector<char> basins;
		vector<pair<int, int> > queue;

		for(int y = 1; y <= h; ++y)
		{
			for(int x = 1; x <= w; ++x)
			{
				unsigned best = ~0;
				unsigned bestdir = 0;
				for(int j = 0; j < 5; ++j)
				{
					if(map[y + ydir[j]][x + xdir[j]] < best)
					{
						best = map[y + ydir[j]][x + xdir[j]];
						bestdir = j;
					}
				}

				bestdirs[y][x] = bestdir;
				if(!bestdir)
				{
					queue.push_back(make_pair(x, y));
					basinmap[y][x] = basins.size();
					basins.push_back(0);
				}
			}
		}

		while(!queue.empty())
		{
			pair<int, int> p = queue.back();
			int x = p.first;
			int y = p.second;
			queue.pop_back();
			for(int i = 1; i < 5; ++i)
			{
				if(bestdirs[y - ydir[i]][x - xdir[i]] == i)
				{
					basinmap[y - ydir[i]][x - xdir[i]] = basinmap[y][x];
					queue.push_back(make_pair(x - xdir[i], y - ydir[i]));
				}
			}
		}

		char next_basin = 'a';

		cout << "Case #" << (i + 1) << ':' << endl;
		for(int y = 1; y <= h; ++y)
		{
			for(int x = 1; x <= w; ++x)
			{
				int b = basinmap[y][x];
				if(b < 0)
				{
					cerr << x << ' ' << y << endl;
					abort();
				}
				if(!basins[b])
					basins[b] = next_basin++;
				if(x > 1)
					cout << ' ';
				cout << basins[b];
			}
			cout << endl;
		}
	}
	return 0;
}
