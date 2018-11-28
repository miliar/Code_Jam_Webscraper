#include <vector>
#include <iostream>
#include <string>
#include <cmath>
#include <map>
#include <climits>
#include <queue>
#include <stack>
#include <sstream>
#include <fstream>

using namespace std;

int main()
{

	ifstream cin("A-small-attempt1.in");
	ofstream cout("google1.out");

	string s1,g1,s2,g2,s3,g3;

	s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	s2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	s3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";

	g1 = "our language is impossible to understand";
	g2 = "there are twenty six factorial possibilities";
	g3 = "so it is okay if you want to just give up";


	map<char,char> mp;

	for(int i=0;i<s1.size();i++)
	{
		mp[s1[i]]=g1[i];
	}

	for(int i=0;i<s2.size();i++)
	{
		mp[s2[i]]=g2[i];
	}

	for(int i=0;i<s3.size();i++)
	{
		mp[s3[i]]=g3[i];
	}

	mp['z'] = 'q';
	mp['q'] = 'z';

	int n;
	cin >> n;
	string s;
	getline(cin,s);

	for(int c=1;c<=n;c++)
	{
		getline(cin,s);

		string t=s;

		for(int i=0;i<t.size();i++)
		{
			t[i] = mp[s[i]];
		}

		cout << "Case #" << c << ": " << t << endl;

	}

	system("pause");
}