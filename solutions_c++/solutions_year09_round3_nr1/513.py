#include<cstdio>
#include<string>
#include<algorithm>
#include<iostream>
#include<vector>
#include<map>
using namespace std;

int main()
{
	freopen("a.in","r",stdin) ;
	freopen("a.out","w",stdout) ;
	int cases;
	cin>>cases;
	for(int cas=1;cas<=cases;cas++)
	{
		string s;
		cin>>s;
		map<char,int> P;
		if(s.size()==1) {
			cout<<"Case #"<<cas<<": "<<"1"<<endl;
			continue;
		}
		P[s[0]]=1;
		int cur=0;
		for(int i=1;i<s.size();i++)
		{
			if(P.find(s[i])==P.end())
			{
				P[s[i]]=cur;
				if(cur==0)cur=2;
				else cur++;
			}
		}
		if(P.size()==1) cur=2;
		long long ans=0,base=cur,baseexp=1;
		for(int i=s.size()-1;i>=0;i--)
		{
			ans+=baseexp*P[s[i]];
			baseexp*=base;
		}
		cout<<"Case #"<<cas<<": "<<ans<<endl;
	}
	return 0;
}