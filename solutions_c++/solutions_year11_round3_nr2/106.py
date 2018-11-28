#include<cstdio>
#include<algorithm>
using namespace std;
long long int l,t,n,c,a[1000100]={0},num[1000001]={0},total[1000001]={0};
int main()
{
	int test,tt=0,i;
	scanf("%d",&test);
	while(test--)	
	{
		scanf("%lld%lld%lld%lld",&l,&t,&n,&c);
		for(i=0;i<c;i++)
			scanf("%lld",&a[i]);
		int j=0;
		for(i=0;i<n;i++)
		{
			num[i]=a[j];
			if(i>0)
				total[i]=total[i-1]+num[i];
			else
				total[i]=num[i];
			j++;
			if(j==c)
				j=0;
		}
		long long int i,k,time=0;
		for(i=0;i<n;i++)
		{
			time+=num[i]*2;
			if(time>=t)
			{
				int val=(total[i]-t/2);
				time=t;
				num[i]=val;
				break;
			}
		}
		sort(num+i,num+n);
		int start=i;
		for(i=n-1;i>=start;i--)
		{
			if(l>0)
			{
				time+=num[i];
				l--;
			}
			else
			{	
				time+=num[i]*2;
			}
		}
		printf("Case #%d: %lld\n",++tt,time);

	}
	return 0;
}
