#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>

using namespace std;

const int split=512;

int main()
{
	int _cn,_cc,i,j,k,p,n,ll;
	double w,l;
	double r[1024],x[1024],y[1024];
	scanf("%d",&_cn);
	for (_cc=1;_cc<=_cn;++_cc)
	{
		scanf("%d %lf %lf",&n,&w,&l);
		for (i=0;i<n;++i) scanf("%lf",r+i);
		printf("Case #%d: ",_cc);
		ll=0;
		for (i=0;i<n;++i)
		{
			for (j=0;j<=split;++j) 
			{
				for (k=0;k<=split;++k)
				{
					x[i]=j*w/(double)split;
					y[i]=k*l/(double)split;
					for (p=0;p<i;++p) if ((x[i]-x[p])*(x[i]-x[p])+(y[i]-y[p])*(y[i]-y[p])<(r[i]+r[p]+1e-8)*(r[i]+r[p])) break;
					if (p==i) 
					{
						++ll;
						break;
					}
				}
				if (k<=split) break;
			}
			printf("%.10lf %.10lf ",x[i],y[i]);
		}
		if (ll!=n) { exit(EXIT_FAILURE); }
		printf("\n");
	}
	return 0;
}
