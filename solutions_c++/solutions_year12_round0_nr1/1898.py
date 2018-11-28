#include <iostream>
#include <map>
#include <string>

using namespace std;

string s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
string s2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
string s3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
string ss1 = "our language is impossible to understand";
string ss2 = "there are twenty six factorial possibilities";
string ss3 = "so it is okay if you want to just give up";

map<char, char> dic;

int main()
{
	freopen("A-small-attempt4.in", "r", stdin);
	freopen("A-small-attempt4.out", "w", stdout);

	dic.clear();

	string s;
	int i, j, k, T, cases = 1;

	for( i = 0; i < s1.size(); ++i )
		dic[ s1[i] ] = ss1[i];
	for( i = 0; i < s2.size(); ++i )
		dic[ s2[i] ] = ss2[i];
	for( i = 0; i < s3.size(); ++i )
		dic[ s3[i] ] = ss3[i];
	dic['z'] = 'q';
	dic['q'] = 'z';

	cin >> T;
	getline(cin, s);
	while( T-- )
	{
		getline(cin, s);
		cout << "Case #" << cases++ << ": ";
		for( i = 0; i < s.size(); ++i )
			cout << dic[s[i]];
		cout << endl;
	}

	return 0;
}