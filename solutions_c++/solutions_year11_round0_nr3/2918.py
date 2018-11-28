#include <iostream>
using namespace std;
int main()
{
	int t,n,c[2000],mini,res;
	__int64 sum;
	cin>>t;
	for (int i=1;i<=t;i++)
	{
		cin>>n;
		sum=0;
		res=0;
		for (int j=0;j<n;j++)
		{
			cin>>c[j];
			sum+=c[j];
			if (j==0)
				mini=c[j];
			else if (mini>c[j])
				mini=c[j];
			res = (res^c[j]);
		}
		cout<<"Case #"<<i<<": ";
		if (res == 0)
			cout<<sum-mini<<endl;
		else
			cout<<"NO"<<endl;
	}
	return 0;
}