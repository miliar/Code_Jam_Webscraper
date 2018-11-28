#include <stdio.h>
#include <cstring>

char tmp[100][100], str[100][100];
int n, tc = 0, k;
char lst[100];
int top;

void init()
{
	for(int i=0; i<n; ++i)
	{
		for(int j=0; j<n; ++j) str[i][j] = tmp[n - 1 - j][i];
		str[i][n] = 0;
	}

	for(int i=n-1; i>=0; --i)
	{
		for(int j=0; j<n; ++j)
		{
			if(str[i][j] != '.') continue;

			int x = i - 1;
			while(x >= 0 && str[x][j] == '.') x--;
			if(x < 0) continue;
			str[i][j] = str[x][j];
			str[x][j] = '.';
		}
	}

	//for(int i=0; i<n; ++i) puts(str[i]);
}

bool check(char ch)
{
	if(top < k) return 0;

	int cnt = 0;
	char p = ' ';
	for(int i=0; i<top; ++i)
	{
		if(lst[i] == ch)
		{
			if(p == lst[i]) cnt++;
			else cnt = 1;
		}
		else
		{
			cnt = 0;
		}
		p = lst[i];
		if(cnt >= k) return 1;
	}
	return 0;
}

int solve(char ch)
{
	for(int i=0; i<n; ++i)
	{
		top = 0;
		for(int j=0; j<n; ++j) lst[top++] = str[i][j];
		if(check(ch)) return 1;
	}

	for(int i=0; i<n; ++i)
	{
		top = 0;
		for(int j=0; j<n; ++j) lst[top++] = str[j][i];
		if(check(ch)) return 1;
	}

	for(int i=0; i<n; ++i)
	{
		top = 0;
		int r = 0, c = i, dr = 1, dc = 1;
		while(r >= 0 && r < n && c >= 0 && c < n)
		{
			lst[top++] = str[r][c];
			r += dr;
			c += dc;
		}
		if(check(ch)) return 1;
	}

	for(int i=0; i<n; ++i)
	{
		top = 0;
		int r = i, c = 0, dr = 1, dc = 1;
		while(r >= 0 && r < n && c >= 0 && c < n)
		{
			lst[top++] = str[r][c];
			r += dr;
			c += dc;
		}
		if(check(ch)) return 1;
	}

	for(int i=0; i<n; ++i)
	{
		top = 0;
		int r = i, c = n - 1, dr = 1, dc = -1;
		while(r >= 0 && r < n && c >= 0 && c < n)
		{
			lst[top++] = str[r][c];
			r += dr;
			c += dc;
		}
		if(check(ch)) return 1;
	}

	for(int i=0; i<n; ++i)
	{
		top = 0;
		int r = 0, c = i, dr = 1, dc = -1;
		while(r >= 0 && r < n && c >= 0 && c < n)
		{
			lst[top++] = str[r][c];
			r += dr;
			c += dc;
		}
		if(check(ch)) return 1;
	}

	return 0;
}

int main()
{
	int t;

	scanf("%d", &t);

	while(t--)
	{
		scanf("%d%d", &n, &k);
		for(int i=0; i<n; ++i) scanf("%s", tmp[i]);

		init();

		int t1 = solve('R');
		int t2 = solve('B');

		printf("Case #%d: ", ++tc);
		if(t1 && t2) puts("Both");
		else if(t1) puts("Red");
		else if(t2) puts("Blue");
		else puts("Neither");
	}

	return 0;
}

