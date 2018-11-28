#include <stdio.h>
#include <algorithm>

using namespace std;

int p,k,l;
double array[1001];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j,m;
	scanf("%d",&m);
	for(int M=1;M<=m;M++)
	{
		scanf("%d%d%d",&p,&k,&l);
		for(i=0;i<l;i++)
			scanf("%lf",&array[i]);
		sort(array,array+l);
		for(i=0;i<l/2;i++)
			swap(array[i],array[l-i-1]);
		double ans=0;
		for(i=0,j=0;i<l;i++)
		{
			if(i%k==0)
				j++;
			ans+=array[i]*j;
		}
		printf("Case #%d: %.0lf\n",M,ans);
	}
	return 0;
}