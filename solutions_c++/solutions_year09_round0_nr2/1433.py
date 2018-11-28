#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <iostream>
#include <sstream>
#include <fstream>
#define _USE_MATH_DEFINES
#include <math.h> 

using namespace std;

char dfs(vector<vector<int> > const & alts, int h, int w, vector<vector<char> > & dmap, char c)
{
	if (dmap[h][w] != 0)
		return dmap[h][w];

	int dirh[] = {-1, 0, 0, 1};
	int dirw[] = {0, -1, 1, 0};
	int dir = -1;
	int alt = alts[h][w];
	for (int i = 0; i < 4; ++i)
	{
		int newh = h + dirh[i];
		int neww = w + dirw[i];
		if (newh >= 0 && newh < (int)alts.size() && neww >= 0 && neww < (int)alts[0].size())
			if (alts[newh][neww] < alt)
			{
				alt = alts[newh][neww];
				dir = i;
			}
	}
	if (dir == -1)
		dmap[h][w] = c;
	else
		dmap[h][w] = dfs(alts, h + dirh[dir], w + dirw[dir], dmap, c);
	return dmap[h][w];
}

int main()
{
	ifstream ifstr("B-large.in");
	int T, H, W;
	ifstr >> T;

	ofstream ofstr("B-large.out");
	for (int i = 0; i < T; ++i)
	{
		ifstr >> H >> W;

		vector<vector<int> > alts(H, vector<int>(W, 0));
		for (int j = 0; j < H; ++j)
			for (int k = 0; k < W; ++k)
				ifstr >> alts[j][k];

		vector<vector<char> > dmap(H, vector<char>(W, 0));
		char c = 'a';
		for (int j = 0; j < H; ++j)
			for (int k = 0; k < W; ++k)
				if (dfs(alts, j, k, dmap, c) == c)
					++c;

		ofstr << "Case #" << i + 1 << ":\n";
		for (int j = 0; j < H; ++j)
		{
			for (int k = 0; k < W; ++k)
				ofstr << dmap[j][k] << ' ';
			ofstr << "\n";
		}
	}

	return 0;
}
