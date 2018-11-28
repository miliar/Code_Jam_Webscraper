#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>
using namespace std;
#define forn(i, n) for (int i = 0; i < (int)(n); i++)

map<char, char> a;

void learn(string s, string t)
{
	forn(i, s.length())
		a[s[i]] = t[i];
}
string solve(string s)
{
	forn(i, s.length())
		s[i] = a[s[i]];
	return s;
}

string s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi \
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd \
de kr kd eoya kw aej tysr re ujdr lkgc jv y qeez";
string s2 = "our language is impossible to understand \
there are twenty six factorial possibilities \
so it is okay if you want to just give up a zooq";

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	learn(s1, s2);

	int n;
	string s;
	
	cin >> n;
	getline(cin, s);
	
	forn(i, n)
	{
		getline(cin, s);
		cout << "Case #" << i+1 << ": " << solve(s) << endl;
	}
	
	return 0;
}
