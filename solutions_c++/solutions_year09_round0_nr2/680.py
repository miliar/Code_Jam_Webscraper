#include<cstdio>
#include<iostream>

#define MAX 100

using namespace std;

int H,W;
int G[MAX][MAX];
char Ans[MAX][MAX];

int Dx[]={-1, 0, 0, 1};
int Dy[]={ 0,-1, 1, 0};

pair<int,int> Q[MAX*MAX];

int main()
{
	freopen("B-Large.in","r",stdin);
	freopen("B-Large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int Case=1;Case<=T;Case++)
	{
		scanf("%d %d",&H,&W);
		for(int i=0;i<H;i++) for(int j=0;j<W;j++)
		{
			scanf("%d",&G[i][j]);
			Ans[i][j]=0;
		}
		char ID='a';
		for(int i=0;i<H;i++) for(int j=0;j<W;j++) if(!Ans[i][j])
		{
			Ans[i][j]=ID;
			int L=0,R=0;
			Q[R++]=make_pair(i,j);
			while(L<R)
			{
				pair<int,int> Last=Q[L++];
				int Dir=-1,Min=G[Last.first][Last.second];
				for(int k=0;k<4;k++)
				{
					int x=Last.first+Dx[k];
					int y=Last.second+Dy[k];
					if(0>x||x>=H||0>y||y>=W) continue;

					//Flow in;
					if(G[x][y]>G[Last.first][Last.second])
					{
						int Temp_Dir=-1,Temp_Min=G[x][y];
						for(int l=0;l<4;l++)
						{
							int Temp_x=x+Dx[l];
							int Temp_y=y+Dy[l];
							if(0>Temp_x||Temp_x>=H||0>Temp_y||Temp_y>=W) continue;
							if(G[Temp_x][Temp_y]<Temp_Min)
							{
								Temp_Min=G[Temp_x][Temp_y];
								Temp_Dir=l;
							}
						}
						if(Temp_Dir==-1) continue;
						int Temp_x=x+Dx[Temp_Dir];
						int Temp_y=y+Dy[Temp_Dir];
						if(Temp_x==Last.first&&Temp_y==Last.second)
						{
							if(Ans[x][y]) continue;
							Ans[x][y]=ID;
							Q[R++]=make_pair(x,y);
						}
						continue;
					}

					if(G[x][y]<Min)
					{
						Min=G[x][y];
						Dir=k;
					}
				}
				if(Dir==-1) continue;
				//Flow out
				int x=Last.first+Dx[Dir];
				int y=Last.second+Dy[Dir];
				if(Ans[x][y]) continue;
				Ans[x][y]=ID;
				Q[R++]=make_pair(x,y);
			}
			ID++;
		}

		printf("Case #%d:\n",Case);
		for(int i=0;i<H;i++) for(int j=0;j<W;j++)
		{
			putchar(Ans[i][j]);
			if(j==W-1) putchar('\n');
			else putchar(' ');
		}
	}
	return 0;
}