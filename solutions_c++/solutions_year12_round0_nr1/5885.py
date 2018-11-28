#include<iostream>
#include<string>
#include<algorithm>
#include<set>
#include<map>
using namespace std;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	map < char, char> m;
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


	string strgoogle, str3ady;
	int t;
	cin >> t;
	cin.ignore();
	for(int i = 0; i < t; i ++)
	{
		getline(cin, strgoogle);
		cout << "Case #" << i+1 << ": ";
		for(int j = 0; j < strgoogle.size(); j++)
			if(strgoogle[j] == ' ')
				cout << ' ';
			else
				cout << m[char(strgoogle[j])];
		cout << endl;
	}

}