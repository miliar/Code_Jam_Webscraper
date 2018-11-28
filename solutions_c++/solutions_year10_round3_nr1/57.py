#include<iostream>
using namespace std;
main()
{
	int i,j,k,n,test,arr[1001][2],ans;
	cin>>test;
	for(i=1;i<=test;i++)
	{
		ans=0;
		cin>>n;
		for(j=1;j<=n;j++)
		cin>>arr[j][0]>>arr[j][1];
		for(j=1;j<=n;j++)
		{
			for(k=j+1;k<=n;k++)
			{
				if(arr[j][0] > arr[k][0] && arr[j][1] < arr[k][1])
				ans++;
				if(arr[j][0] < arr[k][0] && arr[j][1] > arr[k][1])
				ans++; 
			}
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
}
