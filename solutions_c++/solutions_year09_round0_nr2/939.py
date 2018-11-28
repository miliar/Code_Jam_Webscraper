#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <algorithm>
#include <cassert>
#include <map>

using namespace std;

const int hmax = 101;
const int dx[] = { -1, 0, 0, 1 };
const int dy[] = { 0, -1, 1, 0 };

int a[hmax][hmax];
int u[hmax][hmax];
char r[hmax][hmax];
int h, w;
map < int, char > color;

int go(int i, int j)
{
	if (u[i][j] != -1) return u[i][j];
	u[i][j] = -2;
	int mind = -1, argmind = 100000;
    for (int d = 0; d < 4; ++d)
    {
    	int x = i + dx[d], y = j + dy[d];
    	if (x >= 0 && x < h && y >= 0 && y < w)
    		if (argmind > a[x][y]) argmind = a[x][y], mind = d;
    }
    if (a[i][j] <= argmind) return (u[i][j] = i*w + j);
    int x = i + dx[mind], y = j + dy[mind];
    assert(x >= 0 && x < h && y >= 0 && y < w && u[x][y] != -2);
    u[i][j] = go(x, y);
    return u[i][j];
}

int main()
{
	int test_cnt;
	cin >> test_cnt;
	for (int test_id = 1; test_id <= test_cnt; ++test_id)
	{
		scanf("%d%d", &h, &w);
		for (int i = 0; i < h; ++i)
			for (int j = 0; j < w; ++j)
				scanf("%d", &a[i][j]), u[i][j] = -1;
		for (int i = 0; i < h; ++i)
			for (int j = 0; j < w; ++j)
				go(i, j);

  		color.clear();
  		char c = 'a';
		for (int i = 0; i < h; ++i)
			for (int j = 0; j < w; ++j)
				if (color.count(u[i][j]) == 0) color[u[i][j]] = c++;
		for (int i = 0; i < h; ++i)
			for (int j = 0; j < w; ++j)
				r[i][j] = color[u[i][j]];

		printf("Case #%d:\n", test_id);
		fprintf(stderr, "Case #%d:\n", test_id);
		for (int i = 0; i < h; ++i)
		{
			for (int j = 0; j < w; ++j)
			{
				if (j > 0) printf(" ");
				printf("%c", r[i][j]);
			}
			printf("\n");
		}
	}

	return 0;
}
