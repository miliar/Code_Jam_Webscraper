#include<iostream>
using namespace std;

#define MAXSIZE 10005

int rank[MAXSIZE];    // 节点高度的上界
int parent[MAXSIZE]; // 根节点
int ref[MAXSIZE];
int chars[26];

int FindSet(int x)
{// 查找+递归的路径压缩
	if( x != parent[x] ) 
		parent[x] = FindSet(parent[x]);
    return parent[x];
}
void Union(int root1, int root2)
{
	int x = FindSet(root1), y = FindSet(root2);
    if( x == y )
		return ;
    if( rank[x] > rank[y] )
		parent[y] = x;
    else
	{
        parent[x] = y;
		if( rank[x] == rank[y] ) ++rank[y];
	}
}
void init(int n)
{
	memset(rank, 0, sizeof(int)*n);
    for(int i=0; i < n; ++i)
	{
		parent[i] = i;
		ref[i] = -1;
	}
}

int matrix[105][105], dir[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, h, w;
	scanf("%d", &t);
	for(int cc = 1; cc <= t; cc++)
	{
		scanf("%d%d", &h, &w);
		for(int i = 0; i < h; i++)
		{
			for(int j = 0; j < w; j++)
			{
				scanf("%d", &matrix[i][j]);
			}
		}
		init(h*w);
		for(int i = 0; i < h; i++)
		{
			for(int j = 0; j < w; j++)
			{
				if(cc == 5 && i == 1 && j == 0)
				{
					cc++;
					cc--;
				}
				int mx, my, x, y, mins = INT_MAX;
				for(int k = 0; k < 4; k++)
				{
					x = i + dir[k][0];
					y = j + dir[k][1];
					if(x >= 0 && x < h && y >= 0 && y < w)
					{
						if(matrix[x][y] < mins && matrix[x][y] < matrix[i][j])
						{
							mx = x;
							my = y;
							mins = matrix[x][y];
						}
					}
				}
				if(mins != INT_MAX)
				{
					Union(mx*w+my, w*i+j);
				}
			}
		}

		printf("Case #%d:\n", cc);
		char c = 'a';
		for(int i = 0; i < h; i++)
		{
			for(int j = 0; j < w; j++)
			{
				int num = i * w + j;
				num = FindSet(num);
				if(ref[num] == -1)
				{
					ref[num] = c;
					c++;
				}
				if(j != 0)
				{
					printf(" ");
				}
				printf("%c", (char)(ref[num]));
			}
			printf("\n");
		}
	}
	return 0;
}