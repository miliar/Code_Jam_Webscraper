

#include <vector>
#include <algorithm>
using namespace std;

const int H = 100;
const int W = 100;
int tt, h, w;

int map[H][W];
int res[H][W];

int dir[4][2] = {-1, 0, 0, -1, 0, 1, 1, 0};


bool checksize(int x, int low, int high)
{
	return low <= x && x < high;
}

void dfs(int i, int j, int index)
{
	res[i][j] = index;
	
	int mh = 200000;

	// out
	for	(int t = 0; t < 4; ++t) 
		if (checksize(i+dir[t][0], 0, h) &&
		    checksize(j+dir[t][1], 0, w))
		{
			mh = min(mh, map[i+dir[t][0]][j+dir[t][1]]);
		}

	if(mh < map[i][j])
	{
		for	(int t = 0; t < 4; ++t) 
			if (checksize(i+dir[t][0], 0, h) &&
				checksize(j+dir[t][1], 0, w) &&
				mh == map[i+dir[t][0]][j+dir[t][1]])
			{
				if(res[i+dir[t][0]][j+dir[t][1]] == 0)
					dfs(i+dir[t][0], j+dir[t][1], index);
				break;
			}
	}

	// in
	for	(int t = 0; t < 4; ++t) 
		if (checksize(i+dir[t][0], 0, h) &&
		    checksize(j+dir[t][1], 0, w) &&
		    res[i+dir[t][0]][j+dir[t][1]] == 0 &&
			map[i+dir[t][0]][j+dir[t][1]] > map[i][j]
			)
		{
			int ti = i+dir[t][0];
			int tj = j+dir[t][1];
			int tmh = 200000;
			for	(int tt = 0; tt < 4; ++tt) 
				if (checksize(ti+dir[tt][0], 0, h) &&
					checksize(tj+dir[tt][1], 0, w))
				{
					tmh = min(tmh, map[ti+dir[tt][0]][tj+dir[tt][1]]);
				}
			if (tmh< map[i][j])
				continue;
			for	(int tt = 0; tt < 4; ++tt) 
				if (checksize(ti+dir[tt][0], 0, h) &&
					checksize(tj+dir[tt][1], 0, w) &&
					tmh == map[ti+dir[tt][0]][tj+dir[tt][1]]
					)
				{
					if(ti+dir[tt][0] == i && tj+dir[tt][1] == j)
						dfs(ti, tj, index);
					break;
				}
		}

}

void Work()
{
	memset(res, 0, sizeof(res));
	int index = 1;
	for	(int i = 0; i < h; ++i)
	{
		for (int j = 0; j < w; ++j) if(res[i][j] == 0)
		{
			dfs(i, j, index++);
		}
	}
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &tt);
	for	(int cn = 1; cn <= tt; ++cn)
	{
		scanf("%d%d", &h, &w);
		for	(int i = 0; i < h; ++i)
		{
			for(int j = 0; j < w; ++j)
			{
				scanf("%d", map[i]+j);
			}
		}

		Work();

		// output
		printf("Case #%d:\n", cn);

		for	(int i = 0; i < h; ++i)
		{
			printf("%c", 'a'-1+res[i][0]);
			for(int j = 1; j < w; ++j)
			{
				printf(" %c", 'a'-1+res[i][j]);
			}
			putchar('\n');
		}
	}

	return 0;
}

