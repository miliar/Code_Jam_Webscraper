#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
	int t,n,s,p;
	scanf("%d",&t);
	int i=1;
	while(i<=t)
	{
		scanf("%d%d%d",&n,&s,&p);
		int arr[n],cnt=0;
		for(int j=0;j<n;j++)
			scanf("%d",&arr[j]);
		sort(arr,arr+n);
		for(int j=n-1;j>=0;j--)
		{
			int temp;
			temp=arr[j]/3;
			if(arr[j]%3==0)
			{
				if(temp>=p)
					cnt++;
				else
				{
					if(temp!=0)
					{
					if(s!=0)
					{
						if((temp+1)>=p)
							cnt++;
						s--;
					}
					}
				}
			}
			else if(arr[j]%3==1)
			{
				if(temp>=p)
					cnt++;
				else
				{
					if(temp!=0)
					if((temp+1)>=p)
						cnt++;
				}
			}
			else
			{
				if(temp!=0)
				{
				if((temp+1)>=p)
					cnt++;
				else
				{
					if(s!=0)
					{
						if((temp+2)>=p)
							cnt++;
						s--;
					}
				}
				}
			}
			//cout<<"j = "<<j<<" arr = "<<arr[j]<<" cnt = "<<cnt<<"\n";
		}
		//cout<<s<<"\n";
		printf("Case #%d: %d\n",i,cnt);
		i++;
	}
	return 0;
}
