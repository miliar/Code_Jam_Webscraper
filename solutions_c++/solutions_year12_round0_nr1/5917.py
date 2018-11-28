#include <iostream>
#include <string>
#include <map>

using namespace std;

int main()
{
	map<char,char> M;
	M['a'] = 'y';
	M['b'] = 'h';
	M['c'] = 'e';
	M['d'] = 's';
	M['e'] = 'o';
	M['f'] = 'c';
	M['g'] = 'v';
	M['h'] = 'x';
	M['i'] = 'd';
	M['j'] = 'u';
	M['k'] = 'i';
	M['l'] = 'g';
	M['m'] = 'l';
	M['n'] = 'b';
	M['o'] = 'k';
	M['p'] = 'r';
	M['q'] = 'z';
	M['r'] = 't';
	M['s'] = 'n';
	M['t'] = 'w';
	M['u'] = 'j';
	M['v'] = 'p';
	M['w'] = 'f';
	M['x'] = 'm';
	M['y'] = 'a';
	M['z'] = 'q';	

	string a;

	int T; cin >> T; getline(cin,a);
	for (int z = 1; z <= T; z++){
		getline(cin, a);
		cout << "Case #" << z << ": ";
		for (int i = 0; i < a.size(); i++){
			if (a[i] != ' ')
				cout << M[a[i]];
			else
				cout << " ";
		}
		cout << endl;
	}
	return 0;

}
