#include <iostream>
using namespace std;

int main()
{
	long r,k,n,t;
	long ar[2000];
	long arr[2000];
	long closing[2000];
	//cout<<"t"<<endl;
	cin>>t;
	for (int i = 1;i<=t;i++)
	{
		//cout<<i<<" r,k,n"<<endl;
		cin>>r>>k>>n;
		for (int ii = 0;ii<n;ii++)
		{
			cin>>ar[ii];
			arr[ii]=0;
			closing[ii]=0;
		}
		int cur = 0;
		for (int ii = 0;ii<n;ii++)
		{
			cur = ii;
			int currentTotal = 0;
			int currentGroup = 0;
			while (currentGroup<n && currentTotal+ar[cur%n]<=k)
			{
				currentTotal+=ar[cur%n];
				cur++;
				currentGroup++;
			}
			closing[ii]=cur%n;
			arr[ii]=currentTotal;
			//cout<<ii<<" "<<arr[ii]<<" "<<closing[ii]<<endl;
		}
		int current = 0;
		long total = 0;
		cur = 0;
		while (current<r)
		{
			total+=arr[cur];
			cur=closing[cur];
			current++;
		}

		cout<<"Case #"<<i<<": "<<total<<endl;
	}
	return 0;
}