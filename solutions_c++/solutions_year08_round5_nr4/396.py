#include<iostream>
using namespace std;
int mat[101][101];
int m,n,k;
struct node
{
	int x,y;
}s[1000000];
int dx[2]={1,2};
int dy[2]={2,1};
const int inf=10007;
int solve()
{
	mat[1][1]=1;
	for(int i=1;i<=m;i++)
		for(int j=1;j<=n;j++)
		{
			if(mat[i][j]==-1)continue;
			if(mat[i][j]==0)continue;
			for(int p=0;p<2;p++)
			{
				int x=i+dx[p];
				int y=j+dy[p];
				if(x>m||y>n)continue;
				if(mat[x][y]==-1)continue;
				mat[x][y]=(mat[x][y]+mat[i][j])%inf;
			}
		}
		return  mat[m][n];
}
int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);

//	freopen("3.txt","w",stdout);
	int zu;
	scanf("%d",&zu);
	int g=1;
	while(zu--)
	{
		printf("Case #%d: ",g++);
		memset(mat,0,sizeof(mat));
		scanf("%d%d%d",&m,&n,&k);
		while(k--)
		{
			int x,y;
			scanf("%d%d",&x,&y);
			mat[x][y]=-1;
		}
		printf("%d\n",solve());
	}
}