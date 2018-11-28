#pragma comment(linker, "/STACK:16777216")
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <utility>

#define forn( i,n ) for ( int i=0; i<(int)(n); i++ )

using namespace std;

int n;
map<char,char> dict;
string str;
char x[101];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	dict['y'] = 'a', dict['e'] = 'o',dict['q'] = 'z',dict['j'] = 'u',dict['p'] = 'r',
		dict['m']='l',dict['s'] = 'n',dict['l'] = 'g',dict['c'] = 'e',dict['k'] = 'i',
		dict['d'] = 's',dict['x'] = 'm',dict['v'] = 'p',dict['n'] = 'b',dict['r'] = 't',
		dict['i'] = 'd',dict['b'] = 'h',dict['t'] = 'w',dict['a'] = 'y',dict['h'] = 'x',
		dict['w'] = 'f',dict['f'] = 'c',dict['o'] = 'k',dict['u'] = 'j',dict['g'] = 'v',
		dict['z'] = 'q';
	cin >> n;
	forn(i,n)
	{
		cin.getline(x,101);
		if (x[0] == 0)
			cin.getline(x,101);
		str = x;
		forn(i,str.length())
		{
			if (str[i] == ' ')
				continue;
			else str[i] = dict[str[i]];
		}
		cout << "Case #" << i+1 << ": " << str << endl;
	}
	return 0;
}