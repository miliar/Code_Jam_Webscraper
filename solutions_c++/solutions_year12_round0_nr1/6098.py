#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	freopen("1.in","r",stdin);
	string s;
	char ar[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int n=0,i,j;
        getline(cin,s);
        for(j=0;j<s.length();++j)
        {
                n=n*10+s[j]-48;
        }
	for(i=1;i<=n;++i)
	{
		string t="";
		cout<<"Case #"<<i<<": ";
		getline(cin,s);
		for(j=0;j<s.length();++j)
		{
			
			if(s[j]!=32){t+=ar[s[j]-97];}
			else t+=" ";
		}
		cout<<t<<endl;
	}
	return 0;
}
