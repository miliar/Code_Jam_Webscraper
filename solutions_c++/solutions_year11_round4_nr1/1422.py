#include <iostream>
#include <algorithm>
using namespace std;
struct stu
{
	int x,su;
	bool operator <(const stu &t)const
	{
		return su<t.su;
	}
}arr[1001];
int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int T,cas;
	scanf("%d",&T);
	for(cas=1;cas<=T;cas++)
	{
		int x,s,r,n,len=0,st,en;
		double t;
		int i;
		scanf("%d %d %d %lf %d",&x,&s,&r,&t,&n);
		for(i=0;i<n;i++)
		{
			scanf("%d %d %d",&st,&en,&arr[i].su);
			len+=en-st;
			arr[i].x=en-st;
		}
		len=x-len;
		if(len!=0)
		{
			arr[n].x=len;
			arr[n].su=0;
			n++;
		}
		sort(arr,arr+n);
		double ans=0;
		for(i=0;i<n;i++)
		{
			double rt=double(arr[i].x)/(arr[i].su+r);
			if(rt>t)
			{
				ans+=t+( double(arr[i].x) - t*(arr[i].su+r) ) / (arr[i].su+s);
				t=0;
			}
			else
			{
				ans+=rt;
				t-=rt;
			}
		}
		printf("Case #%d: %.9lf\n",cas,ans);
	}
	return 0;
}