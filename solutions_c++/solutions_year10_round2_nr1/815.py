#include<iostream>
#include<string>
#include<map>
using namespace std;
main()
{
	int test,cas=1;
	string a,b;
	map<string,int> mp;
	cin>>test;

	while(test--)
	{
		mp.clear();
		mp["/"]=1;
		int n,m,i,j;
		cin>>n>>m;
		for(i=0;i<n;i++)
		{
			cin>>a;
			a.push_back('/');
			b="";
			for(j=0;j<a.size();j++)
			{
				b.push_back(a[j]);
				if(a[j]=='/')
				{
					mp[b]=1;
					//cout<<b<<endl;
				}
			}
		}
		int ans=0;
		for(i=0;i<m;i++)
		{
			cin>>a;
			a.push_back('/');
			b="";
			for(j=0;j<a.size();j++)
			{
				b.push_back(a[j]);
				if(a[j]=='/' && mp.find(b)==mp.end())
				{
					ans++;
					mp[b]=1;
				}
			}
		}
		cout<<"Case #"<<cas<<": "<<ans<<endl;
		cas++;
	}
}
				
			
		
	
