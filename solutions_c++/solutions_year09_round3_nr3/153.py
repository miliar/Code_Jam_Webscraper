#include<stdio.h>

int n,m,p[101],d[101][101],ans;

int f(int l,int r)
{
	int i,s=-1,t,min=2100000000,x;
	for(i=0;i<n;i++)
	{
		if(l<=p[i] && p[i]<=r)
		{
			if(s==-1) s=i;
			t=i;
		}
	}
	if(s==-1) return 0;
	if(d[s][t]>0) return d[s][t];
	for(i=s;i<=t;i++)
	{
		x=f(l,p[i]-1)+f(p[i]+1,r)+r-l;
		if(x<min) min=x;
	}
	d[s][t]=min;
	return min;
}

void process()
{
	int i,j;
	ans=210000000;
	for(i=0;i<n;i++) for(j=0;j<n;j++) d[i][j]=0;
	ans=f(1,m);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j,t;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d%d",&m,&n);
		for(j=0;j<n;j++)
		{
			scanf("%d",&p[j]);
		}
		process();
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}