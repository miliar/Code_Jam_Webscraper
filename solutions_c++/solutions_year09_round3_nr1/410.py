#include<iostream>
#include<map>
#include<vector>
using namespace std;
string x;
vector<int> y;
main()
{	
	int test,cas=1;
cin>>test;
	while(test--)
	{		
		cin>>x;
		map<char,int> tm;
		y.clear();
		tm.clear();
		int i,cnt=0;
		for(i=0;i<x.size();i++)
		{		
			if(i==0)
			{
				tm[x[i]]=1;
				y.push_back(1);
				
			}
			else
			if(tm.find(x[i])!=tm.end())
			{
				y.push_back(tm[x[i]]);
			}
			else
			{
				tm[x[i]]=cnt;
				y.push_back(cnt);
				if(cnt==0)
				cnt=2;
				else
				cnt++;
			}
		}
		if(cnt<2)
		cnt=2;
		long long ans=0;
		long long p=1;		
		for(i=y.size()-1;i>=0;i--)
		{
			ans=ans+(y[i]*p);
			if(ans<0)
			{
				cout<<"trouble";
				return 0;
			}
		
			p=p*cnt;
		}
		cout<<"Case #"<<cas<<": "<<ans<<endl;
		cas++;
	}
	
}
		
		
