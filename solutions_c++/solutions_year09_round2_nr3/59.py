#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <algorithm>
#define BASE 100
using namespace std;

string dp[2][10][10][200];
int id,W,Q,N,T;
char map[11][11];

int v[4][2] = {{1,0},{0,1},{-1,0},{0,-1}};

bool valid(int x,int y)
{
	return x >= 0 && x < W && y >= 0 && y < W;
}

int main()
{
	int i,j,k,t,l,m,x,y,ll,ok;
	char ss[100];
	//freopen("C-small-attempt0.in","r",stdin);
	//freopen("C.txt","w",stdout);
	scanf("%d",&T);
	for(t = 1;t <= T;t++)
	{
		scanf("%d%d",&W,&Q);
		for(i = 0;i < W;i++)
			scanf("%s",map[i]);
		printf("Case #%d:\n",t);
		while(Q--)
		{
			id = 0;
			scanf("%d",&N);
			for(i = 0;i < W;i++)
				for(j = 0;j < W;j++)
					for(k = 0;k < 200;k++)
						dp[id][i][j][k] = string("");
			for(i = 0;i < W;i++)
				for(j = 0;j < W;j++)
				{
					if(map[i][j] >= '0' && map[i][j] <= '9')
					{
						ss[0] = map[i][j];
						ss[1] = 0;
						dp[id][i][j][map[i][j] - '0' + BASE] = string(ss);
					}
				}
			for(i = 0;i < W;i++)
				for(j = 0;j < W;j++)
				{
					if(dp[id][i][j][BASE + N] != string(""))
					{
						puts(dp[id][i][j][BASE +N].c_str());
						goto la;
					}
				}
			while(true)
			{
				for(i = 0;i < W;i++)
					for(j = 0;j < W;j++)
						for(k = 0;k < 200;k++)
							dp[1 - id][i][j][k] = string("");
				for(i = 0;i < W;i++)
					for(j = 0;j < W;j++)
						for(k = 0;k < 200;k++)
						{
							if(dp[id][i][j][k] != string(""))
							{
								strcpy(ss,dp[id][i][j][k].c_str());
								ll = strlen(ss);
								for(l = 0;l < 4;l++)
								{
									x = i + v[l][0],y = j + v[l][1];
									if(valid(x,y) && (map[x][y] == '+' || map[x][y] == '-'))
									{
										ss[ll] = map[x][y];
										for(m = 0;m < 4;m++)
										{
											x += v[m][0],y += v[m][1];
											if(valid(x,y) && map[x][y] >= '0' && map[x][y] <= '9')
											{
												ss[ll + 1] = map[x][y];
												ss[ll + 2] = 0;
												if(ss[ll] == '+' && k + (map[x][y] - '0') >= 200)
												{
													x -= v[m][0];
													y -= v[m][1];
													continue;
												}
												else if(ss[ll] == '-' && k - (map[x][y] - '0') < 0)
												{
													x -= v[m][0];
													y -= v[m][1];
													continue;
												}
												if(ss[ll] == '+')
													ok = k + ss[ll + 1] - '0';
												else
													ok = k - ss[ll + 1] + '0';
												if(dp[1 - id][x][y][ok] == string("") || strcmp(ss,dp[1 - id][x][y][ok].c_str()) < 0)
													dp[1 - id][x][y][ok] = string(ss);
											}
											x -= v[m][0];
											y -= v[m][1];
										}
									}
								}
							}
						}
					id = 1 - id;
					string ans = string("");
					for(i = 0;i < W;i++)
						for(j = 0;j < W;j++)
						{
							if(dp[id][i][j][BASE + N] != string(""))
							{
								if(ans == string("") || strcmp(dp[id][i][j][BASE + N].c_str(),ans.c_str()) < 0)
									ans = dp[id][i][j][BASE + N].c_str();
							}
						}
					if(ans != string(""))
					{
						puts(ans.c_str());
						goto la;
					}
				}
				la:;
			}
		}
	//system("PAUSE");
	return 0;
}
								
		
	
