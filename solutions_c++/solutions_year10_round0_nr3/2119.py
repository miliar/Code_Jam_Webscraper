#include <cstdio>
using namespace std;
const int maxn=1100;
int r,k,n,m;
int g[maxn];
long long v[maxn];
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		scanf("%d%d%d",&r,&k,&n);
		long long sum=0;
		for(int j=0;j<n;j++)
		{
			scanf("%d",&g[j]);
			sum+=g[j];
		}
		if((long long)k>sum) k=sum;
		int j=0,l=0;
		for(m=0;m==0||j>0;m++)
		{
			v[m]=0;
			while(true)
			{
				if(v[m]+g[l]>(long long)k) break;
				v[m]+=g[l];
				l++;
				if(l==n) l=0;
			}
			j=l;
		}
		for(int j=m;j>0;j--) v[j]=v[j-1];
		v[0]=0;
		for(int j=1;j<=m;j++) v[j]+=v[j-1];
		long long ans=r/m*v[m]+v[r%m];
		printf("Case #%d: %I64d\n",i,ans);
	}
	return 0;
}
