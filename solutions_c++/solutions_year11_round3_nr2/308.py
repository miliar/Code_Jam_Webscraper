#include<stdio.h>
#include<algorithm>
using namespace std;

int L,N,C;
long long t,ans;
int a[1000001];
long long b[1000001],c[1000001];


int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int Cas=1;Cas<=T;Cas++)
	{	
		printf("Case #%d: ",Cas);
		scanf("%d%I64d%d%d",&L,&t,&N,&C);
		for (int i=0;i<C;i++) 
		{
			scanf("%d",&a[i]);
			if (i==0)
				b[i]=a[i];
			else
				b[i]=b[i-1]+a[i];
		}

		ans=b[C-1]*(N/C);
		if (N%C!=0)
			ans+=b[N%C-1];
		ans*=2;

		long long s=(t/(b[C-1]*2))*C;
		long long t1=t%(b[C-1]*2);
		int i=0;
		while (t1>=a[i]*2)
		{
			t1-=a[i]*2;
			s++;
			i++;
		}
		int cnt=1;
		c[0]=a[s%C]-t1/2;
		for (i=s+1;i<N;i++)
			c[cnt++]=a[i%C];
		if (L>=cnt)
		{
			for (int i=0;i<cnt;i++)
				ans-=c[i];
		}
		else
		{
			sort(c,c+cnt);
			for (int i=cnt-1;i>=cnt-L;i--)
				ans-=c[i];
		}

		printf("%I64d\n",ans);

	}
}