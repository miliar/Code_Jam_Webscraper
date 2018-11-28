#include <cstdio>
#include <memory.h>

using namespace std;

int arr[101][101];
int next_arr[101][101];

int sim()
{
	int stage = 0;
	for (;;stage++)
	{
		int i, j;
		int no = true;
		for (i = 1;i <= 100;i++)
		{
			for (j = 1;j <= 100;j++)
			{
				next_arr[i][j] = arr[i][j];
				if (!arr[i][j])
				{
					if (arr[i - 1][j] && arr[i][j - 1])
						next_arr[i][j] = true;
				}
				else
				{
					if (!arr[i - 1][j] && !arr[i][j - 1])
						next_arr[i][j] = false;
					no = false;
				}
			}
		}
		if (no)
			break;
		memcpy(arr, next_arr, sizeof(next_arr));
	}
	return stage;
}

int main()
{
	int tc;
	scanf("%d", &tc);

	int ti;
	int N;
	for (ti = 1;ti <= tc;ti++)
	{
		printf("Case #%d: ", ti);
		scanf("%d", &N);
		int i;
		memset(arr, 0, sizeof(arr));
		for (i = 0;i < N;i++)
		{
			int sx, sy, ex, ey;
			scanf("%d %d %d %d", &sx, &sy, &ex, &ey);
			int x, y;
			for (x = sx;x <= ex;x++)
				for (y = sy;y <= ey;y++)
					arr[x][y] = true;
		}

		int ans = sim();

		printf("%d\n", ans);
	}
	return 0;
}
