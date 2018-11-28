#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

const int MAX = 128;
int A[128][128], R, C;

bool change(int M[128][128])
{
	bool end = false;
	int nR[128][128];
	memset(nR, 0, sizeof(nR));
	for (int i = 1; i <= R; i++)
	{
		for (int j = 1; j <= C; j++)
		{
			nR[i][j] = M[i][j];
			if (M[i][j] == 1)
			{
				if (!M[i - 1][j] && !M[i][j - 1])
						nR[i][j] = 0;
			}
			else
			{
				if (M[i - 1][j] && M[i][j - 1])
						nR[i][j] = 1;
			}
			//printf("%d", nR[i][j]);
			end = end || nR[i][j];
		}
		//printf("\n");
	}
	//printf("\n");
	//system("pause");
	memcpy(A, nR, sizeof(nR));
	return end;
}

int main()
{
	freopen("f:\\C-small-attempt1.in", "r", stdin);
	freopen("f:\\C-small-attempt1.out", "w", stdout);
	int T;
	char s[100];
	scanf("%d", &T);
	for (int t_case = 1; t_case <= T; t_case++)
	{
		memset(A, 0, sizeof(A));
		R = 105; C = 105;
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
		{
			int x1, y1, x2, y2;
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			for (int x = x1; x <= x2; x++)
			{
				for (int y = y1; y <= y2; y++)
				{
					A[x][y] = 1;
				}
			}
		}
		int res = 0;
		while (change(A))
			res++;
		printf("Case #%d: %d\n", t_case, res + 1);
		fprintf(stderr, "Case #%d: %d\n",t_case, res + 1);
	}
	return 0;
}
