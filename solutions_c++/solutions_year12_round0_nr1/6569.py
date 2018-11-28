#include <iostream>
#include <map>
#include <string>
#include <fstream>
#include <stdlib.h>

using namespace std;

std::map<char, char> charJamMap;

void CreateMap()
{
charJamMap['a'] = 'y';
charJamMap['b'] = 'h';
charJamMap['c'] = 'e';
charJamMap['d'] = 's';
charJamMap['e'] = 'o';
charJamMap['f'] = 'c';
charJamMap['g'] = 'v';
charJamMap['h'] = 'x';
charJamMap['i'] = 'd';
charJamMap['j'] = 'u';
charJamMap['k'] = 'i';
charJamMap['l'] = 'g';
charJamMap['m'] = 'l';
charJamMap['n'] = 'b';
charJamMap['o'] = 'k';
charJamMap['p'] = 'r';
charJamMap['q'] = 'z';
charJamMap['r'] = 't';
charJamMap['s'] = 'n';
charJamMap['t'] = 'w';
charJamMap['u'] = 'j';
charJamMap['v'] = 'p';
charJamMap['w'] = 'f';
charJamMap['x'] = 'm';
charJamMap['y'] = 'a';
charJamMap['z'] = 'q';
charJamMap[' '] = ' ';
}

int main(int argc, char* argv[])
{
	ifstream f("C:\\A-small-attempt5.in");

	if(!f)
	{
		return -1;
	}

	CreateMap();
	char sInput[100] = "";
	f.getline(sInput, 1000);
	int noTestCases = 1;
	while(f.getline(sInput, 1000))
	{
		cout<<"Case #"<<noTestCases++<<": ";
		char *p = sInput;
		while(*p != '\0')
		{
			if(charJamMap.find(*p) != charJamMap.end())
			{
				cout<<charJamMap[*p];
			}
			else
			{
				cout<<*p;
			}
			
			p++;

		}
		cout<<endl;
		strcpy(sInput, "");
	}
	f.close();
	return 0;
}

