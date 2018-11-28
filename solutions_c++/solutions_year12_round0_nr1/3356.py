#include <map>
#include <iostream>
using namespace std;

int main(int argc, const char *argv[])
{
	map<char, char> M;
	M['e'] = 'o';
	M['j'] = 'u';
	M['p'] = 'r';
	M['m'] = 'l';
	M['y'] = 'a';
	M['s'] = 'n';
	M['l'] = 'g';
	M['j'] = 'u';
	M['y'] = 'a';
	M['l'] = 'g';
	M['c'] = 'e';
	M['k'] = 'i';
	M['d'] = 's';
	M['k'] = 'i';
	M['x'] = 'm';
	M['v'] = 'p';
	M['e'] = 'o';
	M['d'] = 's';
	M['d'] = 's';
	M['k'] = 'i';
	M['n'] = 'b';
	M['m'] = 'l';
	M['c'] = 'e';
	M['r'] = 't';
	M['e'] = 'o';
	M['j'] = 'u';
	M['s'] = 'n';
	M['i'] = 'd';
	M['c'] = 'e';
	M['p'] = 'r';
	M['d'] = 's';
	M['r'] = 't';
	M['y'] = 'a';
	M['s'] = 'n';
	M['i'] = 'd';
	M['r'] = 't';
	M['b'] = 'h';
	M['c'] = 'e';
	M['p'] = 'r';
	M['c'] = 'e';
	M['y'] = 'a';
	M['p'] = 'r';
	M['c'] = 'e';
	M['r'] = 't';
	M['t'] = 'w';
	M['c'] = 'e';
	M['s'] = 'n';
	M['r'] = 't';
	M['a'] = 'y';
	M['d'] = 's';
	M['k'] = 'i';
	M['h'] = 'x';
	M['w'] = 'f';
	M['y'] = 'a';
	M['f'] = 'c';
	M['r'] = 't';
	M['e'] = 'o';
	M['p'] = 'r';
	M['k'] = 'i';
	M['y'] = 'a';
	M['m'] = 'l';
	M['v'] = 'p';
	M['e'] = 'o';
	M['d'] = 's';
	M['d'] = 's';
	M['k'] = 'i';
	M['n'] = 'b';
	M['k'] = 'i';
	M['m'] = 'l';
	M['k'] = 'i';
	M['r'] = 't';
	M['k'] = 'i';
	M['c'] = 'e';
	M['d'] = 's';
	M['d'] = 's';
	M['e'] = 'o';
	M['k'] = 'i';
	M['r'] = 't';
	M['k'] = 'i';
	M['d'] = 's';
	M['e'] = 'o';
	M['o'] = 'k';
	M['y'] = 'a';
	M['a'] = 'y';
	M['k'] = 'i';
	M['w'] = 'f';
	M['a'] = 'y';
	M['e'] = 'o';
	M['j'] = 'u';
	M['t'] = 'w';
	M['y'] = 'a';
	M['s'] = 'n';
	M['r'] = 't';
	M['r'] = 't';
	M['e'] = 'o';
	M['u'] = 'j';
	M['j'] = 'u';
	M['d'] = 's';
	M['r'] = 't';
	M['l'] = 'g';
	M['k'] = 'i';
	M['g'] = 'v';
	M['c'] = 'e';
	M['j'] = 'u';
	M['v'] = 'p';

	M['q'] = 'z';
	M['z'] = 'q';
	M[' '] = ' ';

	//cout << M.size() << endl;
	//map<char, char>::iterator it = M.begin();
	//while (it != M.end())
	//{
	//	cout << it->first << endl;
	//	++ it;
	//}

	int n;
	cin >> n;
	string ss;
	getline(cin, ss);
	for (int i = 0; i < n; i ++)
	{
		string s;
		getline(cin, s);
		cout << "Case #" << i+1 << ": ";
		for (int j = 0; j < s.length(); j ++)
		{
			cout << M[s[j]];
		}
		cout << endl;
	}

	return 0;
}
