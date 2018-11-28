#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int m;
	int n;
	
	cin>>m;
	int no=1;
	int a;
	while(no<=m)
	{
		cin>>n;
		vector<int> x;
	vector<int> y;
		int res=0;
		for(int i=0;i<n;i++)
		{
			cin>>a;
			x.push_back(a);
		}
		for(int i=0;i<n;i++)
		{
			cin>>a;
			y.push_back(a);
		}
		sort(x.begin(),x.end());
		reverse(x.begin(),x.end());
		sort(y.begin(),y.end());
		for(int i=0;i<n;i++)
			res+=x[i]*y[i];
		cout<<"Case #"<<no++<<": "<<res<<endl;
	}
	return 0;
}
	