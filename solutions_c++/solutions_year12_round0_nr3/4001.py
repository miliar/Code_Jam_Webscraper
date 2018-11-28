#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
int ans;
int y[10];

void dfs(int a,int b)
{
	int i,j,u,v,m,len,x;
	for(i=a;i<=b;i++)
	{
		memset(y,0,sizeof(y));
		len=log10((double)i)+1;
		for(j=1,u=1;j<=len;j++) u*=10;
		for(j=1,v=10;j<len;j++,v*=10)
		{
			x=i%v;
			x*=(u/v);
			x+=(i/v);
			for(m=0;y[m];m++)
				if(y[m]==x) break;
			if(y[m]==0&&x>i&&x<=b) 
			{
				ans++;
				y[m]=x;
			}
		}
	}
}

int main()
{
	freopen("C-large.in","r",stdin);
    freopen("small.txt","w",stdout);
	int t,k=1;
	scanf("%d",&t);
	while(t--)
	{
		int a,b;
		ans=0;
		scanf("%d %d",&a,&b);
		dfs(a,b);
		printf("Case #%d: %d\n",k++,ans);
	}
	return 0;
}
