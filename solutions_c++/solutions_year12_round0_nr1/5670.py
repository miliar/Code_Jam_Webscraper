#include <iostream>
#include <fstream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <ctime>
#include <cctype>

using namespace std;
int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	map <char, char> m;
	m['a'] = 'y';
	m['b'] = 'n';
	m['c'] = 'f';
	m['d'] = 'i';
	m['e'] = 'c';
	m['f'] = 'w';
	m['g'] = 'l';
	m['h'] = 'b';
	m['i'] = 'k';
	m['j'] = 'u';
	m['k'] = 'o';
	m['l'] = 'm';
	m['m'] = 'x';
	m['n'] = 's';
	m['o'] = 'e';
	m['p'] = 'v';
	m['q'] = 'z';
	m['r'] = 'p';
	m['s'] = 'd';
	m['t'] = 'r';
	m['u'] = 'j';
	m['v'] = 'g';
	m['w'] = 't';
	m['x'] = 'h';
	m['y'] = 'a';
	m['z'] = 'q';

	int t;
	scanf("%d\n", &t);
	for (int i = 0; i < t; i++)
	{
		string s;
		char c[10000];
		gets(c);
		s = string(c);
		cout << "Case #" << i + 1 << ": ";
		for (int j = 0; j < s.size(); j++){
			if (s[j] == ' ') cout << s[j]; else {
				for (map<char, char>::iterator it = m.begin(); it != m.end(); it++){
					if (it->second == s[j]){
						cout << it->first;
						break;
					}
				}
			}
		}
		puts("");
	}
			
	return 0;
}