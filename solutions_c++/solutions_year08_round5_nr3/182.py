#include<cstdio>
#include<vector>
using namespace std;
int t,k,n,m,i,j,sol[2][2<<10],cur,last,b[2][101];
char a[100][100];
void go2(int i,int y,int x,int nr)
{
	if(i==m+1)
	{
		if(nr+sol[last][y]>sol[cur][x])
			sol[cur][x]=nr+sol[last][y];
		return;
	}
	if(b[last][i-1]==0 && a[j-1][i-1]=='.' && b[cur][i-1]==0 && b[cur][i+1]==0)
	{
		b[last][i]=1;
		go2(i+1,(y<<1)+1,x,nr);
	}
	b[last][i]=0;
	go2(i+1,y<<1,x,nr);
}
void go(int i,int x,int nr)
{
	if(i==m+1)
	{
		go2(1,0,x,nr);
		return;
	}
	if(b[cur][i-1]==0 && a[j][i-1]=='.')
	{
		b[cur][i]=1;
		go(i+1,(x<<1)+1,nr+1);
	}
	b[cur][i]=0;
	go(i+1,x<<1,nr);
}
int main()
{
	freopen("Input.in","r",stdin);
	freopen("Output.out","w",stdout);
	scanf("%d ",&t);
	for(k=1;k<=t;k++)
	{
		scanf("%d %d ",&n,&m);
		for(i=1;i<=n;i++)
			scanf("%s",a[i]);
		memset(sol,0,sizeof(sol));
		memset(b,0,sizeof(b));
		for(j=1;j<=n;j++)
		{
			last=cur;
			cur=cur^1;
			go(1,0,0);
		}
		int max=0;
		for(i=0;i<(1<<m);i++)
			if(sol[cur][i]>max) max=sol[cur][i];
		printf("Case #%d: %d",k,max);
		printf("\n");
	}
	return 0;
}
