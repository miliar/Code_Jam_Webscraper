#include <stdio.h>
#include <vector>
#include <map>

using namespace std;

vector<vector<pair<int,int> > > uf;

pair<int,int> directions[4] = {make_pair(-1,0),
									make_pair(0,-1),
									make_pair(0,1),
									make_pair(1,0)
									};

void uf_union(pair<int,int> p1, pair<int,int> p2)
{
	uf[p1.first][p1.second] = p2;
}

pair<int,int> uf_find(pair<int,int> p)
{
	if (uf[p.first][p.second] == p)
		return p;
	pair<int,int> res = uf_find(uf[p.first][p.second]);
	uf[p.first][p.second] = res;
	return res;
}

vector<vector<int> > grid;

int main()
{
	FILE *in = fopen("B-large.in", "r");
	FILE *out = fopen("B.out", "w");

	int t;
	fscanf(in, "%d", &t);

	for(int casenum = 1; casenum <= t; casenum++)
	{
		int h,w;
		fscanf(in, "%d %d", &h, &w);

		uf.clear();
		grid.clear();
		for(int i = 0; i < h; i++)
		{
			uf.push_back(vector<pair<int,int> >());
			grid.push_back(vector<int>());

			for(int j = 0; j < w; j++)
			{
				uf.back().push_back(make_pair(i,j));

				int val;
				fscanf(in, "%d", &val);
				grid.back().push_back(val);
			}
		}

		for(int i = 0; i < h; i++)
		{
			for(int j = 0; j < w; j++)
			{
				int best = -1;
				int minalt = 100000000;
				
				for(int k = 0; k < 4; k++)
				{
					int ni = i + directions[k].first;
					int nj = j + directions[k].second;
					if (ni >= 0 && ni < h && nj >= 0 && nj < w)
					{
						if (grid[ni][nj] < minalt)
						{
							best = k;
							minalt = grid[ni][nj];
						}
					}
				}

				if (minalt < grid[i][j])
				{
					uf_union(make_pair(i,j), make_pair(i+directions[best].first, j+directions[best].second));
				}
			}
		}

		map<pair<int,int>,char> labels;

		fprintf(out, "Case #%d:\n", casenum);

		for(int i = 0; i < h; i++)
		{
			for(int j = 0; j < w; j++)
			{
				if (!labels.count(uf_find(make_pair(i,j))))
				{
					labels[uf_find(make_pair(i,j))] = labels.size() + 'a';
				}

				fprintf(out, "%c ", labels[uf_find(make_pair(i,j))]);
			}
			fprintf(out, "\n");
		}
	}
}
