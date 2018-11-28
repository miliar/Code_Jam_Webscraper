
#include <iostream>
#include <queue>
#include <stdio.h>
using namespace std;

#define FOR(i, k, n) for (i = k; i < n; i++)

#define rep(i, n) FOR(i, 0, n)
#define repr(i, n) for (i = n - 1; i >= 0; i--)

int c[510][510];
int ans[510][510];
int sum[510];
#define mod 100003

void preceed(int n)
{
}

void test(int c)
{
	int R, C;

	bool possible = true;
	int i, j;
	char in[50][50];
	// bool u[50][50];
	scanf("%d %d", &R, &C);
	rep(i, R) 
	{
		getchar();
		rep(j, C)
		{
			scanf("%c", &(in[i][j]));
			// u[i][j] = false;
		}
	}

	rep(i, R) rep(j, C)
	{
		if (in[i][j] == '#')
		{
			if (i < R - 1 && j < C - 1 && in[i + 1][j] == '#' && in[i][j + 1] == '#' && in[i +1][j + 1] == '#')
			{
				// u[i][j] = u[i + 1][j] = u[i][j + 1] = u[i + 1][j + 1] = true;
				in[i][j] = '/';
				in[i + 1][j] = '\\';
				in[i][j + 1] = '\\';
				in[i + 1][j + 1] = '/';
			}
			else
			{
				goto TagFail;
			}
		}
	}
	printf("Case #%d:\n", c);
	rep(i, R)
	{
		rep(j, C)
		{
			printf("%c", in[i][j]);
		}
		printf("\n");
	}
	return;
TagFail:
	printf("Case #%d:\nImpossible\n", c);
}

int main()
{
	int i, t, m, n;
	preceed(500);

	scanf("%d", &t);
	
	rep(i, t) test(i + 1);

	return 0;
}

