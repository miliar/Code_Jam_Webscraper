#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

int main ()
{
	map<char, char> mymap;
	mymap['a'] = 'y'; mymap['b'] = 'h'; mymap['c'] = 'e'; mymap['d'] = 's'; mymap['e'] = 'o'; mymap['f'] = 'c'; mymap['g'] = 'v';
	mymap['h'] = 'x'; mymap['i'] = 'd'; mymap['j'] = 'u'; mymap['k'] = 'i'; mymap['l'] = 'g'; mymap['m'] = 'l'; mymap['n'] = 'b';
	mymap['o'] = 'k'; mymap['p'] = 'r'; mymap['q'] = 'z'; mymap['r'] = 't'; mymap['s'] = 'n'; mymap['t'] = 'w'; mymap['u'] = 'j';
	mymap['v'] = 'p'; mymap['w'] = 'f'; mymap['x'] = 'm'; mymap['y'] = 'a'; mymap['z'] = 'q';
	
	int t;
	cin >> t;
	string str;
	getline(cin, str);
	vector<string> v(t);
	for (int i = 0; i < t; i++)
	{
		getline(cin, v[i]);
		for (int j = 0; j < (int)v[i].size(); j++)
		{
			if (v[i][j] != ' ')
			{
				char ch = v[i][j];
				v[i][j] = mymap[ch % 'a' + 'a'];
			}
		}
	}
	
	for (int i = 0; i < t; i++)
	{
		cout << "Case #" << i + 1 << ": " << v[i] << endl;
	}
	
}