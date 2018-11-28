#include <stdio.h>
int ans,n,a[12];

void dfs(int l,int r)
{
	bool flag=0;
	for(int i=l;i<=r;i++)	
	{
		a[i]++;
		if (a[i]<=n) flag=1;
	}
	if (flag) 
	{
		ans++;
		dfs(l,(l+r)/2);
		dfs((l+r)/2+1,r);
	}
}



int main()
{
	int t;
	int now[11];

	freopen("D:\\ACM\\Google\\B-small-attempt1.in","r",stdin);
	freopen("D:\\ACM\\Google\\B-small-attempt1.out","w",stdout);
    now[0]=1;
	for(int i=1;i<=10;i++) now[i]=now[i-1]*2;
	scanf("%d",&t);
	for(int ll=1;ll<=t;ll++)
	{
		scanf("%d",&n);
		for(int i=1;i<=now[n];i++) scanf("%d",&a[i]);
		for(int i=n-1;i>=0;i--)
			for(int j=1;j<=now[i];j++) scanf("%*d");
		ans=0;
		dfs(1,now[n]);
		printf("Case #%d: %d\n",ll,ans);
	}
	return 0;
}

