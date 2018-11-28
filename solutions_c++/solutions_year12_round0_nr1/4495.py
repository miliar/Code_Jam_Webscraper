#include <iostream>
#include <string>
#include <map>
using namespace std;
int main()
{
	string s1="qaozejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
	string s2="zyeqour language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
	map<char, char> dict;
	for(int i=0;i<s1.length();i++)dict[s1[i]]=s2[i];
	int T;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>T;
	string s;
	getline(cin,s);
	for(int j=1;j<=T;j++)
	{
		getline(cin,s);
		for(int i=0;i<s.length();i++)s[i]=dict[s[i]];
		cout<<"Case #"<<j<<": "<<s<<endl;
	}
}