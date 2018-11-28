#include<cstdio>


int main()
{
	freopen("in","rt",stdin);
	freopen("out","wt",stdout);

	int T;
	scanf("%d",&T);

	for (int t=0; t<T; t++)
	{
		int l,r,c;
		scanf("%d%d%d",&l,&r,&c);
		
		int k=0;
		while (l*c<r)
		{
			r=(r+c-1)/c;
			k++;
		}

		int d=1,ans=0;
		while (d<=k)
		{
			ans++;
			d*=2;
		}

		printf("Case #%d: %d\n",t+1,ans);

	}

	return 0;
}