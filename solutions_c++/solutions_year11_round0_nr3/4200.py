#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	freopen("c-ans.in","r",stdin);
	freopen("c-ans.out","w",stdout);
	int n,t,i,j,ans,sum;
	
	int a[2000];
	scanf("%d",&t);
	int k=0;
	while(t--)
	{
		
		k++;
		int flag=0;
		scanf("%d",&n);
		scanf("%d",&a[0]);
		ans=sum=a[0];
		for(i=1;i<n;i++)
		{
			scanf("%d",&a[i]);
			ans=ans^a[i];
			sum+=a[i];
			
		}
		if(ans==0)
			flag=1;
		sort(a,a+n);
		if(flag)
		{
			
			printf("Case #%d: %d\n",k,sum-a[0]);
		}
		else 
		{
			printf("Case #%d: NO\n",k);
		}
		
	}
	return 0;
}



