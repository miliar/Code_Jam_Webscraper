#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cctype>

using namespace std;
template <class T> T sqr(T a) { return a * a; }

char s[60][60];
int w, h;

int fill(int y, int x, char c)
{
	if (y >= h || x >= w || s[y][x] != '#')
		return 0;
	s[y][x] = c;
	return 1;
}

int main()
{
#ifdef impetus
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int testnum;
	scanf("%d", &testnum);
	for (int tc = 0; tc < testnum; tc++)
	{
		scanf("%d%d", &h, &w);
		for (int i = 0; i < h; i++)
			scanf("%s", s[i]);
		int fail = 0;
		for (int i = 0; i < h; i++)
			for (int j = 0; j < w; j++)
				if (s[i][j] == '#')
				{
					fail |= !fill(i, j, '/');
					fail |= !fill(i, j + 1, '\\');
					fail |= !fill(i + 1, j, '\\');
					fail |= !fill(i + 1, j + 1, '/');
				}
		printf("Case #%d:\n", tc + 1);
		if (fail)
			printf("Impossible\n");
		else
			for (int i = 0; i < h; i++)
				printf("%s\n", s[i]);
	}
	return 0;
}