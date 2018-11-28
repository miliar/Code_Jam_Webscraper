#include<math.h>
#include<stdio.h>
#include<algorithm>
using namespace std;
struct plants{
	double x;
	double y;
	double r;
}a[50];
int n;
double f(int i)
{
	return (sqrt((a[i].x-a[(i+1)%n].x)*(a[i].x-a[(i+1)%n].x)
		+(a[i].y-a[(i+1)%n].y)*(a[i].y-a[(i+1)%n].y))+a[i].r+a[(i+1)%n].r)/2;
}
int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int i,t,tt=1;
	double ans;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%lf%lf%lf",&a[i].x,&a[i].y,&a[i].r);
		printf("Case #%d: ",tt++);
		if(n==1)
		{
			printf("%lf\n",a[0].r);
			continue;
		}
		if(n==2)
		{
			printf("%lf\n",max(a[0].r,a[1].r));
			continue;
		}
		ans=1000000000;
		for(i=0;i<n;i++)
		{
			if(ans>max(f(i),a[(i+2)%n].r))
				ans=max(f(i),a[(i+2)%n].r);
		}
		printf("%lf\n",ans);
	}
	return 0;
}
