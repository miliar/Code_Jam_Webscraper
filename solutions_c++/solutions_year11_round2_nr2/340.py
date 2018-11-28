#include<stdio.h>
#include<algorithm>
using namespace std;
int n,m,d;
__int64 a[1000010],na[1000010];
int min(int a,int b)
{
	if(a<b)return a;
	return b;
}
int max(int a,int b)
{
	if(a>b)return a;
	return b;
}
int main()
{
	int test,i,j,T=1;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&test);
	for(;test>0;test--)
	{
		scanf("%d %d",&n,&d);
		memset(a,0,sizeof(a));
		for(i=m=0;i<n;i++)
		{
			int p,v;
			scanf("%d %d",&p,&v);
			for(;v>0;v--)
			{
				a[m++]=p*2;
			}
		}
		d*=2;
		sort(a,a+m);
		__int64 l,r,md,ans=-1;
		l=0;r=10000000000000;
		while(l<=r)
		{
			md=(l+r)/2;
			na[0]=a[0]-md;
			for(i=1;i<m;i++)
			{
				if(na[i-1]+d<a[i])
				{
					na[i]=a[i]-md;
					if(na[i]<na[i-1]+d)
						na[i]=na[i-1]+d;
				//	printf("%d,%d %d %d] ",na[i],a[i],na[i-1],d);
				}
				else if(na[i-1]+d>a[i])
				{
					na[i]=a[i]+md;
					if(na[i]>na[i-1]+d)
						na[i]=na[i-1]+d;
					else if(na[i]<na[i-1]+d)
					{
						i=-1;
						break;
					}
				//	printf("%d,%d %d %d] ",na[i],a[i],na[i-1],d);
				}
				else
				{
					na[i]=a[i];
				//	printf("%d %d %d %d))",na[i],a[i],na[i-1],d);
				}
			}
			if(i!=-1)
			{
				ans=md;
				r=md-1;
			}
			else
			{
				l=md+1;
			}
		}
		printf("Case #%d: %.1lf\n",T++,(double)ans/2);
	}
	return 0;
}