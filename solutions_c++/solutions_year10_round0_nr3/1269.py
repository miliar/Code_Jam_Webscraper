#include <cstdio>
#include <cstring>
using namespace std;

int r,k,n;
int a[2200];
int v[2200];
long long ans,ans0[2200];

int next(int p0)
{
	int l=k,p=p0;
	while(p<n+p0 && l>=a[p])l-=a[p++];
	ans+=k-l;
	return p;
}


int main()
{
	int t;
	scanf("%d",&t);
	for(int t1=1;t1<=t;++t1)
	{
		scanf("%d %d %d",&r,&k,&n);
		for(int i=0;i<n;++i)
		{
			scanf("%d",&a[i]);
			a[n+i]=a[i];
		}
		int p=0;
		ans=0;
		memset(v,0,sizeof(v));
		for(int i=1;i<=r;++i)
		{
			p=next(p)%n;
			if(v[p])
			{
				ans-=ans0[v[p]];
				ans*=(r-v[p])/(i-v[p]);
				ans+=ans0[v[p]+(r-v[p])%(i-v[p])];
				break;
			}
			v[p]=i;
			ans0[i]=ans;
		}
		printf("Case #%d: %Ld\n",t1,ans);
	}
	return 0;
}



