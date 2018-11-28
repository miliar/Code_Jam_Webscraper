#include<iostream>
#include<cmath>
using namespace std;
int main()
{
	int sun;
	cin>>sun;
	for(int pra=0;pra<sun;pra++)
	{
	int n;
	cin>>n;
	int p=pow(2,n);
	int arr[p];
	int ans[p];
	int level[p][n];
	for(int i=0;i<p;i++)
	{
		cin>>arr[i];
		ans[i]=0;
	}
	int tk;
	for(int i=0;i<n;i++)
	{

		for(int j=0;j<pow(2,n-1-i);j++)
			cin>>tk;
	}


	for(int i=0;i<p;i++)
		for(int j=0;j<n;j++)
			level[i][j]=0;
	int cost=0;

	int l;
	while(1)
	{
		int min=n;
		int temp=0;

		for(int i=0;i<p;i++)
		{
		if(ans[i]+arr[i]<n)
		{
			if(arr[i]<min)
			{
				min=arr[i];
				l=i;
				temp=1;

			}
		}

		}
		if(temp==0)
			break;
		
		int course=n-ans[l]-arr[l];
		while(course--)
		{
		cost+=1;

		int d;

		for(d=n-1;d>=0;d--)
		{
				if(level[l][d]==0)
					break;
		}
		int tp=d;
		d+=1;
		d=pow(2,d);
		int t=l/d;
		t=t*d;
		for(int i=t;i<t+d;i++)
		{
			level[i][tp]=1;
			ans[i]+=1;
		}
		}

	}
	cout<<"Case #"<<pra+1<<": "<<cost<<endl;
	}

}
