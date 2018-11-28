#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
	string s;

	int a[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int t;
	cin>>t;
	getchar();	
	for(int j=0;j<t;j++)
	{	
		getline(cin,s);
		cout<<"Case #"<<j+1<<": ";	
		for(int i=0;i<s.size();i++)
		{
			if(s[i]!=' ')
			printf("%c",a[s[i]-'a']);
			else
			printf(" ");
		}
		cout<<"\n";
	}
	
}
