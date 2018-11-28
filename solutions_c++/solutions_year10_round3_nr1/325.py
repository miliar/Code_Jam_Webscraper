#include<stdio.h>
#define N 1000+10
int a[N];
int b[N];
bool intersect(int x,int y)
{
	if((a[x]-a[y])*(b[x]-b[y])>0)
		return false;
	return true;
}

int main()
{
	int n;
	int t;
	int ans;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	for(int i=1;i<=t;++i)
	{
		ans=0;
		scanf("%d",&n);
		for(int j=0;j<n;++j)
			scanf("%d%d",&a[j],&b[j]);
		for(int j=0;j<n;++j)
			for(int k=j+1;k<n;++k)
			{
				if(intersect(j,k))
					++ans;
			}
		printf("Case #%d: %d\n",i,ans);
	}

	return 0;
}