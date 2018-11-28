#include <iostream>
#include <map>
#include <cctype>
using namespace std;

int main()
{
	map< char, char > m;
	m['y'] = 'a';
	m['n'] = 'b';
	m['f'] ='c';
	m['i'] ='d';
	m['c'] ='e';
	m['w'] ='f';
	m['l'] ='g';
	m['b'] ='h';
	m['k'] ='i';
	m['u'] = 'j';
	m['o'] ='k';
	m['m'] = 'l';
	m['x'] ='m';
	m['s'] ='n';
	m['e'] ='o';
	m['v'] ='p';
	m['z'] ='q';
	m['p'] ='r';
	m['d'] ='s';
	m['r'] ='t';
	m['j']='u';
	m['g']='v';
	m['t']='w';
	m['h']='x';
	m['a']='y';
	m['q'] = 'z';

	m[' '] = ' ';

	int x;
	cin >> x;
	while(!isalpha(cin.peek()))
		cin.ignore();
	for(int i = 0; i < x; i++)
	{
		string s;
		getline(cin,s);
		string out;
		for(int j = 0; j < s.size(); j++)
		{
			out += m[s[j]];
		}

		std::cout << "Case #" << i+1 << ": " << out << std::endl;
	}

	return 0;
}