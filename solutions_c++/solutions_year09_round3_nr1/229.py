#include <cstdio>
#include <iostream>
#include <string>
#include <map>
#include <set>
using namespace std;

int T,cas=1;
map <char,int> mp;
set <int> app;
string s;

int main()
{
	freopen("d://A-large.in","r",stdin);
	freopen("d://1.txt","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		cin>>s;
		mp.clear();
		app.clear();
		mp.insert(make_pair(s[0],1));
		app.insert(1);
		long long base=2;
		int cur=0;
		for(int i=1;i<s.size();i++)
		{
			if(mp.find(s[i])==mp.end())
			{
				if(cur==0)
				{
					mp.insert(make_pair(s[i],0));
					app.insert(0);
					cur=2;
				}
				else
				{
					mp.insert(make_pair(s[i],cur));
					cur++,base++;
				}
			}
		}
		long long res=0;
		for(int i=0;i<s.size();i++)
			res=res*base+mp[s[i]];
		printf("Case #%d: ",cas++);
		cout<<res<<endl;
	}
	return 0;
}