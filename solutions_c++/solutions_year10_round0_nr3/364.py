#include <iostream>
using namespace std;

int main()
{
	int t,r,k,n,g[1111],f[1111],p[1111],w[1111];
	long long e[1111];
	scanf("%d",&t);
	for (int i=0;i<t;i++)
	{
		memset(w,0,sizeof(w));
		memset(e,0,sizeof(e));
		scanf("%d%d%d",&r,&k,&n);
		for (int j=0;j<n;j++)
		{
			scanf("%d",g+j);
		}
		long long sum=0;
		for (int h=0;h<n;h++)
		{
			f[h]=0;
			p[h]=h;
			for (int d=0;d<n;d++)
			{
				if (f[h]+g[(h+d)%n]<=k)
				{
					f[h]+=g[(h+d)%n];
				}
				else
				{
					p[h]=(h+d)%n;
					break;
				}
			}
		}
		int z=0,R=r;
		for (;r>0;r--)
		{
			if (w[z])
				break;
			e[z]=sum;
			w[z]=r;
			sum+=f[z];
			z=p[z];
		}
		if (r)
		{
			sum=e[z]+(sum-e[z])*(r/(w[z]-r)+1);
			r=r%(w[z]-r);
			for (;r>0;r--)
			{
				sum+=f[z];
				z=p[z];
			}
		}
		printf("Case #%d: %lld\n",i+1,sum);
	}
	return 0;
}