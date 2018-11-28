#include<iostream>
#include<map>
#include<string>
using namespace std;

map<char, char> m;

void solve(int x)
{
	string s, w;
	getline(cin, s);
	for(int i = 0; i < (int)s.size(); i++)
	{
		w+=m[s[i]];
	}
	cout << "Case #" << x << ": " << w << endl;
}

void prep()
{
	m[' '] = ' ';
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
}

int main()
{
	prep();
	int n; string z;
	ios_base::sync_with_stdio(0);
	cin >> n;
	getline(cin, z);
	for(int i = 1; i <= n; i++)solve(i);
}
