#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<map>
#include<algorithm>
using namespace std;

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C--output.txt","w",stdout);
	int T,n,c[16],i,j,k=0,xor,min,sum;
	scanf("%d",&T);
	while(T--)
	{
		sum=0;
		min=10000000;
		k++;
		xor=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d",&c[i]);
			xor=xor^c[i];
			if(c[i]<min)
				min=c[i];
			sum+=c[i];
		}
		if(xor!=0)printf("Case #%d: NO\n",k);
		else printf("Case #%d: %d\n",k,sum-min);
	}
	return 0;
}