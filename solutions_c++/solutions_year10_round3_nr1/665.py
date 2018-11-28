#include<cstdio>

int cmp(int x,int y)
{
	if (x<y) return 1;
	if (x>y) return -1;
	return 0;
}

int a[2000],b[2000];
int main()
{
	freopen("in","rt",stdin);
	freopen("out","wt",stdout);

	int T;
	scanf("%d",&T);
	
	for (int t=0; t<T; t++)
	{
		int ans=0,n;
		scanf("%d",&n);

		for (int i=0; i<n; i++)
		{
			scanf("%d%d",&a[i],&b[i]);

			for (int j=0; j<i; j++)
			{
				if (cmp(a[i],a[j])*cmp(b[i],b[j])<0) ans++;
			}
		}

		printf("Case #%d: %d\n",t+1,ans);
	}
	
	return 0;
}