#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
	int cases;
	cin>>cases;
	for(int numCase=1;numCase<=cases;numCase++)
	{
		int n;
		cin>>n;
		vector<int> a(n);
		for(int i=0;i<n;i++)
			cin>>a[i];
		int ret=0;
		for(int i=0;i<n;i++)
		{
			ret^=a[i];
		}
		if(ret!=0)
		cout<<"Case #"<<numCase<<": "<<"NO"<<endl;
		else 
		{
			sort(a.begin(),a.end());
			int ret=0;
			for(int i=1;i<a.size();i++)
				ret+=a[i];
		cout<<"Case #"<<numCase<<": "<<ret<<endl;
		}
	}
	return 0;
}
