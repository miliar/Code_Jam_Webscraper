#include<iostream>
#include<cmath>
#include<vector>
#include<queue>
#include<cstring>
using namespace std;

struct node
{
	int row,col;
};

int map[110][110];
char grid[110][110];
int mm[4][2]=
{
	-1,0,
	0,-1,
	0,1,
	1,0,
};
node stk[110000];

int main()
{
	int T,r,c,i,j,ii,min,k,flag,ll;
	char cur;
	node start,var,nw,dir;

	//freopen("B-large.in","r",stdin);
	//freopen("B-out.txt","w",stdout);
	
	scanf("%d",&T);
	for(ii=0;ii<T;ii++)
	{
		scanf("%d %d",&r,&c);
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				scanf("%d",&map[i][j]);
				grid[i][j]='.';
			}
		}
		cur='a';
		queue<node> q;
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				if(grid[i][j]=='.')
				{
					start.row=i;
					start.col=j;
					min=32000;
					flag=0;
					for(k=0;k<4;k++)
					{
						nw.row=start.row+mm[k][0];
						nw.col=start.col+mm[k][1];
						if(nw.row>=0 && nw.row<r && nw.col>=0 && nw.col<c)
						{
							if(map[start.row][start.col]>map[nw.row][nw.col])
							{
								flag=1;
								if(map[nw.row][nw.col]<min)
								{
									min=map[nw.row][nw.col];
									dir.row=nw.row;
									dir.col=nw.col;
								}
							}
						}
					}
					if(flag==0)
					{
						grid[start.row][start.col]=cur;
						cur++;
					}
					else
					{
						if(grid[dir.row][dir.col]!='.')
						{
							grid[start.row][start.col]=grid[dir.row][dir.col];
						}
						else
						{
							q.push(start);
							ll=0;
							while(!q.empty())
							{
								var=q.front();
								q.pop();
								stk[ll]=var;
								ll++;
								if(grid[var.row][var.col]!='.')
								{
									for(k=0;k<ll;k++)
									{
										grid[stk[k].row][stk[k].col]=grid[var.row][var.col];
									}
									continue;
								}
								grid[var.row][var.col]='X';
								flag=0;
								min=32000;
								for(k=0;k<4;k++)
								{
									nw.row=var.row+mm[k][0];
									nw.col=var.col+mm[k][1];
									if(nw.row>=0 && nw.row<r && nw.col>=0 && nw.col<c)
									{
										if(map[var.row][var.col]>map[nw.row][nw.col])
										{
											flag=1;
											if(map[nw.row][nw.col]<min)
											{
												min=map[nw.row][nw.col];
												dir.row=nw.row;
												dir.col=nw.col;
											}
										}
									}
								}
								if(flag==1)
								{
									q.push(dir);
								}
								else
								{
									for(k=0;k<ll;k++)
									{
										grid[stk[k].row][stk[k].col]=cur;
									}
									cur++;
								}
							}
						}
					}
				}
			}
		}
		printf("Case #%d:\n",(ii+1));
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				if(j!=0) printf(" ");
				printf("%c",grid[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}