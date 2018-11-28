#include <cstdio>
#include <cstring>

int		n, m, D;

char	mat	[510][510];

struct	Matrix
{
	int		n, m;
	char	mat	[510][510];
	int		sum	[510][510];	
	int		ws	[510][510];

	void clear()
	{
		memset(mat, 0, sizeof(mat));
	}

	void solve()
	{
		memset(sum, 0, sizeof(sum));
		memset(ws, 0, sizeof(ws));
		for (int i = 1; i <= n; i ++)
		{
			int ls = 0;
			int lws = 0;
			for (int j = 1; j <= m; j ++)
			{
				ls += mat[i][j];
				lws += (n - i + 1) * (int) mat[i][j];
				sum[i][j] = sum[i - 1][j] + ls;
				ws[i][j] = ws[i - 1][j] + lws;
			}
		}
	}

	int get(int x, int y, int h, int w)
	{
		int vsum = sum[x][y] - sum[x - h][y] - sum[x][y - w] + sum[x - h][y - w];
		int vws = ws[x][y] - ws[x - h][y] - ws[x][y - w] + ws[x - h][y - w];
		int corner = h * mat[x - h + 1][y] + h * mat[x - h + 1][y - w + 1];
		return vws - (n - x) * vsum - corner;
	}
};

Matrix	list[4];

void init()
{
	scanf("%d%d%d", &n, &m, &D);
	for (int i = 0; i < n; i ++)
		scanf("%s", mat[i]);
	for (int i = 0; i < n; i ++)
		for (int j = 0; j < m; j ++)
			mat[i][j] -= '0';

	list[0].clear();
	list[1].clear();
	list[2].clear();
	list[3].clear();

	list[0].n = n; list[0].m = m;
	for (int i = 1; i <= list[0].n; i ++)
		for (int j = 1; j <= list[0].m; j ++)
			list[0].mat[i][j] = mat[i - 1][j - 1];

	for (int t = 1; t <= 3; t ++)
	{
		list[t].n = list[t - 1].m;
		list[t].m = list[t - 1].n;
		for (int i = 1; i <= list[t-1].n; i ++)
			for (int j = 1; j <= list[t-1].m; j ++)
				list[t].mat[ list[t-1].m + 1 - j ][ i ] = list[t - 1].mat[i][j];
	}
}

void solve()
{
	for (int t = 0; t <= 3; t ++)
		list[t].solve();


	int best = 2;

	// odd
	for (int k = (n % 2 == 0 ? n - 1 : n); k > best; k -= 2)
	{
		int h = (k + 1) / 2;
		for (int i = 1; i <= n; i ++)
			if ( i - h + 1 >= 1 && i + h - 1 <= n )
				for (int j = 1; j <= m; j ++)
					if ( j - h + 1 >= 1 && j + h - 1 <= m )
		{

			int left = j - h + 1;
			int right = j + h - 1;

			int upart = list[0].get(i, right, h, k);
			int dpart = list[2].get(n + 1 - i, m + 1 - left, h, k);

			if (upart != dpart) continue;

			int top = i - h + 1;
			int bottom = j + h - 1;

			int lpart = list[1].get(m + 1 - j, bottom, h, k);
			int rpart = list[3].get(j, n + 1 - top, h, k);

			if (lpart != rpart) continue;

			best = k;
			break;
		}
	}

	// even
	for (int k = (n % 2 == 1 ? n - 1 : n); k > best; k -= 2)
	{
		int h = k / 2;
		for (int i = k; i <= n; i ++)
			for (int j = k; j <= n; j ++)
		{
			int upart = list[0].get(i - h, j, h, k);
		
			int px = i - h + 1;
			int py = j - k + 1;
			
			int dpart = list[2].get(n + 1 - px, m + 1 - py, h, k);

			if (upart != dpart) continue;

			int qy = j - h + 1;
			int rpart = list[1].get(m + 1 - qy, i, h, k);

			int rx = i - k + 1;
			int ry = j - h;
			int lpart = list[3].get(ry, n + 1 - rx, h, k);


			if (lpart != rpart) continue;

			best = k;
			break;
		}
	}

	if (best < 3)
	{
		printf("IMPOSSIBLE\n");
	}
	else
		printf("%d\n", best);
}

int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small.out", "w", stdout);

	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);

//	freopen("in.txt", "r", stdin);

	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t ++)
	{
		init();
		printf("Case #%d: ", t);
		solve();
	}

	return 0;
}
