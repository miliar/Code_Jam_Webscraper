#include<iostream>
#include<string>
#include<set>
using namespace std;


int main()
{

	freopen("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\gcj\\A-small-attempt0.in","r",stdin);
	freopen("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\gcj\\A-small-attempt0.out","w",stdout);

	int cas;
	cin>>cas;
	for(int cs=1;cs<=cas;cs++)
	{
		int n,m;
		cin>>n>>m;
		set<string> mark;
		for(int ni=0;ni<n;ni++)
		{
			string s;
			cin>>s;
			for(int i=0;i<s.length();i++)
			{
				if(i==s.length()-1||s[i+1]=='/')
				{
					string t=s.substr(0,i+1);
					mark.insert(t);
				}
			}
		}
		int res=0;
		for(int mi=0;mi<m;mi++)
		{
			string s;
			cin>>s;
			for(int i=0;i<s.length();i++)
			{
				if(i==s.length()-1||s[i+1]=='/')
				{
					string t=s.substr(0,i+1);
					if(mark.find(t)==mark.end())
					{
						mark.insert(t);
						res++;
					}
				}
			}
		}
		cout<<"Case #"<<cs<<": "<<res<<"\n";
	}
}