#include <cstdio>
#include <algorithm>

using namespace std;

char f[100][100];

int w, h;

bool eq(int x, int y, char c)
{
	if (x < 0 || y < 0 || x >= w || y >= h) return false;
	return f[y][x] == c;
}

void solve()
{
	scanf("%d%d ", &h, &w);
	for (int i = 0; i < h; i++) gets(f[i]);

	for (int x = 0; x < w; x++)
	{
		for (int y = 0; y < h; y++)
		{
			if (eq(x, y, '#'))
			{
				if (!eq(x+1, y, '#') || !eq(x, y+1, '#') || !eq(x+1, y+1, '#'))
				{
					printf("\nImpossible");
					return;
				}
				f[y][x] = '/';
				f[y][x+1] = '\\';
				f[y+1][x] = '\\';
				f[y+1][x+1] = '/';
			}
		}
	}

	for (int i = 0; i < h; i++) printf("\n%s", f[i]);
	
}

int main()
{
	freopen("1c-a.in", "r", stdin);
	freopen("1c-a.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		printf("Case #%d:", i+1);
		solve();
		printf("\n");
	}
	return 0;
}