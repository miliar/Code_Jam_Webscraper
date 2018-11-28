#include<iostream>
#include<algorithm>
using namespace std;
__int64 a[1002],b[1002],g[1002];
int n,m;
__int64 x,y,z;
void DP()
{
	int i,j;
	
	for(i=0;i<n;i++)
		g[i]=1;
	for(i=1;i<n;i++)
	{
		for(j=0;j<i;j++)
		{
			if(b[j]<b[i]) g[i]=(g[i]+g[j])%1000000007;	
		}
	}
	//cout<<g[n-1]<<endl;

}
int main()
{
	freopen("C-small-attempt0.in.txt","r",stdin);
	freopen("A.out","w",stdout);
	int i,T,t=1;
	__int64 sum;
	cin>>T;
	while(T--)
	{
		//cin>>n>>m>>x>>y>>z;
		scanf("%d%d%I64d%I64d%I64d",&n,&m,&x,&y,&z);
		sum=0;
		memset(g,0,sizeof(g));
		for(i=0;i<m;i++)
			scanf("%I64d",&a[i]);
		for(i=0;i<n;i++)
		{
			b[i]=a[i%m];
		//	printf("%I64d ",b[i]);
			a[i%m] = (x*a[i%m]+y*(i+1))%z;

		}
		DP();
		for(i=0;i<n;i++)
			sum=(sum+g[i])%1000000007;
		printf("Case #%d: %I64d\n",t++,sum);
	}

return 0;
}