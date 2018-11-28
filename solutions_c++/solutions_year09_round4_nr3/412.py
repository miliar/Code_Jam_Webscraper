#include<stdio.h>

int n,k,p[20][30],ans,g[20][20],K,path[20],F,c[20];

void back(int l)
{
	int i,j;
	if(l==K)
	{
		int f=1;
		for(i=0;i<l;i++)
		{
			for(j=i+1;j<l;j++)
			{
				if(g[path[i]][path[j]]==0) f=0;
			}
		}
		if(f==1) F=1;
		return;
	}
	i=0;
	if(l>0) i=path[l-1]+1;
	for(;i<n;i++)
	{		
		if(c[i]==0)
		{
			c[i]=1;
			path[l]=i;
			back(l+1);
			c[i]=0;
		}
	}
}

int process()
{
	int i,j,l,a,b;
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			g[i][j]=0;
			for(l=0;l<k;l++)
			{
				if(p[i][l]==p[j][l]) g[i][j]=1;
				if(l>0)
				{
					a=p[i][l]-p[j][l]; b=p[i][l-1]-p[j][l-1];
					if((a<0 && b>0) || (a>0 && b<0)) g[i][j]=1;
				}
			}
		}
	}
	int ans;
	for(i=1;i<=n;i++)
	{
		F=0;
		K=i;
		back(0);
		if(F==1)
		{
			ans=K;
		}
	}
	return ans;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j,l,t,res;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d%d",&n,&k);
		for(j=0;j<n;j++)
		{
			for(l=0;l<k;l++)
			{
				scanf("%d",&p[j][l]);
			}
		}
		res=process();
		printf("Case #%d: %d\n",i,res);
	}
	return 0;
}