#include <cstdio>
#include <cstring>


int nt;

int n, m, F;

char s[55][55];

int d[55][55][55][55];


int solve(int x, int y, int from, int to);

int jump(int x, int y, int from, int to)
{
	int xx = x + 1;
	while(s[xx + 1][y] == '.') xx++;

	if (xx - x > F) return -2;

	if (xx == x + 1) return solve(xx, y, from, to);

	return solve(xx, y, 52, 52);
}

int solve(int x, int y, int from, int to)
{
	if (d[x][y][from][to] != -1) return d[x][y][from][to];

	if (x == n) return 0;

	int res = -2, cur = 0;

	// walk left & jump

	for(int i = 1; ;i++)
		if (s[x][y - i] == '.' || (y - i >= from && y - i <= to))
		{
			if (s[x + 1][y - i] == '.')
			{
				cur = jump(x, y - i, 52, 52);

				if (cur != -2)
				if (res == -2 || res > cur) res = cur;				

				break;
			}
		}
		else break;


	// walk right & jump

	for(int i = 1; ;i++)
		if (s[x][y + i] == '.' || (y + i >= from && y + i <= to))
		{
			if (s[x + 1][y + i] == '.')
			{
				cur = jump(x, y + i, 52, 52);

				if (cur != -2)
				if (res == -2 || res > cur) res = cur;				

				break;
			}
		}
		else break;

	// dig & jump

	int L = y, R = y;

	while(1)
	{
		L--;

		if (s[x][L] == '.' || (L >= from && L <= to))
		if (s[x + 1][L] == '#') continue;

		L++; break;
	}

	while(1)
	{
		R++;

		if (s[x][R] == '.' || (R >= from && R <= to))
		if (s[x + 1][R] == '#') continue;

		R--; break;
	}

//	printf("L = %d, R = %d\n", L, R);

	for(int start = L; start <= R; start++)
	for(int end = start; end <= R; end++)
	{
		int digs = end - start + 1;

		if (start > L)
		{
			cur = jump(x, start, start, end);

			if (cur != -2)
			if (res == -2 || res > cur + digs) res = cur + digs;				
		}

		if (end < R)
		{
			cur = jump(x, end, start, end);

			if (cur != -2)
			if (res == -2 || res > cur + digs) res = cur + digs;
		}
	}

	d[x][y][from][to] = res;
	return res;
}


int main()
{
	scanf("%d", &nt);

	for(int tt = 1; tt <= nt; tt++)
	{
		printf("Case #%d: ", tt);

		scanf("%d %d %d", &n, &m, &F);

		memset(s, '#', sizeof s);

		for(int i = 1; i <= n; i++) scanf("%s", s[i] + 1);

		memset(d, -1, sizeof d);

		int res = solve(1, 1, 52, 52);

		if (res == -2) printf("No\n"); else printf("Yes %d\n", res);
	}

	return 0;	
}