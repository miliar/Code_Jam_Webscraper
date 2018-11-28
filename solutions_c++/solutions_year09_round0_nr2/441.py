#include <cstdio>
#include <cstring>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <cctype>
#include <bitset>
#include <sstream>
#include <set>
#include <map>

using namespace std;
template <class T> T sqr(T a) { return a * a; }
#define memfill(a, b) memset(a, b, sizeof(a))
#define pb push_back
#define vi vector<int>
#define vii vector<vector<int> >
#define vs vector<string>
#define pii pair<int, int>
#define dist(a, b) sqrt(sqr(a.x - b.x) + sqr(a.y - b.y))
#define bound(x, y, n, m) (x >= 0 && y >= 0 && x < n && y < m)

int w, h, counter;
int a[200][200];
char res[200][200];

int sh[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int alt(int x, int y)
{
	if (!bound(x, y, h, w))
		return 1000000000;
	return a[x][y];
}

char solve(int x, int y)
{
	if (res[x][y] != 0)
		return res[x][y];
	int best = 0;
	for (int i = 1; i < 4; i++)
		if (alt(x + sh[i][0], y + sh[i][1]) < alt(x + sh[best][0], y + sh[best][1]))
			best = i;
	if (alt(x + sh[best][0], y + sh[best][1]) < a[x][y])
		return res[x][y] = solve(x + sh[best][0], y + sh[best][1]);
	else
		return res[x][y] = 'a' + counter++;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	for (int testCount = 0; testCount < testNum; testCount++)
	{
		scanf("%d%d", &h, &w);
		for (int i = 0; i < h; i++)
			for (int j = 0; j < w; j++)
			{
				scanf("%d", &a[i][j]);
				res[i][j] = 0;
			}
		counter = 0;
		for (int i = 0; i < h; i++)
			for (int j = 0; j < w; j++)
				solve(i, j);
		printf("Case #%d:\n", testCount + 1);
		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w; j++)
				printf("%c ", res[i][j]);
			printf("\n");
		}
	}
	return 0;
}