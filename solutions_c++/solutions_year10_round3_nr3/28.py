#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

int nt;

int n, m;

char s[1000];

char c[512][512];

int d[512][512];

//int cap[512][512];

int min3(int a, int b, int c)
{
	if (a > b) a = b;
	if (a > c) a = c;
	return a;
}

/*int get_capped(int x, int y)
{
	if (cap[x][y] != -1 && cap[x][y] < d[x][y]) return cap[x][y];
	return d[x][y];
}*/

void cap(int x, int y, int size)
{
	if (x < 0 || x >= m) return;
	if (y < 0 || y >= n) return;

	if (d[x][y] > size) d[x][y] = size;
}

void cut(int x, int y, int size)
{
	for(int i = 0; i < size; i++)
	for(int j = 0; j < size; j++) d[x - i][y - j] = 0;

	// capping

	for(int i = 1; i < size; i++)
	{
		for(int j = -i; j < size; j++) cap(x + i, y - j, i);
		for(int j = -i; j < size; j++) cap(x - j, y + i, i);
	}

/*		puts("-------------------");

		for(int i = 0; i < m; i++)
		{
			for(int j = 0; j < n; j++) printf("%d", d[i][j]);
			puts("");
		}
*/
}

vector<pair<int, int> > res;

int main()
{
	scanf("%d", &nt);

	for(int tt = 1; tt <= nt; tt++)
	{
		printf("Case #%d: ", tt);

		scanf("%d %d", &m, &n);

		for(int i = 0; i < m; i++)
		{
			scanf("%s", s);
			for(int j = 0; j < n; j += 4)
			{
				int k = s[j / 4];
				if (k <= '9') k -= '0'; else k -= 'A' - 10;				

				c[i][j    ] = k / 8; k %= 8;
				c[i][j + 1] = k / 4; k %= 4;
				c[i][j + 2] = k / 2; k %= 2;
				c[i][j + 3] = k;
			}
		}

		for(int i = 0; i < m; i++) d[i][0] = 1;
		for(int i = 0; i < n; i++) d[0][i] = 1;

		for(int i = 1; i < m; i++)
		for(int j = 1; j < n; j++)
		{
			d[i][j] = 1;

			if (c[i][j] != c[i - 1][j - 1]) continue;
			if (c[i][j] == c[i - 1][j    ]) continue;
			if (c[i][j] == c[i    ][j - 1]) continue;

			d[i][j] = min3(d[i - 1][j - 1], d[i - 1][j], d[i][j - 1]) + 1;
		}

/*		puts("");

		for(int i = 0; i < m; i++)
		{
			for(int j = 0; j < n; j++) printf("%d", d[i][j]);
			puts("");
		}
*/
//		for(int i = 0; i < m; i++) for(int j = 0; j < n; j++) cap[i][j] = -1;

        res.clear();
		
		for(int size = 512; size > 0; size--)
		{
			int cnt = 0;
			for(int i = 0; i < m; i++)
			{
		        int j = 0;

		        while(j < n)
		        {

					if (d[i][j] == size)
					{
						cut(i, j, size);
						cnt++;
						j += size;
					}

					j += size - d[i][j];
				}
			}
			if (cnt) res.push_back(make_pair(size, cnt));
		}

		printf("%d\n", res.size());
		for(int i = 0; i < res.size(); i++) printf("%d %d\n", res[i].first, res[i].second);
	}	

	return 0;	
}