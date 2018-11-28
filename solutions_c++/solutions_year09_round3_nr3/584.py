#include<iostream>
using namespace std;
int a[6];
int n,p;
int hash[6];
int mmin;
void dfs(int *q,int m)
{
	int i,j;
	if(m==p)
	{
		int k[101]={0};
		int sum=0;
		for(i=0;i<m;i++)
		{
			k[q[i]]=1;
			for(j=q[i]+1;j<=n;j++)
			{
				if(k[j]==1)
					break;
				sum++;
			}
			for(j=q[i]-1;j>0;j--)
			{
				if(k[j]==1)
					break;
				sum++;
			}
		}
		if(sum<mmin)
			mmin=sum;
		return ;
	}

	for(i=0;i<p;i++)
	{
		if(hash[i]==0)
		{
			hash[i]=1;
			q[m]=a[i];
			dfs(q,m+1);
			hash[i]=0;
		}
	}
	return ;
}
int main()
{
	int t,tt;
	tt=0;
	int i,j;
	freopen("C-small-attempt4.in","r",stdin);
	freopen("ourrrrrrt.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		tt++;
		scanf("%d %d",&n,&p);
		for(i=0;i<p;i++)
		{
			scanf("%d",&a[i]);
		}
		memset(hash,0,sizeof(hash));

		mmin=99999999;
		int x[6];
		dfs(x,0);
		printf("Case #%d: %d\n",tt,mmin);

	}
	return 0;
	
}