#include<iostream>
#include<string>
#define MaxN 30

using namespace std;

int n;
string s[MaxN+1];
char c[27];

int main()
{
	for(int i=0;i<26;i++)
	{
		char x;
		cin>>x; c[x-'a']=i+'a';
	}
	cin>>n;
	getline(cin,s[0]);
	for(int i=1;i<=n;i++)
	{
		getline(cin,s[i]);
		for(int j=0;j<s[i].size();j++)
		{
			if (s[i][j]!=' ') s[i][j]=c[s[i][j]-'a'];
		}
		cout<<"Case #"<<i<<": "<<s[i]<<endl;
	}
	return 0;
}
