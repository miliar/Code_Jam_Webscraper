#include<stdio.h>
#include<memory.h>

int n,v;
int g[10001],c[10001],value[10001];
int f[10001][2];

int cal(int root)
{
	if(value[root]!=-1) return value[root];
	
	if(g[root]==1)
	{
		return value[root]=(cal(root*2)&cal(root*2+1));
	}
	else 
	{
		return value[root]=(cal(root*2)|cal(root*2+1));
	}
}

int fmin(int a,int b)
{
	if(a<b) return a;
	else return b;
}

int dp(int root,int v)
{
	if(value[root]==v) return 0;
	if(f[root][v]!=-1) return f[root][v];
	if(root*2>n) return f[root][v]=1e9;

	int res1,res2;
	//and
	int t1=dp(root*2,1);
	int t2=dp(root*2+1,1);

	int t3=dp(root*2,0);
	int t4=dp(root*2+1,0);

	if(v==1) res1=t1+t2;
	else res1=fmin(t3,t4);
	//or
	if(v==1) res2=fmin(t1,t2);
	else res2=t3+t4;
		
	int res;
	if(c[root]==1)
	{
		if(g[root]==1) res=fmin(res1,res2+1);
		else res=fmin(res1+1,res2);
	}
	else
	{
		if(g[root]==1) res=res1;
		else res=res2;
	}

	f[root][v]=res;
	if(f[root][v]>=1e9) f[root][v]=1e9;
	return f[root][v];
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int T1,T,i,j;
	scanf("%d",&T);
	for(T1=1;T1<=T;T1++)
	{
		scanf("%d%d",&n,&v);
		
		memset(c,0,sizeof(c));
		memset(value,-1,sizeof(value));
		for(i=1;i<=n/2;i++)
		{
			scanf("%d%d",&g[i],&c[i]);			
		}
		for(;i<=n;i++)
		{
			scanf("%d",&value[i]);
		}

		memset(f,-1,sizeof(f));
		cal(1);
		int ans=dp(1,v);

		if(ans==1e9) printf("Case #%d: IMPOSSIBLE\n",T1);
		else printf("Case #%d: %d\n",T1,ans);
	}
	return 0;
}
