#include <iostream>
#include <string>

using namespace std;

char map[26];

void init()
{
	string s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
	string s2 = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
	int len = s1.length();
	for (int i = 0; i < len; ++i)
		if (s1[i] >= 'a' && s1[i] <= 'z')
		map[s1[i] - 'a'] = s2[i];
	map['q'-'a'] = 'z';
	map['z'-'a'] = 'q';
}

int main()
{
	init();

	int T;
	cin >> T;
	string temp;
	getline(cin, temp);

	for (int testcase = 1; testcase <= T; ++testcase) {
		string s;
		getline(cin, s);
		int len = s.length();
		for (int i = 0; i < len; ++i)
			if (s[i] >= 'a' && s[i] <= 'z')
				s[i] = map[s[i]-'a'];
		cout << "Case #" << testcase << ": " << s << endl;
	}
}
