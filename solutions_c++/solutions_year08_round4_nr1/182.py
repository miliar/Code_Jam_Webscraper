#include <iostream>
using namespace std;

struct gao
{
	bool f;
	int g,c; //1 AND others OR
	int a[2];
}a[40000];

int n,m,v;

void solve(int x)
{
	if(a[x].f)
	{
		solve(2*x);
		solve(2*x+1);
		if(a[x].g==1)
		{
			if(a[x].a[0]>a[2*x].a[0]+a[2*x+1].a[1])
				a[x].a[0]=a[2*x].a[0]+a[2*x+1].a[1];
			if(a[x].a[0]>a[2*x].a[1]+a[2*x+1].a[0])
				a[x].a[0]=a[2*x].a[1]+a[2*x+1].a[0];
			if(a[x].a[0]>a[2*x].a[0]+a[2*x+1].a[0])
				a[x].a[0]=a[2*x].a[0]+a[2*x+1].a[0];
			if(a[x].a[1]>a[2*x].a[1]+a[2*x+1].a[1])
				a[x].a[1]=a[2*x].a[1]+a[2*x+1].a[1];
			if(a[x].c==1)
			{
				if(a[x].a[1]>a[2*x].a[0]+a[2*x+1].a[1]+1)
					a[x].a[1]=a[2*x].a[0]+a[2*x+1].a[1]+1;
				if(a[x].a[1]>a[2*x].a[1]+a[2*x+1].a[0]+1)
					a[x].a[1]=a[2*x].a[1]+a[2*x+1].a[0]+1;
				if(a[x].a[0]>a[2*x].a[0]+a[2*x+1].a[0]+1)
					a[x].a[0]=a[2*x].a[0]+a[2*x+1].a[0]+1;
				if(a[x].a[1]>a[2*x].a[1]+a[2*x+1].a[1]+1)
					a[x].a[1]=a[2*x].a[1]+a[2*x+1].a[1]+1;
			}
		}
		else
		{
			if(a[x].a[1]>a[2*x].a[0]+a[2*x+1].a[1])
				a[x].a[1]=a[2*x].a[0]+a[2*x+1].a[1];
			if(a[x].a[1]>a[2*x].a[1]+a[2*x+1].a[0])
				a[x].a[1]=a[2*x].a[1]+a[2*x+1].a[0];
			if(a[x].a[0]>a[2*x].a[0]+a[2*x+1].a[0])
				a[x].a[0]=a[2*x].a[0]+a[2*x+1].a[0];
			if(a[x].a[1]>a[2*x].a[1]+a[2*x+1].a[1])
				a[x].a[1]=a[2*x].a[1]+a[2*x+1].a[1];
			if(a[x].c==1)
			{
				if(a[x].a[0]>a[2*x].a[0]+a[2*x+1].a[1]+1)
					a[x].a[0]=a[2*x].a[0]+a[2*x+1].a[1]+1;
				if(a[x].a[0]>a[2*x].a[1]+a[2*x+1].a[0]+1)
					a[x].a[0]=a[2*x].a[1]+a[2*x+1].a[0]+1;
				if(a[x].a[0]>a[2*x].a[0]+a[2*x+1].a[0]+1)
					a[x].a[0]=a[2*x].a[0]+a[2*x+1].a[0]+1;
				if(a[x].a[1]>a[2*x].a[1]+a[2*x+1].a[1]+1)
					a[x].a[1]=a[2*x].a[1]+a[2*x+1].a[1]+1;
			}
		}
	}
}

int main()
{
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
	int i,j,x;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		printf("Case #%d: ",i);
		scanf("%d%d",&m,&v);
		for(j=1;j<=(m-1)/2;j++)
		{
			scanf("%d%d",&a[j].g,&a[j].c);
			a[j].f=true;
			a[j].a[0]=a[j].a[1]=99999999;
		}
		for(j;j<=m;j++)
		{
			scanf("%d",&x);
			a[j].f=false;
			a[j].a[(x+1)%2]=99999999;
			a[j].a[x]=0;
		}
		solve(1);
		if(a[1].a[v]==99999999)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",a[1].a[v]);
	}
	return 0;
}