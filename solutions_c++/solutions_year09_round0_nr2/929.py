#include <cstdio>
#include <cstring>

const int maxn = 100 + 10;

const int o[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
int a[maxn][maxn];
int b[maxn][maxn];
char c[maxn][maxn];
char mm[maxn * maxn];
int n, m;
int cur;
char lb;

bool inrang(int x, int y)
{
	return 0 <= x && x < n && 0 <= y && y < m;
}

int color(int x, int y)
{
	if (b[x][y]) return b[x][y];
	int mh = 100000, d;
	int tx, ty;
	for (int i = 0; i < 4; i++)
		if (inrang(tx = x + o[i][0], ty = y + o[i][1]) &&
			a[tx][ty] < mh)
		{
			mh = a[tx][ty];
			d = i;
		}
	if (mh >= a[x][y]) return b[x][y] = ++cur;
	else return b[x][y] = color(x + o[d][0], y + o[d][1]);
}

void label()
{
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			c[i][j] = mm[b[i][j]];
}

int main()
{
//	freopen("B-large.in", "r", stdin);
//	freopen("b.out", "w", stdout);
	int testnumber, testcount;
	
	scanf("%d", &testnumber);
	for (testcount = 0; testcount < testnumber; testcount++)
	{
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				scanf("%d", &a[i][j]);
		
		memset(b, 0, sizeof b);
		cur = 0;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (!b[i][j]) color(i, j);
		
		memset(mm, 0, sizeof mm);
		lb = 'a';
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (!mm[b[i][j]]) mm[b[i][j]] = lb++;
		label();
		
		printf("Case #%d:\n", testcount + 1);
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m - 1; j++)
				printf("%c ", c[i][j]);
			printf("%c\n", c[i][m - 1]);
		}
	}
	
	return 0;
}