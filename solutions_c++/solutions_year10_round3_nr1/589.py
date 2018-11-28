#include<cstdio>
int a[1010],b[1010];
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int c=1;c<=t;++c)
	{
		int n,count=0;
		scanf("%d",&n);
		for(int i=0;i<n;++i)
		{
			scanf("%d%d",&a[i],&b[i]);
			for(int j=0;j<i;++j)
			if((a[i]-a[j])*(b[i]-b[j])<0)
				++count;
		}
		printf("Case #%d: %d\n",c,count);
	}
	return 0;
}
