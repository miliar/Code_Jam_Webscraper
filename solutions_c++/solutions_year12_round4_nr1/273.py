// A
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdio>
using namespace std;
const int MAX=10000+10;


int N,L,flag;
int a[MAX][2];
int far[MAX];
bool vis[MAX];

bool okay(int x,int y)
{
	int d1=a[x][0],l1=a[x][1];
	int d2=a[y][0],l2=a[y][1];
		
	if(far[x]>=d2)
	{
		int tmp=min(d2-d1,l2);
		far[y]=max(far[y],d2+tmp);
		return 1;
	}
	return 0;
}
int main()
{
	int T;scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&N);
		for(int i=1;i<=N;i++) scanf("%d%d",&a[i][0],&a[i][1]);
		scanf("%d",&L);
		memset(vis,0,sizeof(vis));
		memset(far,0,sizeof(far));
		vis[1]=1;
		far[1]=2*a[1][0];
		flag=0;
		for(int i=1;i<=N;i++)
		{
			if(vis[i]==0) continue;
			if(far[i]>=L) {flag=1;break;}
			for(int j=i+1;j<=N;j++)
			{
				if(vis[j]==0&&okay(i,j)) vis[j]=1;
			}
		}
		
		static int CN=0;
		printf("Case #%d: ",++CN);
		if(flag) puts("YES");
		else puts("NO");
	}
		
	return 0;
}
