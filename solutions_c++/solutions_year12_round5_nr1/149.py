#include<stdio.h>
#include<string.h>
#include<algorithm>
struct level
{
	int t,p,k;
};
bool operator <(const level &a,const level &b)
{
	int temp1,temp2;
	temp1=a.t*100+b.t*a.p;
	temp2=b.t*100+a.t*b.p;
	if (temp1!=temp2)
		return temp1<temp2;
	else
		return a.k<b.k;
}
level a[1000];
int main()
{
	int t,tt,n,i;
	scanf("%d",&t);
	for (tt=1;tt<=t;tt++)
	{
		scanf("%d",&n);
		for (i=0;i<n;i++)
		{
			scanf("%d",&a[i].t);
			a[i].k=i;
		}
		for (i=0;i<n;i++)
		{
			scanf("%d",&a[i].p);
			a[i].p=100-a[i].p;
		}
		std::sort(a,a+n);
		printf("Case #%d:",tt);
		for (i=0;i<n;i++)
			printf(" %d",a[i].k);
		printf("\n");
	}
	return 0;
}
