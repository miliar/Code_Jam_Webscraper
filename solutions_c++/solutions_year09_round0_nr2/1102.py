#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;

struct Node
{
	int vi, vj;
}node[200005];

int num, mat[105][105], used[105][105], row, col;

int dir[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

void solve(int x, int y)
{
	int len = 0, ans = -1, Min, xx, yy, px, py, i;
	while(1)
	{
		if(used[x][y] != -1)
		{
			ans = used[x][y];
			break;
		}
		Min = -1;
		for(i=0; i<4; i++)
		{
			xx = x + dir[i][0];
			yy = y + dir[i][1];
			if(xx < 0 || xx >= row || yy < 0 || yy >= col)
				continue;
			if(mat[x][y] > mat[xx][yy])
			{
				if(Min == -1 || Min > mat[xx][yy])
				{
					Min = mat[xx][yy];
					px = xx;
					py = yy;
				}
			}
		}
		node[len].vi = x;
		node[len].vj = y;
		len ++;
	
		if(Min == -1)
			break;
		x = px;
		y = py;
	}
	if(ans == -1)
	{
		for(i=0; i<len; i++)
		{
			used[node[i].vi][node[i].vj] = num;
		}
		num ++;
	}
	else
	{
		for(i=0; i<len; i++)
		{
			used[node[i].vi][node[i].vj] = ans;
		}
	}
}

int main()
{
	//freopen("B-large.in", "r", stdin);
//	freopen("B-large.out", "w", stdout);
	int test, i, j, cases = 1;
	scanf("%d", &test);
	while(test --)
	{
		scanf("%d %d", &row, &col);
		for(i=0; i<row; i++)
		{
			for(j=0; j<col; j++)
			{
				scanf("%d", &mat[i][j]);
				used[i][j] = -1;
			}
		}

		num = 0;
		for(i=0; i<row; i++)
		{
			for(j=0; j<col; j++)
			{
				if(used[i][j] != -1)
					continue;
				solve(i, j);
			}
		}

		printf("Case #%d:\n", cases ++);
		for(i=0; i<row; i++)
		{
			for(j=0; j<col; j++)
			{
				if(j)
					printf(" ");
				printf("%c", used[i][j] + 'a');
			}
			printf("\n");
		}
	}
	return 0;
}