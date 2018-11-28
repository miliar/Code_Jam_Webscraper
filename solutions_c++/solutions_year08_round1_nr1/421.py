#include<cstdio>
#include<algorithm>
using namespace std;
typedef __int64 ll;
ll x[1005],y[1005];
ll sum;
bool ok;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,cc,n,i,j;
	ll tmp;
	scanf("%d",&t);
	for(cc=1;cc<=t;cc++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)scanf("%I64d",&x[i]);
		for(i=0;i<n;i++)scanf("%I64d",&y[i]);
		while(true)
		{
			ok=0;
			for(i=0;i<n;i++)
				for(j=i+1;j<n;j++)
				{
					if(x[i]*y[i]+x[j]*y[j]>x[i]*y[j]+x[j]*y[i])
					{
						tmp=x[i];
						x[i]=x[j];
						x[j]=tmp;
						ok=1;
					}
				}
			if(ok==0)break;
		}
		sum=0;
		for(i=0;i<n;i++)
		sum=sum+x[i]*y[i];
		printf("Case #%d: %I64d\n",cc,sum);
	}
	return 0;
}
					
		

