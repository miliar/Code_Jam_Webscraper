#include <iostream>
using namespace std;

int a[1001];
int b[1001];
int c[1001];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int nn;
	int i,j,n,m,k,x,y,z;
	scanf("%d",&nn);
	for(k=1;k<=nn;k++)
	{
		printf("Case #%d: ",k);
		scanf("%d%d%d%d%d",&n,&m,&x,&y,&z);
		for(i=0;i<m;i++)
			scanf("%d",&a[i]);
		for(i=0;i<n;i++)
		{
			b[i]=a[i%m];
			a[i%m]=((__int64)x*(__int64)a[i%m]+(__int64)y*(__int64)(i+1))%z;
		}
		for(i=0;i<n;i++)
			c[i]=1;
		for(i=1;i<n;i++)
			for(j=0;j<i;j++)
			{
				if(b[j]<b[i])
					c[i]=(c[i]+c[j])%1000000007;
			}
		int t=0;
		for(i=0;i<n;i++)
		{
			t=(t+c[i])%1000000007;
		}
		printf("%d\n",t);	
	}
	return 0;
}