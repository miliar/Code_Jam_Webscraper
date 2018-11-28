#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#include<map>
#include<set>
using namespace std;
int sub[26] = {
			  	'y','h','e','s','o',
			  	'c','v','x','d','u',
			  	'i','g','l','b','k',
			  	'r','z','t','n','w',
			  	'j','p','f','m','a','q'
              };
int main()
{
    int t, t1=1;
	cin>>t;
	string s1;
    getline(cin,s1);
	while(t1<=t)
	{
	    string s;
		getline(cin,s);
		for(int i=0;i<s.size();i++)
		{
		    if(s[i]==' ')continue;
			int t = s[i]-'a';
			s[i] = sub[t];
		}
		cout<<"Case #"<<t1<<": "<<s<<endl;
		t1++;
	}
	return 0;
}
