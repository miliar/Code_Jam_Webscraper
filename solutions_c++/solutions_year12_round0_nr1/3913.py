#include <iostream>
#include <string>
using namespace std;

string trans1="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
string trans2="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

int t,t1;
string s;
string s1="qwertyuiopasdfghjklzxcvbnm";
string s2="zfotwajdkrynscvxuigqmephbl";

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int i;

	cin >> t;
	getline(cin, s);
	for(t1=0;t1<t;t1++)
	{
		getline(cin, s);
		for(i=0;i<s.length();i++)
		{
			if(s[i]!=' ')
			{
				s[i]=s2[ s1.find(s[i]) ];
			}
		}
		cout << "Case #" << t1+1 << ": "<< s << "\n";
	}

	/*
	int i;

	for(i=0;i<trans1.length();i++)
	{
		if(trans1[i]!=' ')
		{
			s2[ s1.find(trans1[i]) ] = trans2[i];
		}
	}

	cout << s2 << "\n";*/

	return 0;
}