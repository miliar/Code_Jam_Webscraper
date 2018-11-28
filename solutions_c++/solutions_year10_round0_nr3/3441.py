#include <cstdio>
#include <cstring>
int g[100001];
int main()
{
	freopen("3.in","r",stdin);
	freopen("3.out","w",stdout);
	int c;
	scanf("%d",&c);
	for(int i=1;i<=c;++i)
	{
		int r,k,n,lp=0,rp,ans=0;
		scanf("%d%d%d",&r,&k,&n);
		for(int j=0;j<n;++j)
			scanf("%d",g+j);
		rp=n;
		for(int j=0;j<r;++j)
		{
			int capa=k,ptr=0;
			while(ptr<n&&capa>=g[ptr+lp])
			{
				capa-=g[ptr+lp];
				ans+=g[ptr+lp];++ptr;
			}
			memcpy(g+rp,g+lp,ptr*sizeof(int));
			rp+=ptr;lp+=ptr;
		}
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}
