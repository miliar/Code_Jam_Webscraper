#include<iostream>
#include<string>
#include<vector>

using namespace std;

int main()
{
	int T=0;
	cin>>T;

	for (int t=0;t<T;t++)
	{
		int n, l, h;
		cin>>n>>l>>h;
		
		int arr[n];
		for (int i=0;i<n;i++) cin>>arr[i];
		
		if (l==1) 
		{
			cout<<"Case #"<<t+1<<": "<<1<<endl;
			continue;	
		}
		
		bool found=false;
		for (int i=l;i<=h;i++)
		{
			int j=0;
			for (j=0;j<n;j++)
			{
				if (i%arr[j]!=0 && arr[j]%i!=0) 
				{
					break;
				}
			}
			
			if (j==n) 
			{
				cout<<"Case #"<<t+1<<": "<<i<<endl;
				found = true;
				break;
			}
		}
		
		if (!found) cout<<"Case #"<<t+1<<": NO"<<endl;
	}//t for ends
}

