#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<set>
#include<fstream>
#include<queue>
#include<fstream>
#include<map>

using namespace std;

int main()
{
	ifstream cin("C-small-attempt0.in");
	ofstream cout("C-small.out");
	//ifstream cin("C-large.in");
	//ofstream cout("C-large.out");


	long long test;
	cin>>test;

	for(int j=0;j<test;j++)
	{
		vector<int> ng;
		int n,l,h;
		cin>>n>>l>>h;
		for(int i=0;i<n;i++)
		{
			int m;
			cin>>m;
			ng.push_back(m);
		}
		
		bool in=false;
		int ans;
		for(int i=l;i<=h;i++)
		{
			in=false;
			for(int q=0;q<ng.size();q++)
			{
				ans=i;
				if(i%ng[q]==0 || ng[q]%i==0)
				{
					continue;
				}
				else
				{
					in=true;
					break;
				}
				
			}
			if(in==false)
				{
					break;
				}

		}

		cout<<"Case #"<<j+1<<": ";
		if(in)
		{
			cout<<"NO\n";
		}
		else
		{
			cout<<ans<<endl;
		}


	}

	//system("pause");
	return 0;
}