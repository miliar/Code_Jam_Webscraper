#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<stack>
#include<cmath>
using namespace std;

int main()
{

	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int test;
	cin>>test;
	for (int curt=1;curt<=test;curt++)
	{
		int n;
		cin>>n;
		int cb=1,co=1;
		vector<int> v1,v2;
		vector<pair<char,int> > v;
		for (int i=0;i<n;i++)
		{
			char c;
			int to;
			cin>>c>>to;
			if (c=='O')
			{
				v1.push_back(to);
			}
			else
			{
				v2.push_back(to);
			}
			v.push_back(make_pair(c,to));
		}
		reverse(v1.begin(),v1.end());
		reverse(v2.begin(),v2.end());
		reverse(v.begin(),v.end());
		int res=0;
		while (!v1.empty()||!v2.empty())
		{
			res++;
			bool ch=1;
			if (!v1.empty())
			{
				if (v1.back()==co)
				{
					if (v.back().first=='O')
					{
						v1.pop_back();
						v.pop_back();
						ch=0;
						
					}
				}
				else
				{
					
					if (v1.back()>co)
						co++;
					else
						co--;
				}
			}
			if (!v2.empty())
			{
				if (v2.back()==cb)
				{
					if (v.back().first=='B'&&ch)
					{
						v2.pop_back();
						v.pop_back();
					}
				}
				else
				{
					if (v2.back()>cb)
						cb++;
					else
						cb--;
				}
			}
		}
		cout<<"Case #"<<curt<<": "<<res<<endl;
	}

	


	 

	return 0;
}