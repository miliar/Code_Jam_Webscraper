#include <cstdio>
#include <vector>
#include <stack>

#define HMAX 100
#define WMAX 100
#define ALTMAX 10000

using namespace std;

int flow_dir(const int altitude[HMAX + 2][WMAX + 2], int r, int c)
{
	static const int dr[4] = {-1, 0, 0, 1};
	static const int dc[4] = {0, -1, 1, 0};

	int best_alt = altitude[r][c];
	int best_dir = -1;
	for (int dir = 0; dir < 4; ++dir)
	{
		if (altitude[r + dr[dir]][c + dc[dir]] < best_alt)
		{
			best_alt = altitude[r + dr[dir]][c + dc[dir]];
			best_dir = dir;
		}
	}
	return best_dir;
}

int main()
{
	int cMaps;
	scanf("%d", &cMaps);
	for (int idx = 0; idx < cMaps; ++idx)
	{
		int h, w;
		scanf("%d%d", &h, &w);
		int altitude[HMAX + 2][WMAX + 2];
		for (int j = 1; j <= w; ++j)
			altitude[0][j] = ALTMAX + 1;
		for (int j = 1; j <= w; ++j)
			altitude[h + 1][j] = ALTMAX + 1;
		for (int i = 1; i <= h; ++i)
			altitude[i][0] = ALTMAX + 1;
		for (int i = 1; i <= h; ++i)
			altitude[i][w + 1] = ALTMAX + 1;
		for (int i = 1; i <= h; ++i)
		{
			for (int j = 1; j <= w; ++j)
				scanf("%d", &altitude[i][j]);
		}
		int dcell[4];
		dcell[0] = -w;
		dcell[1] = -1;
		dcell[2] = 1;
		dcell[3] = w;
		vector<int> neighbors(h * w, 0);
		for (int i = 0; i < h; ++i)
		{
			for (int j = 0; j < w; ++j)
			{
				int cell = i * w + j;
				int dir = flow_dir(altitude, i + 1, j + 1);
				if (dir >= 0)
				{
					neighbors[cell] |= 1 << dir;
					neighbors[cell + dcell[dir]] |= 1 << (3 - dir);
				}
			}
		}
		vector<int> component(h * w, -1);
		int components = 0;
		for (int i = 0; i < h * w; ++i)
		{
			if (component[i] >= 0)
				continue;
			stack<int> s;
			component[i] = components;
			s.push(i);
			while (!s.empty())
			{
				int t = s.top();
				s.pop();
				for (int dir = 0; dir < 4; ++dir)
				{
					if ((neighbors[t] & (1 << dir)) && component[t + dcell[dir]] < 0)
					{
						component[t + dcell[dir]] = components;
						s.push(t + dcell[dir]);
					}
				}
			}
			++components;
		}
		printf("Case #%d:\n", idx + 1);
		for (int i = 0; i < h * w; ++i)
		{
			putchar('a' + component[i]);
			putchar((i + 1) % w == 0 ? '\n' : ' ');
		}
	}
	return 0;
}
