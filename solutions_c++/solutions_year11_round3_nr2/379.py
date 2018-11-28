#include <stdio.h>
#include <algorithm>
#include <string.h>
using namespace std;
long long a[1000010];
long long sum[1000010];
int c[1010];
int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("out1.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int _=1;_<=T;_++)
	{
		int L,N,C;
		long long t;
		memset(a,0,sizeof(a));
		memset(sum,0,sizeof(sum));
		scanf("%d%lld%d%d",&L,&t,&N,&C);
		int i;
		for(i=0;i<C;i++)
			scanf("%d",&c[i]);
		printf("Case #%d: ",_);
		for(i=1;i<=N;i++)
		{
			a[i]=c[(i-1)%C];
		}
		sum[0]=a[0];
		int tmp=-1;
		for(i=1;i<=N;i++)
		{
			sum[i]=sum[i-1]+a[i];
			if(sum[i]*2>=t&&sum[i-1]*2<t)
				tmp=i-1;
		}
		if(L==0)
		{
			printf("%lld\n",sum[N]*2);
			continue;
		}
		if(t==0)
		{
			printf("%lld\n",sum[N]);
			continue;
		}
		if(tmp==-1)
		{
			printf("%lld\n",sum[N]*2);
			continue;
		}
		a[tmp]+=(t/2-sum[tmp]);
		a[tmp+1]-=(t/2-sum[tmp]);
		sum[tmp]=t/2;
		sort(a+tmp+1,a+N+1);
		long long ans=sum[N]*2;
		int j=N;
		for(i=L;i>0&&j>tmp;i--,j--)
		{
			ans-=a[j];
		}
		printf("%lld\n",ans);
	}
	return 0;
}