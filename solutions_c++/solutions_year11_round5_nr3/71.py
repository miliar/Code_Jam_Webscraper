#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
#include <set>

#define ll long long

using namespace std;

int dx[]={-1,-1,-1,0,1,1,1,0},
	dy[]={-1,0,1,1,1,0,-1,-1};

int F[5][5]={0},n,m;
int used[5][5]={0};
bool ok;

void dfs(int x,int y,bool f = true)
{
	if (used[x][y]==1)
	{
		ok=true;
		return;
	}
	if (used[x][y]==2)
	{
		ok=false;
		return;
	}
	if (f) used[x][y]=1;
	else used[x][y]=2;
	dfs((n+x+dx[F[x][y]])%n,(m+y+dy[F[x][y]])%m,false);
	if (!ok) return;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int TT=1;TT<=T;++TT)
	{
		printf("Case #%d: ",TT);
		int tot=0;
		char D[5][5]={0};
		cin >> n >> m;
		for(int i=0;i<n;i++)
			cin >> D[i];
		for(int mask=0;mask<(1<<(n*m));++mask)
		{
			int cur=0;
			for(int i=0;i<n;i++)
			{
				for(int j=0;j<m;j++)
				{
					if (D[i][j]=='-')
					{
						if (mask&(1<<cur)) F[i][j]=7;
						else F[i][j]=3;
					}
					if (D[i][j]=='|')
					{
						if (mask&(1<<cur)) F[i][j]=1;
						else F[i][j]=5;
					}
					if (D[i][j]=='/')
					{
						if (mask&(1<<cur)) F[i][j]=2;
						else F[i][j]=6;
					}
					if (D[i][j]=='\\')
					{
						if (mask&(1<<cur)) F[i][j]=0;
						else F[i][j]=4;
					}
					cur++;
				}
			}
			for(int i=0;i<n;i++)
				for(int j=0;j<m;j++)
					used[i][j]=0;
			for(int i=0;i<n;i++)
			{
				for(int j=0;j<m;j++)
				{
					if (!used[i][j])
					{
						ok=true;
						dfs(i,j);
						if (!ok) break;
						used[i][j]=2;
					}
				}
				if (!ok) break;
			}
			if (ok) tot++;
		}
		printf("%d\n",tot);
	}
	return 0;
}
