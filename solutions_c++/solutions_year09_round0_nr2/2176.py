#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;

int H, W;
int a[100][100];
int ret[100][100];
int bas;

int dfs(int r, int c)
{
	if (ret[r][c]) return ret[r][c];
	int dx[4] = {0,-1,1,0};
	int dy[4] = {-1,0,0,1};
	int res = -1;
	int resv = a[r][c];
	for (int i = 0; i < 4; i++)
	{
		int tr = r + dy[i];
		int tc = c + dx[i];
		if (tr>=0&&tr<H&&tc>=0&&tc<W)
			if (a[tr][tc]<resv)
			{
				res = i;
				resv = a[tr][tc];
			}
	}
	if (res == -1)
		return ret[r][c] = bas++;
	else
		return ret[r][c] = dfs(r + dy[res], c+dx[res]);
}

void getac()
{
	memset(ret, 0, sizeof(ret));
	bas = 'a';
	for (int i =0 ; i < H; i++)
		for (int j =0 ; j < W; j++)
			dfs(i, j);
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t= 0; t < T; t++)
	{
		scanf("%d%d", &H, &W);
		for (int i =0 ; i<H; i++)
			for (int j =0 ; j < W; j++)
				scanf("%d", &a[i][j]);
		getac();
		printf("Case #%d:\n", t+1);
		for (int i =0 ; i<H; i++)
		{
			for (int j =0 ; j < W;j++)
			{
				printf("%c", ret[i][j]);
				if (j!=W-1) putchar(' ');
			}
			putchar('\n');
		}

	}
	
	return 0;
}

