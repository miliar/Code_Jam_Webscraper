#include <stdio.h>
#include <vector>

using std::vector;

int main()
{
	static const int max_len = 100;
	int nCases = 0;scanf("%d",&nCases);
	for(int iCases = 1;iCases <= nCases;++iCases)
	{
		vector< vector<int> > cells[2];
		cells[0].resize(max_len);cells[1].resize(max_len);
		for(int i = 0;i < max_len;++i)
		{
			cells[0][i].resize(max_len,0);
			cells[1][i].resize(max_len,0);
		}
		int prev = 0,curr = 1;
		int r = 0;scanf("%d",&r);
		for(int i = 0;i < r;++i)
		{
			int x1 = 0,x2 = 0,y1 = 0,y2 = 0;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for(int x = x1-1;x < x2;++x)
			{
				for(int y = y1-1;y < y2;++y) cells[prev][x][y] = 1;
			}
		}
		bool all_zero = false;
		int ret = 0;
		for(;!all_zero;++ret)
		{
			all_zero = true;
			for(int x = max_len-1;x >= 0;--x)
			{
				for(int y = max_len-1;y >= 0;--y)
				{
					int& ri = cells[curr][x][y];
					ri = 0;
					bool north = true,west = true;
					if(x == 0) west = false;
					else if(0 == cells[prev][x-1][y]) west = false;

					if(y == 0) north = false;
					else if(0 == cells[prev][x][y-1]) north = false;

					if(west && north) ri = 1;
					else if(!west && !north) ri = 0;
					else ri = cells[prev][x][y];
					all_zero &= (0 == ri);
				}
			}
			prev ^= curr;curr ^= prev;prev ^= curr;
		}
		printf("Case #%d: %d\n",iCases,ret);
	}
	return 0;
}