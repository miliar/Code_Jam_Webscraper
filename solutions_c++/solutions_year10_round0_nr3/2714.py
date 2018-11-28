#include<iostream>
using namespace std;

int main()
{
	
	int i,j,d,t,r,k,m,n,sum,arr[11],temp[11],te;
	cin>>t;
	for(m=1;m<=t;m++)
	{
		cin>>r>>k>>n;
		for(i=0;i<n;i++)
			cin>>arr[i];
		sum=0;
		for(d=0;d<r;d++)
		{
			te=0;
			for(j=0;j<n;j++)
			{
				te+=arr[j];
				if(te>k)
					{
						te-=arr[j];
						break;
					}		
			}
			if(j<n)
			{
				for(i=0;i<j;i++)
				{
					temp[i]=arr[i];
				}
				for(i=j;i<n;i++)
					arr[i-j]=arr[i];
				
				for(i=0;i<j;i++)
				{	
					arr[n-j+i]=temp[i];
				}	
			}	
			sum+=te;
		}
		cout<<"Case #"<<m<<": "<<sum<<endl;
	}
}