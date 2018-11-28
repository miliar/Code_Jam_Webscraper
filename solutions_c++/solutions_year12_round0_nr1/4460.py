#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<list>
#include<queue>
#include<cctype>
#include<stack>
#include<map>
#include<set>
using namespace std;




int main()
{
	char array[26]={'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
	map<char,char> m;
	for(int i=0;i<26;i++)
	{
		m[array[i]]='a'+i;
	}
	int n;
	cin>>n;
	string temp;
	getline(cin,temp,'\n');
	for(int i=0;i<n;i++)
	{
		printf("Case #%d: ",i+1);
		string s;
		getline(cin,s,'\n');
		for(int j=0;j<s.size();j++)
		{
			if(s[j]==' ')
				cout<<' ';
			else
				cout<<m[s[j]];
		}
		cout<<endl;
		
	}
	return 0;
}
