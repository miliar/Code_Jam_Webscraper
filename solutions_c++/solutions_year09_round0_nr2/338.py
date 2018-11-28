#include <iostream>
using namespace std;
int mat[105][105], H, W;
//int catalog[27][10002], ci;
int name[105][105], ci;
int offset[4][2] = {-1, 0, 0, -1, 0, 1, 1, 0};
char used[30];
bool checkbasin(int i, int j)
{
	if(i > 1 && mat[i-1][j] < mat[i][j]) return false;
	if(i < H && mat[i+1][j] < mat[i][j]) return false;
	if(j > 1 && mat[i][j-1] < mat[i][j]) return false;
	if(j < W && mat[i][j+1] < mat[i][j]) return false;
	return true;
}
int checkflow(int i, int j)
{
	int k, x, y, min = mat[i][j], reti, retj;
	reti = i, retj = j;
	for(k = 0; k < 4; k++)
	{
		x = i + offset[k][0];
		y = j + offset[k][1];
		if(x < 1 || x > H || y < 1 || y > W) continue;
		if(mat[x][y] < mat[i][j])
		{
			if(mat[x][y] < min) 
			{
				min = mat[x][y];
				reti = x;
				retj = y;
			}
		}
	}
	return reti * 1000 + retj;
}
void dfs(int i, int j)
{
	int k, x, y;
	for(k = 0; k < 4; k++)
	{
		x = i + offset[k][0];
		y = j + offset[k][1];
		if(x < 1 || x > H || y < 1 || y > W || name[x][y] != -1) continue;
		if(i * 1000 + j == checkflow(x, y))
		{
			name[x][y] = name[i][j];
			dfs(x, y);
		}
	}
}
int main()
{
//	freopen("B-small-attempt1.in", "r", stdin);
//	freopen("in.txt", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int N;
	scanf("%d", &N);
	int Case;
	for(Case = 1; Case <= N; Case++)
	{
		int i, j;
		scanf("%d%d", &H, &W);
		for(i = 1; i <= H; i++)
			for(j = 1; j <= W; j++)
				scanf("%d", &mat[i][j]);
		memset(name, -1, sizeof(name));
		ci = 0;
		for(i = 1; i <= H; i++)
			for(j = 1; j <= W; j++) if(name[i][j] == -1)
			{
				if(checkbasin(i, j))
				{
					name[i][j] = ci;
					dfs(i, j);
					ci++;
				//	catalog[ci][++catalog[ci][0]] = i * 1000 + j;
				}
			}
		printf("Case #%d:\n", Case);
		memset(used, -1, sizeof(used));
		char ch = 'a';
		for(i = 1; i <= H; i++, puts(""))
			for(j = 1; j <= W; j++)
			{
				if(used[name[i][j]] == -1) used[name[i][j]] = ch++;
				if(j == 1) printf("%c", used[name[i][j]]);
				else printf(" %c", used[name[i][j]]);
			}
	}
}