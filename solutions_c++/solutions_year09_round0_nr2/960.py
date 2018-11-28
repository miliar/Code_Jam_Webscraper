#include <cstdio>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

int h, w;
pair<int, int> area[300][300];
map<int, char> area_name;

int find_rep(int y, int x)
{
	int y1 = area[y][x].second / w;
	int x1 = area[y][x].second % w;

	if (y1 == y && x1 == x)
	{
		return area[y][x].second;
	}

	area[y][x].second = find_rep(y1, x1);
	return area[y][x].second;
}

void uni(int a, int b)
{
	int y = b / w;
	int x = b % w;

	area[y][x].second = a;
}

void try_uni(int ya, int xa, int yb, int xb)
{
	int rep_a = find_rep(ya, xa);
	int rep_b = find_rep(yb, xb);

	if (rep_a != rep_b)
	{
		uni(min(rep_a, rep_b), max(rep_a, rep_b));
	}
}

void solve()
{
	area_name.clear();
	int dx[] = { 0,-1, 1, 0};
	int dy[] = {-1, 0, 0, 1};

	for(int y = 0; y < h; ++y)
	{
		for(int x = 0; x < w; ++x)
		{
			int m = area[y][x].first;
			int idx = -1;
			for(int i = 0; i < 4; ++i)
			{
				if (y + dy[i] < 0 || h <= y + dy[i] || x + dx[i] < 0 || w <= x + dx[i])
					continue;
				
				if (m > area[y+dy[i]][x+dx[i]].first)
				{
					m = area[y+dy[i]][x+dx[i]].first;
					idx = i;
				}
			}

			if (idx != -1)
			{
				try_uni(y, x, y+dy[idx], x+dx[idx]);
			}
		}
	}

	char let = 'a';
	for(int y = 0; y < h; ++y)
	{
		for(int x = 0; x < w; ++x)
		{
			int rep = find_rep(y, x);
			if (area_name.find(rep) == area_name.end())
			{
				area_name[rep] = let++;
			}

			printf("%c ", area_name[rep]);
		}
		printf("\n");
	}
}

int main()
{
	//freopen("input.txt", "r", stdin);
	freopen("D:/downloads/B-large.in", "r", stdin);
	freopen("C:/Users/kiheon/Desktop/output.txt", "w", stdout);

	int z;
	scanf("%d", &z);
	for(int i = 0; i < z; ++i)
	{
		scanf("%d%d", &h, &w);
		for(int y = 0; y < h; ++y)
		{
			for(int x = 0; x < w; ++x)
			{
				scanf("%d", &area[y][x].first);
				area[y][x].second = y*w + x;
			}
		}

		printf("Case #%d:\n", i+1);
		solve();
	}
}