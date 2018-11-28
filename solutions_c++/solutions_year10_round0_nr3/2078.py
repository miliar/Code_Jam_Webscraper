#include<iostream>
using namespace std;
int arr[1001];
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,g,i,r,k,n,ans;
	scanf("%d",&t);
	for(g=0;g<t;g++)
	{
		ans=0;
		scanf("%d %d %d",&r,&k,&n);
		for(i=0;i<n;i++)scanf("%d",&arr[i]);
		i=0;
		int sum=0,he=0;
		while(r)
		{
			if(arr[i]>k)
			{
				r--;
				continue;
			}
			sum=0;
			while(sum+arr[i]<=k)
			{
				ans+=arr[i];
				sum+=arr[i];
				i=(i+1)%n;
				if(he==i)break;
			}
			he=i;
			r--;
		}
		printf("Case #%d: %d\n",g+1,ans);
	}
	return 0;
}