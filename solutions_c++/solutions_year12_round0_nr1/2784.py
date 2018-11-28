/*
 * a.cpp
 *
 *  Created on: Apr 14, 2012
 *      Author: Sara Tarek
 */

#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <memory.h>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdio.h>
#include <utility>
#include <vector>

using namespace std;

int main()
{
	map<char, char> m;
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
	freopen( "input.in", "r", stdin );
	freopen( "output.txt", "w", stdout );

	int T;
	int Case = 1;
	string line;
	cin>>T;
	getline(cin, line);
	while (T > 0){

		getline(cin, line);
		for(int i = 0; i < line.length(); i++)
		{
			line[i] = m[line[i]];
		}
		cout<<"Case #"<<Case<<": "<<line<<endl;
		T--;
		Case++;
	}
	return 0;
}	
	













