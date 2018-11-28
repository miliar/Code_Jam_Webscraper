#include <iostream>
#include <string>

using namespace std;

int main(int argc, char* argv[])
{
	static char mas['z' - 'a' + 1];
	mas['a' - 'a'] = 'y';
	mas['b' - 'a'] = 'h';
	mas['c' - 'a'] = 'e';
	mas['d' - 'a'] = 's';
	mas['e' - 'a'] = 'o';
	mas['f' - 'a'] = 'c';
	mas['g' - 'a'] = 'v';
	mas['h' - 'a'] = 'x';
	mas['i' - 'a'] = 'd';
	mas['j' - 'a'] = 'u';
	mas['k' - 'a'] = 'i';
	mas['l' - 'a'] = 'g';
	mas['m' - 'a'] = 'l';
	mas['n' - 'a'] = 'b';
	mas['o' - 'a'] = 'k';
	mas['p' - 'a'] = 'r';
	mas['q' - 'a'] = 'z';
	mas['r' - 'a'] = 't';
	mas['s' - 'a'] = 'n';
	mas['t' - 'a'] = 'w';
	mas['u' - 'a'] = 'j';
	mas['v' - 'a'] = 'p';
	mas['w' - 'a'] = 'f';
	mas['x' - 'a'] = 'm';
	mas['y' - 'a'] = 'a';
	mas['z' - 'a'] = 'q';

	int n;
	cin >> n;
	cin.get();
	for (int tcase = 1; tcase <= n; ++tcase) {
		string s;
		getline(cin, s);
		cout << "Case #" << tcase << ": "; 
		for (string::const_iterator it = s.begin(); it != s.end(); ++it) {
			cout << mas[*it - 'a'];
		}
		cout << endl;
	}
	return 0;
}