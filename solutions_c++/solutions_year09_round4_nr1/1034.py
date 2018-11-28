#include<iostream>
#include<string>
using namespace std;
main()
{
	int cas=1,test,n,i,arr[41],j;
	scanf("%d",&test);
	while(test--)
	{
		//scanf("%d",&n);
		cin>>n;
		string inp;
		for(i=0;i<n;i++)
		{		
			cin>>inp;
			arr[i]=-1;
			for(j=0;j<inp.size();j++)
			{		
				if(inp[j]=='1')
				arr[i]=j;
			}
		}
		int ans=0;
		for(i=0;i<n;i++)
		{
			for(j=i;j<n;j++)
			{
				if(arr[j]<=i)
				break;
			}
			ans+=(j-i);
			for(;j!=i;j--)
			swap(arr[j],arr[j-1]);
		}
		cout<<"Case #"<<cas<<": "<<ans<<endl;
		cas++;
	}
}
