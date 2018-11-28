#include<iostream>
using namespace std;
int mat[101][101];
int next[101][101];
int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int zu;
	scanf("%d",&zu);
	for(int CaSe = 1 ;CaSe<=zu;CaSe++)
	{
		printf("Case #%d: ",CaSe);

		int m;
		scanf("%d",&m);
		memset(mat,0,sizeof(mat));
		for(int i=0;i<m;i++)
		{
			int x1,y1,x2,y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for(int ii=x1;ii<=x2;ii++)for(int jj=y1;jj<=y2;jj++)
			{
				mat[ii][jj]=1;
			}
		}
		bool f=1;
		for(int d =0;f;d++)
		{
			f=0;
			for(int i=1;i<=100;i++)for(int j=1;j<=100;j++)
			{
				if(mat[i][j]==1)
				{
					if(mat[i-1][j]+mat[i][j-1]==0)
					{
						next[i][j]=0;
					}
					else
					{
						next[i][j]=1;
						f=1;
					}
				}
				else
				{
					if(mat[i-1][j]+mat[i][j-1]==2)
					{
						next[i][j]=1;
						f=1;
					}
					else
					{
						next[i][j]=0;
					}
				}
			}
			for(int i=1;i<=100;i++)for(int j=1;j<=100;j++)mat[i][j]=next[i][j];
			if(!f)cout<<d+1<<endl;
		}
	}
}