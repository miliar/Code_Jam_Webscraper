#include<cstdio>
#include<algorithm>
using namespace std;
struct node
{
	long long p,v;
}f[205];
int mt,t,n,d,i,j;
long long sumv;
int main()
{
	//freopen("B3.in","r",stdin);
	//freopen("B3.out","w",stdout);
	scanf("%d",&t);
	for(mt=1;mt<=t;mt++)
	{
		scanf("%d%d",&n,&d);
		sumv=0;
		for(i=0;i<n;i++) 
		{
			scanf("%lld%lld",&f[i].p,&f[i].v);
			//printf("%lld %lld\n",f[i].p,f[i].v);
			sumv+=f[i].v;
		}
		double maxt=0;
		for(i=1;i<n;i++) 
		{
			long long td=(f[i-1].v-1)*d;
			double ti=1.0*td/2;
			maxt=max(maxt,ti);
		}
		printf("Case #%d: %.12f\n",mt,maxt);
	}
}
