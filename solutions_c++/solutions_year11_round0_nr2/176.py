#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int caseN;
	cin>>caseN;
	for (int caseI=1;caseI<=caseN;caseI++)
	{
		int n;
		map<pair<char,char>,char> combine;
		map<char,set<char> > oppose;
		cin>>n;
		while (n--)
		{
			char a,b,c;
			cin>>a>>b>>c;
			combine[make_pair(a,b)]=c;
			combine[make_pair(b,a)]=c;
		}
		cin>>n;
		while (n--)
		{
			char a,b;
			cin>>a>>b;
			if (!oppose.count(a))
				oppose[a]=set<char>();
			oppose[a].insert(b);
			if (!oppose.count(b))
				oppose[b]=set<char>();
			oppose[b].insert(a);
		}
		string ans;
		cin>>n;
		while (n--)
		{
			char a;
			cin>>a;
			if (ans.size())
			{
				char b=ans[ans.size()-1];
				if (combine.count(make_pair(b,a)))
				{
					ans.erase(--ans.end());
					ans+=combine[make_pair(b,a)];
					continue;
				}
			}
			if (oppose.count(a))
			{
				bool flag=false;
				for (int i=0;i<ans.size();i++)
					if (oppose[a].count(ans[i]))
					{
						flag=true;
						break;
					}
				if (flag)
				{
					ans="";
					continue;
				}
			}
			ans+=a;
		}
		cout<<"Case #"<<caseI<<": [";
		for (int i=0;i<ans.size();i++)
		{
			cout<<ans[i];
			if (i+1<ans.size())
				cout<<", ";
		}
		cout<<"]"<<endl;
	}
	return 0;
}
