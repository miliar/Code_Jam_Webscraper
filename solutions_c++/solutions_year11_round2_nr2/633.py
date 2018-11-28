#include<iostream>
#include<algorithm>
#include<math.h>
using namespace std;
#define eps 1e-8
int p,num,a[100005],l,d;
bool check(double mid)
{
	double x=a[0]-mid;
	int i;
	for(i=1;i<l;i++)
	{
		x+=d;
		if(x<a[i]-mid)
			x=a[i]-mid;
		if(x>a[i]+mid)
			return false;
	}
	return true;
}
int main()
{
	int cas,n,i,j;
	double low,high,mid;
	//freopen("Bs.in","r",stdin);
	//freopen("2.txt","w",stdout);
	scanf("%d",&cas);
	for(int ii=1;ii<=cas;ii++)
	{
		printf("Case #%d: ",ii);
		scanf("%d%d",&n,&d);
		l=0;
		for(i=0;i<n;i++)
		{
			scanf("%d%d",&p,&num);
			for(j=0;j<num;j++)
				a[l++]=p;
		}
		low=0;high=1e10;
		while(low+eps<high)
		{
			mid=(low+high)/2;
			if(check(mid))
				high=mid;
			else
				low=mid;
		}
		printf("%.8lf\n",low);
	}
	return 0;
}