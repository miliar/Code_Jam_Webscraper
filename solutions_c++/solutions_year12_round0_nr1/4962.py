//============================================================================
// Name        : google_code_jam.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string.h>
#include <iostream>
#include <map>
#include <utility>

using namespace std;

int main() {
	map <char, char> convert;
	map <char, char>::iterator it;
	convert[' ']=' ';
	convert['a']='y';
	convert['b']='h';
	convert['c']='e';
	convert['d']='s';
	convert['e']='o';
	convert['f']='c';
	convert['g']='v';
	convert['h']='x';
	convert['i']='d';
	convert['j']='u';
	convert['k']='i';
	convert['l']='g';
	convert['m']='l';
	convert['n']='b';
	convert['o']='k';
	convert['p']='r';
	convert['q']='z';
	convert['r']='t';
	convert['s']='n';
	convert['t']='w';
	convert['u']='j';
	convert['v']='p';
	convert['w']='f';
	convert['x']='m';
	convert['y']='a';
	convert['z']='q';

	int number = 0;
	cin >> number;

	if (number > 30 || number <1)
		return 0;

	string line;
	getline (cin, line);

	for (int i = 0; i < number; i++)
	{
		getline (cin, line);
		int size = line.size();
		if (size > 100)
		{
			return 0;
		}
		cout << "Case #" << i+1 << ": ";

		for (int j = 0; j < size; j++)
		{
			cout << convert.find(line[j])->second;
		}

		cout << endl;


	}





	return 0;
}
