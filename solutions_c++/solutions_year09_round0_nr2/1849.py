#include <cstdio>

int T, H, W, A[102][102], B[102][102], nsink;
int di[4] = {-1, 0, 0, 1};
int dj[4] = {0, -1, 1, 0};
char res[102][102];

void flow(int i, int j)
{
	if(B[i][j] == -1 && res[i][j] == -1)
		res[i][j] = nsink++;
	if(res[i][j] != -1)
		return;
	flow(i + di[B[i][j]], j + dj[B[i][j]]);
	res[i][j] = res[i + di[B[i][j]]][j + dj[B[i][j]]];
}

int main()
{
	scanf("%d", &T);
	for(int t = 1;t <= T;++t)
	{
		scanf("%d %d", &H, &W);
		for(int i = 0;i <= H + 1;++i)
			A[i][0] = A[i][W + 1] = 10000;
		for(int i = 0;i <= W + 1;++i)
			A[0][i] = A[H + 1][i] = 10000;
		for(int i = 1;i <= H;++i)
			for(int j = 1;j <= W;++j)
				scanf("%d", &A[i][j]);
		for(int i = 1;i <= H;++i)
			for(int j = 1;j <= W;++j)
			{
				res[i][j] = -1;
				B[i][j] = -1;
				for(int k = 0;k < 4;++k)
				{
					if(A[i][j] <= A[i + di[k]][j + dj[k]])
						continue;
					if(B[i][j] == -1 || A[i + di[k]][j + dj[k]] < A[i + di[B[i][j]]][j + dj[B[i][j]]])
						B[i][j] = k;
				}
				//printf("%d%c", A[i + di[B[i][j]]][j + dj[B[i][j]]], j == W ? '\n' : ' ');
			}
		nsink = 0;
		printf("Case #%d:\n", t);
		for(int i = 1;i <= H;++i)
			for(int j = 1;j <= W;++j)
			{
				if(res[i][j] == -1)
					flow(i, j);
				printf("%c%c", res[i][j] + 97, j == W ? '\n' : ' ');
			}
		
	}
	return 0;
}
