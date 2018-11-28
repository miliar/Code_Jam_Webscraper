#define _USE_MATH_DEFINES
#include <numeric>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <sstream>
using namespace std;
#pragma warning(disable : 4996 4018)
#pragma comment(linker, "/STACK:16777216")

int R, C;
int A[100][100];
char B[100][100];
char basin;

int dr[] = { -1, 0, 0, 1 };
int dc[] = { 0, -1, 1, 0 };

char fun(int r, int c)
{
	if(B[r][c])
		return B[r][c];
	int mh = 100000, mi;
	for(int i = 0; i < 4; i++)
	{
		int cr = r + dr[i];
		int cc = c + dc[i];
		if(cr < 0 || cr == R || cc < 0 || cc == C)
			continue;
		if(A[cr][cc] < A[r][c] && A[cr][cc] < mh)
			mh = A[cr][cc], mi = i;
	}

	if(mh == 100000)
		return B[r][c] = basin++;

	return B[r][c] = fun(r + dr[mi], c + dc[mi]);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for(int t = 0; t < T; t++)
	{
		printf("Case #%i:\n", t + 1);
		cin >> R >> C;

		int i, j;
		for(i = 0; i < R; i++)
			for(j = 0; j < C; j++)
				cin >> A[i][j];

		memset(B, 0, sizeof(B));
		basin = 'a';

		for(i = 0; i < R; i++)
		{
			for(j = 0; j < C; j++)
			{
				if(!B[i][j])
					fun(i, j);
				printf("%c ", B[i][j]);
			}
			printf("\n");
		}
	}

	return 0;
}
