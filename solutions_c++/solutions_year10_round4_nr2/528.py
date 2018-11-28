#include <cstdio>
#include <algorithm>
using namespace std;
const int maxp=10;
const int maxn=1<<maxp;
int m[maxn];
int c[maxn*2];
int p,n;
int f[maxn*2][maxp+1];
void init()
{
	scanf("%d",&p);
	n=1<<p;
	for(int i=0;i<n;i++)
		scanf("%d",&m[i]);
	int base=n/2;
	for(int i=0;i<p;i++)
	{
		//printf("base=%d\n",base);
		for(int j=0;j<(1<<(p-i-1));j++)
			scanf("%d",&c[base+j]);
		base/=2;
	}
}
int solve()
{
	memset(f,255,sizeof(f));
	for(int i=0;i<n;i++)
	{
		for(int j=p-m[i];j<=p;j++) f[i+n][j]=0;
	}
	//puts("?????");
	int base=n/2;
	for(int i=0;i<p;i++)
	{
		//printf("i=%d base=%d\n",i,base);
		for(int j=0;j<(1<<(p-i-1));j++)
		{
			int z=base+j;
			f[z][p]=0;
			for(int k=0;k<p;k++)
			{
				int t=k>0?f[z][k-1]:-1;
				if(f[z*2][k+1]>=0&&f[z*2+1][k+1]>=0)
				{
					int tmp=f[z*2][k+1]+f[z*2+1][k+1]+c[z];
					if(t<0||t>tmp) t=tmp;
				}
				if(f[z*2][k]>=0&&f[z*2+1][k]>=0)
				{
					int tmp=f[z*2][k]+f[z*2+1][k];
					if(t<0||t>tmp) t=tmp;
				}
				f[z][k]=t;
				//printf("%d,%d %d\n",z,k,t);
			}
		}
		base/=2;
	}
	return f[1][0];
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		init();
		printf("Case #%d: %d\n",i,solve());
	}
	return 0;
}
