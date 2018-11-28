#include <cstdio>
#include <algorithm>

using namespace std;

char a[50][50];
char b[50][50];
int n, k;

bool check(int x, int y, char ch)
{
	bool isok = true;
	for (int i = 0; i < k; ++i)
	{
		if (x + i == n) { isok = false; break; }
		if (b[x + i][y] != ch) { isok = false; break; }
	}
	if (isok) return true;

	isok = true;
	for (int i = 0; i < k; ++i)
	{
		if (y + i == n) { isok = false; break; }
		if (b[x][y + i] != ch) { isok = false; break; }
	}
	if (isok) return true;

	isok = true;
	for (int i = 0; i < k; ++i)
	{
		if (x + i == n || y + i == n) { isok = false; break; }
		if (b[x + i][y + i] != ch) { isok = false; break; }
	}
	if (isok) return true;

	isok = true;
	for (int i = 0; i < k; ++i)
	{
		if (x + i == n || y - i == -1) { isok = false; break; }
		if (b[x + i][y - i] != ch) { isok = false; break; }
	}
	return isok;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int qn = 1; qn <= T; ++qn)
	{
		scanf("%d %d", &n, &k);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
			{
				scanf(" %c", &a[i][j]);
				b[j][n - 1 - i] = a[i][j];
			}
		for (int i = 0; i < n; ++i)
		{
			for (int j = n - 1; j >= 0; --j)
			{
				bool changed = false;
				for (int k = j; k >= 0; --k)
				{
					if (b[k][i] != '.')
					{
						changed = true;
						swap(b[k][i], b[j][i]);
						break;
					}
				}
				if (!changed) break;
			}
		}
		int isR = 0, isB = 0;
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < n; ++j)
			{
				if (b[i][j] != '.')
				{
					if (check(i, j, b[i][j]))
					{
						if (b[i][j] == 'R') isR = 1;
						if (b[i][j] == 'B') isB = 1;
					}
				}
			}
		}
		printf("Case #%d: ", qn);
		if (isR == 1 && isB == 1) printf("Both\n");
		if (isR == 0 && isB == 1) printf("Blue\n");
		if (isR == 1 && isB == 0) printf("Red\n");
		if (isR == 0 && isB == 0) printf("Neither\n");
	}
}
