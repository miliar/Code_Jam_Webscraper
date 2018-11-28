#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

struct	POINT
{
	long double x, y, r;
}	A[1005];
int N;
int	W, L;

inline int	read()
{
	char ch = getchar(); int x = 0; bool flag = 0;
	for (; ch != '-' && (ch < '0' || ch > '9'); ch = getchar());
	if (ch == '-') 	{	flag = 1;	ch = getchar();	}
	for (; ch >= '0' && ch <= '9'; ch = getchar()) x = x * 10 + ch - '0';
	if (flag) return - x; return x;
}

inline int R()
{
	int x = rand() * rand() + rand();
	x = x * rand() + rand();
	x = x * rand() + rand();
	x = x * rand() + rand();
	return abs(x);
}

inline long double dis(long double x, long double y)
{
	return sqrt(x * x + y * y);
}

inline bool	check(long double x, long double y, long double r, int n)
{
	for (int i = 1; i <= n; ++ i)
		if (dis(abs(x - A[i].x), abs(y - A[i].y)) < r + A[i].r)
			return 0;
	return 1;
}

inline void	Main()
{
	N = read(); W = read(); L = read();
	for (int i = 1; i <= N; ++ i)	A[i].r = read() + 0.01;
	for (int i = 1; i <= N; ++ i)
	{
		while (1)
		{
			long double x = R() % W + R() % 1000 / 1000.0, y = R() % L + R() % 1000 / 1000.0;
			if (check(x, y, A[i].r, i - 1))
			{
				A[i].x = x;
				A[i].y = y;
				break;
			}
		}
		printf(" %.3lf %.3lf", double(A[i].x), double(A[i].y));
	}
	printf("\n");
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int T = read();
	for (int t = 1; t <= T; ++ t)
	{
		printf("Case #%d:", t);
		Main();
	}
	return 0;
}
