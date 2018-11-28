#include<iostream>

using namespace std;
int main()
{
	int t,n,x,y;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>n;
		int a[1000],b[1000];
		for(int k=0;k<n;k++)
			cin>>a[k]>>b[k];
		int count=0;
		for(int k=0;k<n;k++)
			for(int j=k+1;j<n;j++)
			{
				x=a[k];
				y=b[k];
				if((a[j]<x && b[j]>y)||(a[j]>x && b[j]<y))
					count++;
	
			}
	cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
	
	
	
	
	
	
	
	
	
	return 0;
}


