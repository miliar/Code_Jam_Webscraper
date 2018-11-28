#include<iostream>
#include<string>
#include<map>
#include<vector>
using namespace std;

int main ()
{
	//freopen ("in.in", "r", stdin);
	//freopen ("out.out", "w", stdout);
	map <char, char> m;
	m['y'] = 'a';
	m['n'] = 'b';
	m['f'] = 'c';
	m['i'] = 'd';
	m['c'] = 'e';
	m['w'] = 'f';
	m['l'] = 'g';
	m['b'] = 'h';
	m['k'] = 'i';
	m['u'] = 'j';
	m['o'] = 'k';
	m['m'] = 'l';
	m['x'] = 'm';
	m['s'] = 'n';
	m['e'] = 'o';
	m['v'] = 'p';
	m['z'] = 'q';
	m['p'] = 'r';
	m['d'] = 's';
	m['r'] = 't';
	m['j'] = 'u';
	m['g'] = 'v';
	m['t'] = 'w';
	m['h'] = 'x';
	m['a'] = 'y';
	m['q'] = 'z';

	string g;
	int n;

	cin >> n;
	cin.ignore();
	for (int c=1; c<=n; c++)
	{
		getline (cin, g);

		
		cout << "Case #" << c << ": ";
		for (int i=0;i<g.size(); i++){
			g[i] = tolower(g[i]);
			if (m.find(g[i]) != m.end())
				cout << m[g[i]];
			else
				cout << g[i];

			
		}
		cout << endl;

	}
	return 0;
}