#include <cstdio>
#include <string>
#include <map>
#include <iostream>

using namespace std;

int main()
{
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

	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

	int N;
	scanf("%d", &N);

	for (int i=0; i<N; i++)
	{
		string s;
		getline(cin, s);
		if (s == "")
		{
			i--;
			continue;
		}
		for (int j=0; j<s.size(); j++)
		{
			s[j] = m[s[j]];
		}
		cout<<"Case #"<<i+1<<": ";
		cout<<s<<endl;
	}
	return 0;
}