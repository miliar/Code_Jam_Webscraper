#include <iostream>
using namespace std;

string orig = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
string enco = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";

char f(char c)
{
	if(c == 'z')
		return 'q';
	if(c == 'q')
		return 'z';
	for(int i = 0; i < enco.size(); i ++)
		if(c == enco[i])
			return orig[i];
	return c;
}

int t;
string s;

int main()
{
	cin >> t;
	cin.ignore();
	for(int cas = 1; cas <= t; cas ++)
	{
		getline(cin, s);
		cout << "Case #" << cas << ": ";
		for(int i = 0; i < s.size(); i ++)
			cout << f(s[i]);
		cout << endl;
	}
	return 0;
}