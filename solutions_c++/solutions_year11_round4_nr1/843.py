#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <math.h>
#include <vector>
#include <string.h>
#include <algorithm>

using namespace std;

int b[1000100],e[1000100],w[1000100];

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t,n,s,r,tt,i,j,tmp,kol,x;
	double res,temp,left;
	scanf("%d",&tt);
	for (int cnt=1;cnt<=tt;cnt++)
	{
		scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
		for (i=1;i<=n;i++)
			scanf("%d%d%d",&b[i],&e[i],&w[i]);
		b[0]=0;
		e[0]=0;
		w[0]=0;
		e[n+1]=x;
		b[n+1]=x;
		w[n+1]=0;
		kol=n+1;
		left=t;
		res=0;
		kol=n+1;
		for (i=1;i<=n+1;i++)
		{
			b[++kol]=e[i-1];
			e[kol]=b[i];
			w[kol]=0;
		}
		for (i=0;i<kol;i++)
			for (j=i+1;j<=kol;j++)
				if (w[i]>w[j])
				{
					tmp=w[i];
					w[i]=w[j];
					w[j]=tmp;
					tmp=b[i];
					b[i]=b[j];
					b[j]=tmp;
					tmp=e[i];
					e[i]=e[j];
					e[j]=tmp;
				}
		for (i=0;i<=kol;i++)
		{
			temp=min(left,(e[i]-b[i]+0.0)/(w[i]+r));
			res+=temp;
			left-=temp;
			res+=(e[i]-b[i]-temp*(w[i]+r))/(w[i]+s);
		}
		printf("Case #%d: %0.8llf\n",cnt,res);
	}
    system("PAUSE");
	return 0;
}