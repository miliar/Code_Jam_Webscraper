#include<stdio.h>
#include <string.h>
int ax[4]={-1,0,0,1};
int ay[4]={0,-1,1,0};
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int T,H,W;
	int height[128][128];
	char tag[128][128];
	int stack[10000][2];
	int top;
	scanf("%d",&T);
	for(int ll=0;ll<T;ll++)
	{
		scanf("%d%d",&H,&W);
		memset(height,0,sizeof(height));
		for(int i=1;i<=H;i++)
		{
			for(int j=1;j<=W;j++)
			{
				scanf("%d",&height[i][j]);
			}
		}
		int level=-1;
		memset(tag,0,sizeof(tag));
		while(true)
		{
			int x,y;
			x=-1;
			y=-1;
			for(int i=1;i<=H;i++)
			{
				for(int j=1;j<=W;j++)
				{
					if(tag[i][j]==0)
					{
						x=i;
						y=j;
						break;
					}
				}
				if(x>=0)
					break;
			}
			if(x>=0)
			{
				level++;
				top=0;
				stack[0][0]=x;
				stack[0][1]=y;
				tag[x][y]=level+'a';
				while(top>=0)
				{
					x=stack[top][0];
					y=stack[top][1];
					top--;
					int tx,ty;
					int sx,sy;
					sx=-1;
					sy=-1;
					for(int i=0;i<4;i++)
					{
						tx=x+ax[i];
						ty=y+ay[i];
						if(tx>=1&&tx<=H&&ty>=1&&ty<=W)
						{
							if(sx==-1)
							{
								if(height[tx][ty]<height[x][y])
								{
									sx=tx;
									sy=ty;
								}
							}
							else
							{
								if(height[tx][ty]<height[sx][sy])
								{
									sx=tx;
									sy=ty;
								}
							}
						}
					}
					if(sx>=0&&tag[sx][sy]==0)
					{
						++top;
						stack[top][0]=sx;
						stack[top][1]=sy;
						tag[sx][sy]=level+'a';
					}
					for(int i=0;i<4;i++)
					{
						tx=x+ax[i];
						ty=y+ay[i];
						if(tx>=1&&tx<=H&&ty>=1&&ty<=W&&tag[tx][ty]==0)
						{
							int kx,ky;
							int mx,my;
							mx=-1;
							my=-1;
							for(int j=0;j<4;j++)
							{
								kx=tx+ax[j];
								ky=ty+ay[j];
								if(kx>=1&&kx<=H&&ky>=1&&ky<=W)
								{
									if(mx==-1)
									{
										if(height[kx][ky]<height[tx][ty])
										{
											mx=kx;
											my=ky;
										}
									}
									else
									{
										if(height[kx][ky]<height[mx][my])
										{
											mx=kx;
											my=ky;
										}
									}
								}
							}
							if(mx==x&&my==y&&tag[tx][ty]==0)
							{
								++top;
								stack[top][0]=tx;
								stack[top][1]=ty;
								tag[tx][ty]=level+'a';
							}
						}
					}

				}
				
			}
			else
			{
				break;
			}

		}
		printf("Case #%d:\n",ll+1);
		for(int i=1;i<=H;i++)
		{
			for(int j=1;j<W;j++)
			{
				printf("%c ",tag[i][j]);
			}
			printf("%c\n",tag[i][W]);
		}
	}
}