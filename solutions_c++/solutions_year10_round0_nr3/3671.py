#include <iostream>
using namespace std;

int main()
{
	long r,k,n,t;
	long ar[2000];
	//cout<<"t"<<endl;
	cin>>t;
	for (int i = 1;i<=t;i++)
	{
		//cout<<i<<" r,k,n"<<endl;
		cin>>r>>k>>n;
		for (int ii = 0;ii<n;ii++)
		{
			cin>>ar[ii];
		}
		long total = 0;
		int cur = 0;
		int now = 0;
		int currentTotal = 0;
		int totalGroup=0;
		while (cur<r)
		{
			while (currentTotal+ar[now%n]<=k && totalGroup<n)
			{
				currentTotal += ar[now%n];
				now++;
				totalGroup++;
			}
			total+=currentTotal;
			totalGroup=0;
			currentTotal=0;
			cur++;
		}
		cout<<"Case #"<<i<<": "<<total<<endl;
	}
	return 0;
}