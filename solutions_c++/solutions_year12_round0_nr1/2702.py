#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>

using namespace std;

int main(){	
	
	int T;
	cin >> T;
	
	string str1g = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string str1e = "our language is impossible to understand";

	string str2g = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	string str2e = "there are twenty six factorial possibilities";
	
	string str3g = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string str3e = "so it is okay if you want to just give up";
	
	map <char,char> mapping;
	map <char,char>::iterator it;
	
	for (int i = 0; i < str1g.length(); i++)
	{
		mapping.insert( make_pair( str1g[i], str1e[i] ) );
	}

	for (int i = 0; i < str2g.length(); i++)
	{
		mapping.insert( make_pair( str2g[i], str2e[i] ) );
	}
	
	for (int i = 0; i < str3g.length(); i++)
	{
		mapping.insert( make_pair( str3g[i], str3e[i] ) );
	}
	
	mapping.insert( make_pair( 'q', 'z' ) );
	mapping.insert( make_pair( 'z', 'q' ) );
	
	string str;
	getline( cin, str );
	
	for (int o = 1; o <= T; o++)
	{
		getline( cin, str );
		string newStr = "";
		
		for (int i = 0; i < str.length(); i++)
		{
			newStr.push_back( mapping[str[i]] );
		}
		
		cout << "Case #" << o << ": " << newStr << endl;
	}
	
	return 0;
}

