#include <iostream>
#include <map>
#include <string>
using namespace std;

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	map<char,char> m;
	m['a'] = 'y';
	m['b'] = 'h';
	m['c'] = 'e';
	m['d'] = 's';
	m['e'] = 'o';
	m['f'] = 'c';
	m['g'] = 'v';
	m['h'] = 'x';
	m['i'] = 'd';
	m['j'] = 'u';
	m['k'] = 'i';
	m['l'] = 'g';
	m['m'] = 'l';
	m['n'] = 'b';
	m['o'] = 'k';
	m['p'] = 'r';
	m['q'] = 'z';
	m['r'] = 't';
	m['s'] = 'n';
	m['t'] = 'w';
	m['u'] = 'j';
	m['v'] = 'p';
	m['w'] = 'f';
	m['x'] = 'm';
	m['y'] = 'a';
	m['z'] = 'q';
	m[' '] = ' ';

	int t;
	cin >> t;
	cin.ignore();
	for (int tc = 1; tc <= t; tc++)
	{
		string str;		
		getline(cin, str);
		string ans(str.length(), ' ');
		for (int i = 0; i < str.length(); i++)
		{
			ans[i] = m[str[i]];
		}
		printf("Case #%d: ", tc);
		cout << ans << endl;
	}
}