#include<iostream>
#include <cstdlib>
#include <map>
#include <cmath>
using namespace std;
int main()
{
map<char,int> m;
int tc;
cin>>tc;
int cc=0;
while(tc--)
{
cc++;
string s;
cin>>s;
int i;
char ch=s[0];
int pos=-1;

for(i=0;i<s.length();i++)
{
		if(s[i]!=ch)
		{
			pos=i;
			break;
		}
	

}
	
	m[s[pos]]=0;
	m[s[0]]=1;
	int ct=2;
	for(i=pos;i<s.length();i++)
	{
		if(s[i]!=s[pos] && s[i]!=s[0] && m.find(s[i])==m.end())
		{
			m[s[i]]=ct;
			ct++;
			//cout<<"imh";
		}
	
	
		
	}
	
	//for(i=0;i<s.length();i++)
	//{
	//cout<<m[s[i]];
	//}
	
	int l=m.size();
	long long int res=0,temp;
	
	for(i=0;i<s.length();i++)
	{
		temp=m[s[s.length()-i-1]]*(long long int)pow(l,i);
		//cout<<temp<<" ";
		res+=temp;
	}
	
	cout<<"Case #"<<cc<<": "<<res<<"\n";
	m.clear();
}

}
