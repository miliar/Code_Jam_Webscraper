#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;

int H,W;
int alt[111][111];
int num[111][111];
int dx[4]={-1,0,0,1};
int dy[4]={0,-1,1,0};
char numlet[111111];
char let[111][111];
vector< pair<int,int>> cells[11111];

inline bool inside(int x,int y)
{
	return x>=0&&y>=0&&x<H&&y<W;
}
void test()
{
	scanf("%d%d",&H,&W);

	int i,j,x,y,J,k,X,Y,top=0,cur;

	for(i=0;i<11111;i++) cells[i].clear();
	for(i=0;i<H;i++)
		for(j=0;j<W;j++)
		{
			scanf("%d",&alt[i][j]);
			num[i][j]=0;
			let[i][j]=0;
			cells[alt[i][j]].push_back(make_pair(i,j));
		}

		for(i=0;i<11111;i++) if(!cells[i].empty())
		{
			J=cells[i].size();
			for(j=0;j<J;j++)
			{
				x=cells[i][j].first;
				y=cells[i][j].second;
				cur=alt[x][y];
				for(k=0;k<4;k++)
				{
					X=x+dx[k]; Y=y+dy[k];
					if(inside(X,Y))
					{
						if(alt[X][Y]<cur) 
						{
							num[x][y]=num[X][Y];
							cur=alt[X][Y];
						}
					}
				}
				if(!num[x][y]) num[x][y]=++top;
			}
		}

		int maxnum=top+1;
		top=0;

		for(i=0;i<maxnum;i++) numlet[i]=0;

		for(i=0;i<H;i++)
			for(j=0;j<W;j++)
				if(!numlet[num[i][j]]) numlet[num[i][j]]='a'+(top++);

		printf("\n");

		for(i=0;i<H;i++)
		{
			for(j=0;j<W;j++)
				printf("%c ",numlet[num[i][j]]);
			printf("\n");
		}
	
}
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);

	int t=0,T;

	scanf("%d",&T);

	for(t=0;t<T;t++)
	{
		printf("Case #%d:",t+1);
		test();
	}
}