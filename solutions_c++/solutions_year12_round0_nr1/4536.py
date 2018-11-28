#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <deque>
#include <map>
#include <math.h>
#include <cstdio>
#include <iomanip>

using namespace std;

int main ()
{

	freopen ("A-small-attempt0.in", "r", stdin);
	freopen ("output.txt", "w", stdout);

	map<char, char> lib;		//<stupid, normal>

	lib['a'] = 'y';
	lib['b'] = 'h';
	lib['c'] = 'e';
	lib['d'] = 's';
	lib['e'] = 'o';
	lib['f'] = 'c';
	lib['g'] = 'v';
	lib['h'] = 'x';
	lib['i'] = 'd';
	lib['j'] = 'u';
	lib['k'] = 'i';
	lib['l'] = 'g';
	lib['m'] = 'l';
	lib['n'] = 'b';
	lib['o'] = 'k';
	lib['p'] = 'r';
	lib['q'] = 'z';
	lib['r'] = 't';
	lib['s'] = 'n';
	lib['t'] = 'w';
	lib['u'] = 'j';
	lib['v'] = 'p';
	lib['w'] = 'f';
	lib['x'] = 'm';
	lib['y'] = 'a';
	lib['z'] = 'q';

	int n;
	cin>>n;
	string str;
	getline (cin,str);
	

	for (int i=1; i<=n; i++)
	{
		getline (cin,str);
		for (int i = 0; i<str.length(); i++)
		{
			if (str[i]!=' ' && str[i]!='\n')
			{
				str[i] = lib[str[i]];
			}
		}
		cout<<"Case #"<<i<<": "<<str<<endl;
	}

    return 0;
}