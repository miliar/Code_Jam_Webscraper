#pragma comment(linker, "/STACK:16777216")
#include <stdio.h>
#include <memory.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int, int> PII;

#define CL(x)		memset(x, 0, sizeof(x))
#define CLX(x, v)	memset(x, v, sizeof(x))
#define PB			push_back
#define MP			make_pair

///////////////////////////////////////////////////////////

const int INF = 1000000;
const int N = 128;

int h, w;
int a[N][N];

void scan()
{
	CLX(a, -1);
	scanf("%d %d", &h, &w);
	for (int i = 1; i <= h; i++)
		for (int j = 1; j <= w; j++)
			scanf("%d", &a[i][j]);
}

char b[N][N];

void calc_b()
{
	CLX(b, 'X');
	for (int i = 1; i <= h; i++)
		for (int j = 1; j <= w; j++)
		{
			int ff, f = INF;
			ff = a[i-1][j]; if (ff != -1 && ff < f) { b[i][j] = 'N'; f = ff; }
			ff = a[i][j-1]; if (ff != -1 && ff < f) { b[i][j] = 'W'; f = ff; }
			ff = a[i][j+1]; if (ff != -1 && ff < f) { b[i][j] = 'E'; f = ff; }
			ff = a[i+1][j]; if (ff != -1 && ff < f) { b[i][j] = 'S'; f = ff; }
			if (f >= a[i][j]) b[i][j] = 'X';
		}
}

char t;
int qs, qf;
int q[2*N*N];
char d[N][N];

void push(int r, int c)
{
	if (d[r][c]) return;
	d[r][c] = t;
	q[qf++] = r;
	q[qf++] = c;
}

void pop(int &r, int &c)
{
	r = q[qs++];
	c = q[qs++];
}

void bfs(int r, int c)
{
	qs = qf = 0;
	push(r, c);
	while (qs != qf)
	{
		pop(r, c);

		if (b[r][c] == 'N') push(r-1, c);
		if (b[r][c] == 'W') push(r, c-1);
		if (b[r][c] == 'E') push(r, c+1);
		if (b[r][c] == 'S') push(r+1, c);

		if (b[r-1][c] == 'S') push(r-1, c);
		if (b[r][c-1] == 'E') push(r, c-1);
		if (b[r][c+1] == 'W') push(r, c+1);
		if (b[r+1][c] == 'N') push(r+1, c);
	}
}

void solve()
{
	calc_b();

	t = 'a';
	CL(d);

	for (int i = 1; i <= h; i++)
		for (int j = 1; j <= w; j++)
			if (!d[i][j])
			{
				bfs(i, j);
				t++;
			}

	for (int i = 1; i <= h; i++)
	{
		for (int j = 1; j <= w; j++)
		{
			if (j > 1) printf(" ");
			printf("%c", d[i][j]);
		}
		printf("\n");
	}
}

int main()
{
//#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
//#endif

	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		printf("Case #%d:\n", i+1);
		scan();
		solve();
	}
	
	return 0;
}