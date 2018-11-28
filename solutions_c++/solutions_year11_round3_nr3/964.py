#include <cstdio>
#include <cstdlib>
int main()
{
	int t,r,c,ti,i,j,n,l,h,ans;
	int f[111];
	freopen("d:\\gcj\\r1c\\C-small-attempt1.in","r",stdin);
	freopen("d:\\gcj\\r1c\\cout.txt","w",stdout);
	scanf("%d",&t);
	for (ti=0;ti<t;ti++)
	{
		scanf("%d%d%d",&n,&l,&h);
		ans=-1;
		for (i=0;i<n;i++)
		{
			scanf("%d",&f[i]);
		}
		for (i=l;i<=h;i++)
		{
			int cov=1;
			for (j=0;j<n;j++)
			{
				if (i%f[j]!=0 && f[j]%i!=0)
				{
					cov=0; break;
				}
			}
			if (cov)
			{
				ans=i;
				break;
			}
		}
		printf("Case #%d: ",ti+1);
		if (ans==-1) printf("NO\n");
		else
		{
			printf("%d\n",ans);
		}
	}


	return 0;
}

