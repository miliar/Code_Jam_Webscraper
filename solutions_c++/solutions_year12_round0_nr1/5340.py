#include <cstdio>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <map>

using namespace std;


int main()
{
	ifstream file("A-small-attempt3.in");
	if (!file.is_open())
		printf("File open fail");
	ofstream output("A-small-attempt3.out");
	if (!output.is_open())
		printf("Output File open fail");
	
	map<char, char> dict;
	dict['a'] = 'y';
	dict['b'] = 'h';
	dict['c'] = 'e';
	dict['d'] = 's';
	dict['e'] = 'o';
	dict['f'] = 'c';
	dict['g'] = 'v';
	dict['h'] = 'x';
	dict['i'] = 'd';
	dict['j'] = 'u';
	dict['k'] = 'i';
	dict['l'] = 'g';
	dict['m'] = 'l';
	dict['n'] = 'b';
	dict['o'] = 'k';
	dict['p'] = 'r';
	dict['q'] = 'z';
	dict['r'] = 't';
	dict['s'] = 'n';
	dict['t'] = 'w';
	dict['u'] = 'j';
	dict['v'] = 'p';
	dict['w'] = 'f';
	dict['x'] = 'm';
	dict['y'] = 'a';
	dict['z'] = 'q';
	dict[' '] = ' ';
	
	char buf[101];
	memset(buf,0,sizeof(buf));
	
	int T;

	file.getline(buf, sizeof(buf));
	T = atoi(buf);
	
	for (int i=0;i<T;i++)
	{
		file.getline(buf, sizeof(buf));
		
		output <<"Case #"<<(i+1)<<": ";
		char *index = buf;
		while(*index != '\0')
		{
			output <<dict[*(index++)];
		}
		
		output <<endl;
		
		memset(buf,0,sizeof(buf));
		
	}
	
	file.close();
	output.close();

	return 0;
}