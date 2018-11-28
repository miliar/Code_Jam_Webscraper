#include <vector>
// #include <algorithm>

#include <cstdio>

using namespace std;

#define ITERATE(it, x) for(__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)

int main()
{
	int T;
	scanf("%d", &T);
	for (int idxCase = 0; idxCase < T; ++idxCase)
	{
		int R;
		scanf("%d", &R);
		vector<int> R1s(R), C1s(R), R2s(R), C2s(R);
		for (int i = 0; i < R; ++i)
			scanf("%d%d%d%d", &C1s[i], &R1s[i], &C2s[i], &R2s[i]);
		int rows = 0;
		int cols = 0;
		for (int i = 0; i < R; ++i)
		{
			if (rows < R2s[i] + 1)
				rows = R2s[i] + 1;
			if (cols < C2s[i] + 1)
				cols = C2s[i] + 1;
		}
		vector<vector<bool> > grid(rows);
		ITERATE (it, grid) it->assign(cols, false);
		long long numBac = 0;
		for (int i = 0; i < R; ++i)
		{
			for (int r = R1s[i]; r <= R2s[i]; ++r)
			{
				for (int c = C1s[i]; c <= C2s[i]; ++c)
				{
					if (!grid[r][c])
					{
						grid[r][c] = true;
						++numBac;
					}
				}
			}
		}
		long long clock = 0;
		while (numBac != 0)
		{
			vector<vector<bool> > newGrid = grid;
			for (int r = 1; r < rows; ++r)
			{
				for (int c = 1; c < cols; ++c)
				{
					if (grid[r][c])
					{
						if (!grid[r - 1][c] && !grid[r][c - 1])
						{
							newGrid[r][c] = false;
							--numBac;
						}
					}
					else
					{
						if (grid[r - 1][c] && grid[r][c - 1])
						{
							newGrid[r][c] = true;
							++numBac;
						}
					}
				}
			}
			swap(grid, newGrid);
			++clock;
		}
    	printf("Case #%d: %lld\n", idxCase + 1, clock);
	}
	return 0;
}
