#include <cstdio>
#include <cstdlib>
#include <string>
#include <iostream>
#include <map>

using namespace std;

#define maxn 110

string x[maxn];

map<char,char> mp;

int main(){

	string s;

	mp.clear();
	/*
	for (int i = 0; i<26; i++)
	{
		mp['a'+i] = ('a'+i);
	}
	*/
	for (int i = 1; i<=6; i++)
	{
		getline(cin,x[i]);

		if(i>3)
		for (int j = 0;j<x[i].length() ;j++ )
		{
			mp[x[i-3][j]] = x[i][j];
		}
	}
	mp[' '] = ' ';
	mp['q'] = 'z';
	mp['z'] = 'q';

	int n;
	//scanf("%d", &n);
	cin>>n;
	getline(cin, s);

	for (int ttt = 0; ttt<n;ttt++ )
	{
		printf("Case #%d: ", ttt+1);
		getline(cin, s);
		//cout<<s<<endl;
		for (int i = 0; i<s.length(); i++)
		{
				printf("%c", mp[s[i]]);
		}
		printf("\n");
	}



	return 0;
}

