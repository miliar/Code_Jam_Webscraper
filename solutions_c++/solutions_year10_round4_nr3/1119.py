// gcj
#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
using namespace std;
const int MAX=200;

int N;
bool v[MAX][MAX],f[MAX][MAX];
bool check()
{
	for(int i=1;i<=100;i++)
	{
		for(int j=1;j<=100;j++) if(v[i][j]) return 0;
	}
	return 1;
}
void born()
{
	for(int i=1;i<=100;i++)
	{
		for(int j=1;j<=100;j++)
		{
			if(v[i][j]) continue;
			if(i>1&&j>1&&!f[i-1][j]&&!f[i][j-1]&&v[i-1][j]&&v[i][j-1]) f[i][j]=1;
		}
	}
}
void die()
{
	for(int i=1;i<=100;i++)
	{
		for(int j=1;j<=100;j++)
		{
			if(!v[i][j]) continue;
			if(i>1&&v[i-1][j]) f[i][j]=1;
			else if(j>1&&v[i][j-1]) f[i][j]=1;
			else ;
		}
	}
}
void jcopy()
{
	for(int i=1;i<=100;i++)
	{
		for(int j=1;j<=100;j++) v[i][j]=f[i][j];
	}
}
int main()
{
	freopen("F:\\C-small-attempt0.in","r",stdin);
	freopen("F:\\C-small-attempt0.out","w",stdout);
	int i,j,T;scanf("%d",&T);
	int CN=0;
	int x1,x2,y1,y2;
	while(T--)
	{
		memset(v,0,sizeof(v));
		scanf("%d",&N);
		for(i=1;i<=N;i++) 
		{
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			if(x1>x2) swap(x1,x2);
			if(y1>y2) swap(y1,y2);
			for(j=x1;j<=x2;j++)
			{
				for(int k=y1;k<=y2;k++) v[j][k]=1;
			}
		}

		int cnt=0;
		while(1)
		{
			if(check()) break;
			cnt++;
			memset(f,0,sizeof(f));
			born();
	
			die();
			jcopy();
		}
		printf("Case #%d: %d\n",++CN,cnt);
	}
	//system("pause");
	return 0;
}

