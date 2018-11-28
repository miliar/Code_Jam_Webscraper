#include <iostream>
#include <sstream>
using namespace std;

int match[26]={121,104,101,65651,111,99,118,120,100,117,105,103,108,98,107,114,122,116,110,119,106,112,102,109,97,113};

int main()
{
	/*for(int i = 0; i < 26; i++)
		match[i]=-1;
	int t;
	cin >> t; cin.ignore();
	match['q'-'a']='z';
	match['e'-'a']='o';
	match['y'-'a']='a';
	for(int _=0;_<t; _++)
	{
		string s1, s2;
		getline(cin,s1);
		getline(cin,s2);
		for(int i = 0; i < (int)s1.size(); i++)
			if(s1[i]!=' ')
				match[s1[i]-'a']=s2[i];
	}
	for(int i = 0; i < 26; i++)
		if(match[i]!=0)
			mark[match[i]-'a']=true;
	for(int i = 0; i < 26; i++)
		if(!mark[i])
			cerr << i << endl,match[25]=i+'a';
	cout << match[0];
	for(int i = 1; i < 26; i++)
		cout << ","  << match[i];
	cout << endl;*/
	string tmp;
	int T;
	cin >> T;
	getline(cin,tmp);
	stringstream ss;
	ss<<tmp;
	ss>>T;
	for(int t=1;t<=T;t++)
	{
		string s;
		getline(cin,s);
		cout << "Case #" << t << ": ";
		for(int i = 0; i < (int)s.size(); i++)
			if(s[i]!=' ')
				cout << char(match[s[i]-'a']);
			else
				cout << " ";
		cout << endl;
	}
	return 0;
}
