#include <cstdio>
#include <cstring>

const int maxn = 50;
const int o[4][2] = {{1, 0}, {1, -1}, {1, 1}, {0, 1}};

char a[maxn][maxn];
int n, k;

bool inrange(int x, int y)
{
	return 0 <= x && x < n && 0 <= y && y < n;
}

int getline(int x, int y)
{
	int max = 0;
	for (int i = 0; i < 4; i++)
	{
		int dx = x, dy = y;
		int tx, ty;
		int res = 1;
		while (inrange((tx = dx + o[i][0]), (ty = dy + o[i][1])) && a[tx][ty] == a[x][y])
		{
			dx = tx;
			dy = ty;
			res++;
		}
		if (res > max) max = res;
	}
	return max;
}

int main()
{
	int testnumber, testcount;
	
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &testnumber);
	for (testcount = 0; testcount < testnumber; testcount++)
	{
		scanf("%d%d", &n, &k);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				scanf(" %c", &a[i][j]);
		
		for (int i = 0; i < n; i++)
		{
			bool change = true;
			while (change)
			{
				change = false;
				for (int j = n - 1; j >= 1; j--)
					if (a[i][j] == '.' && a[i][j - 1] != '.')
					{
						a[i][j] = a[i][j - 1];
						a[i][j - 1] = '.';
						change = true;
					}
			}
		}
		
		int max1 = 0, max2 = 0;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				if (a[i][j] != '.')
			{
				int l = getline(i, j);
				if (a[i][j] == 'R' && l > max1) max1 = l;
				if (a[i][j] == 'B' && l > max2) max2 = l;
			}
		printf("Case #%d: ", testcount + 1);
		if (max1 >= k)
			if (max2 >= k) printf("Both\n");
			else printf("Red\n");
		else
			if (max2 >= k) printf("Blue\n");
			else printf("Neither\n");
	}
	
	return 0;
}
