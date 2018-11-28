#include<iostream>
#include<vector>
#include<string>
using namespace std;

vector<string> v;

int main()
{
	int t,kase=0;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
		v.clear();
		for(int i=0;i<n;i++)
		{
			string tmp;
			cin>>tmp;
			v.push_back(tmp);
		}
		int cnt=0;
		for(int i=0;i<n;i++)
		{
			int end;
			for(int j=i;j<n;j++)
			{
				int idx=0;
				for(int k=0;k<(int)v[j].size();k++)
					if(v[j][k]=='1')
						idx=k;
				if(idx<=i)
				{
					end=j;
					break;
				}
			}
			for(int j=end;j>i;j--)
			{
				swap(v[j],v[j-1]);
				cnt++;
			}
		}
		cout<<"Case #"<<++kase<<": "<<cnt<<endl;
	}
	return 0;
}