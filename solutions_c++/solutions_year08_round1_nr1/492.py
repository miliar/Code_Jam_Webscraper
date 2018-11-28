#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		vector<int> v1,v2;
		int x,x1;
		cin>>x;
		for(int j=0;j<x;j++)
		{
			cin>>x1;
			v1.push_back(x1);
		}
		for(int j=0;j<x;j++)
		{
			cin>>x1;
			v2.push_back(x1);
		}
		sort(v1.begin(),v1.end());
		sort(v2.begin(),v2.end());
		reverse(v2.begin(),v2.end());
		int re=0;
		for(int j=0;j<v1.size();j++)
			re+=v1[j]*v2[j];
		cout<<"Case #"<<i+1<<": "<<re<<endl;
	}
	return 0;
}