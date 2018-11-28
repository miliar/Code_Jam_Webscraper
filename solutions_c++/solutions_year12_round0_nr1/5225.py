#include <algorithm>
#include <vector>
#include <bitset>
#include <map>
#include <math.h>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <queue>
#include <string>
#include <stack>
#include <sstream>
#include <string.h>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
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

	string line;
	ifstream myfile_in ("input.in");
	ofstream myfile_out;
	myfile_out.open ("output.txt");
	int cases = 0;
	bool start = true;
	if (myfile_in.is_open() && myfile_out.is_open())
	{
		while ( myfile_in.good() )
		{
			getline (myfile_in,line);
			if(start)
			{
				start = false;
			}
			else
			{
				myfile_out << "Case #"<< ++cases<<": ";
				for(int i = 0; i < line.length(); i++)
				{
					myfile_out << m.find(line.at(i))->second;
				}
				myfile_out << "\n";
			}
		}
		myfile_in.close();
		myfile_out.close();
	}
	return 0;
}