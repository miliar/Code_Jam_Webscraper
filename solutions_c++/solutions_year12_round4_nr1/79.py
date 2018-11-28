#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>

using namespace std;

int x[11000];
int y[11000];
int z[11000];

int main()
{
	int _cn,_cc,i,j,n,d,md,l;
	scanf("%d",&_cn);
	for (_cc=1;_cc<=_cn;++_cc)
	{
		scanf("%d",&n);
		for (i=0;i<n;++i) scanf("%d %d",x+i,y+i);
		scanf("%d",&d);
		z[0]=x[0];
		md=0;
		for (i=1;i<n;++i) z[i]=0;
		for (i=0;i<n;++i) 
		{
			if(x[i]+z[i]>md) md=x[i]+z[i];
			for (j=i+1;j<n;++j)
			{
				if (x[i]+z[i]<x[j]) break;
				l=x[j]-x[i];
				if (y[j]<l) l=y[j];
				if (z[j]<l) z[j]=l;
			}
		}
		printf("Case #%d: %s\n",_cc,md>=d?"YES":"NO");
	}
	return 0;
}
