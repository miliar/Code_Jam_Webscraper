#include<iostream>
#include<vector>
using namespace std;
main()
{
	int t,c=1;
	cin>>t;
	while(t--)
	{
		int k;
		cin>>k;
		int arr[5001];
		memset(&arr,0,sizeof(arr));
		int ans[101];
		int n;
		cin>>n;
		int i;
		for(i=0;i<n;i++)
		cin>>ans[i];
		int cnt=0,j=1;
		for(i=1;i<=k;)
		{
			if(arr[j]==0)
			{
				cnt++;
			}
			if(i==cnt)
			{
				arr[j]=i;
				i++;
				cnt=0;
			}
			j++;
			if(j==k+1)
			j=1;
		}
		cout<<"Case #"<<c<<": ";
		c++;
		for(i=0;i<n;i++)
		cout<<arr[ans[i]]<<" ";
		cout<<endl;
	}
}

			
		
	
