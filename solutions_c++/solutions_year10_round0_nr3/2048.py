#include<iostream>
#include<vector>
using namespace std;
main()
{
	int t,r,k,n,g;
	vector<int> grp,grp_n;
	vector<long long>count;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>r>>k>>n;
		grp.clear();
		grp_n.clear();
		count.clear();
		for(int j=0;j<n;j++)
		{
			cin>>g;
			grp.push_back(g);
		}
		for(int j=0;j<n;j++)
		{
			long long sum=grp[j];
			int _j=j+1;
			while(_j%n!=j && sum+grp[_j%n]<=k)
			{
				sum+=grp[_j%n];
				_j++;
			}
			grp_n.push_back(_j%n);
			count.push_back(sum);
		}
		int current=0;
		long long sum=0;
		for(int j=0;j<r;j++)
		{
			sum+=count[current];
			current=grp_n[current];
		}
		cout<<"Case #"<<(i+1)<<": "<<sum<<endl;
	}
}
