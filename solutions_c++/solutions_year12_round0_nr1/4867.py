#include <iostream>
#include <stdio.h>
#include <map>
#include <string>

using namespace std;

int main()
{
	map<char, char> m;
	m['a'] = 'y', m['b'] = 'h', m['c'] = 'e', m['d'] = 's', m['e'] = 'o';
	m['f'] = 'c', m['g'] = 'v', m['h'] = 'x', m['i'] = 'd', m['j'] = 'u';
	m['k'] = 'i', m['l'] = 'g', m['m'] = 'l', m['n'] = 'b', m['o'] = 'k';
	m['p'] = 'r', m['q'] = 'z', m['r'] = 't', m['s'] = 'n', m['t'] = 'w';
	m['u'] = 'j', m['v'] = 'p', m['w'] = 'f', m['x'] = 'm', m['y'] = 'a';
	m['z'] = 'q';
	string s;
	int t;
	scanf("%d\n", &t);
	int j = 1;
	while(t--)
	{
		getline(cin, s);
		cout << "Case #" << j << ": ";
		int len = s.size();
		for(int i = 0; i < len; i++)
		{
			if(s[i] == ' ')
				cout << s[i];
			else
				cout << m[s[i]];
		}
		cout << endl;
		j++;
	}
}
