#include<stdio.h>
#include<string.h>
#define N 100
int m,n,match[N],p[N][N];
bool temp[N],g[N][N];
bool f(int i,int j)
{
	int k;
	for(k=0;k<m;k++)
		if(p[i][k]<=p[j][k])
			return false;
	return true;
}
bool hungary_aug(int i)
{
	int j,v;
	for(j=0;j<n;j++)if(g[i][j]&&!temp[j])
	{
		temp[j]=true;
		v=match[j];
		match[j]=i;
		if(v==-1||hungary_aug(v))return true;
		match[j]=v;
	}
	return false;
}
int hungary()
{
	int i,k=0;
	memset(match,-1,sizeof(match));
	for(i=0;i<n;i++){
		memset(temp,false,sizeof(temp));
		k+=hungary_aug(i);
	}
	return k;
}
int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int i,j,t,tt=1;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d %d",&n,&m);
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				scanf("%d",&p[i][j]);
		memset(g,false,sizeof(g));
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				if(i!=j&&f(j,i))
					g[i][j]=true;
		printf("Case #%d: %d\n",tt++,n-hungary());
	}
	return 0;
}
