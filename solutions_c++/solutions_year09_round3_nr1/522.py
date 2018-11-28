#include<cstdio>
#include<string>
#include<vector>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<map>
using namespace std;
int main()
{
	freopen("a.in","r",stdin) ;
	freopen("aout.txt","w",stdout) ;
	int T=0;
	scanf("%d",&T);
	for(int cs=1;cs<=T;++cs)
	{
		string s="";
		cin>>s;
		long long val=0;
		string as="";
		map<char,long long >Value;
		for(int i=0;i<s.length();++i)
			if(Value.find(s[i])==Value.end())
			{
				Value[s[i]]=val++;
				as+=s[i];
			}
		Value[as[0]]=1;
		if(as.length()>1)
			Value[as[1]]=0;
		long long res=0;
		long long base=1;
		if(val==1)
			val++;
		for(int i=s.length()-1;i>=0;--i)
		{
			res+=(base*Value[s[i]]);
			base*=val;
		}
		cout<<"Case #"<<cs<<": "<<res<<endl;
	}	
	return 0;
}