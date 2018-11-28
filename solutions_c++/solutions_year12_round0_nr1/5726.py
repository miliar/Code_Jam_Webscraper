#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	string a, b;
	a = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
	b = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";

	int i;
	vector<char> m(26);
	for (i = 0; i < a.size(); ++i)
		if (a[i] != ' ')
			m[a[i] - 'a'] = b[i];

	m['y' - 'a'] = 'a';
	m['e' - 'a'] = 'o';
	m['q' - 'a'] = 'z';

	vector<bool> v(26, false);
	for (i = 0; i < 26; ++i)
		if (i != 25)
			v[m[i] - 'a'] = true;

	for (i = 0; i < 26; ++i)
		if (!v[i])
			break;
	m[25] = i + 'a';

	int t, l;
	scanf("%d\n", &t);
	for (l = 1; l <= t; ++l)
	{
		string s;
		getline(cin, s);
		for (i = 0; i < s.size(); ++i)
			if (s[i] != ' ')
				s[i] = m[s[i] - 'a'];
		cout << "Case #" << l << ": " << s << '\n';
	}
	return 0;
}
