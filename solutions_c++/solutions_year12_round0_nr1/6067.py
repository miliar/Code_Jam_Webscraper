#include <iostream>
#include <fstream>
using namespace std;

char convert(char c)
{
	switch (c)
	{
		case 'a':
			return 'y';			
		case 'b':
			return 'h';
		case 'c':
			return 'e';
		case 'd':
			return 's';
		case 'e':
			return 'o';
		case 'f':
			return 'c';
		case 'g':
			return 'v';
		case 'h':
			return 'x';
		case 'i':
			return 'd';
		case 'j':
			return 'u';
		case 'k':
			return 'i';
		case 'l':
			return 'g';
		case 'm':
			return 'l';
		case 'n':
			return 'b';
		case 'o':
			return 'k';
		case 'p':
			return 'r';
		case 'q':
			return 'z';
		case 'r':
			return 't';
		case 's':
			return 'n';
		case 't':
			return 'w';
		case 'u':
			return 'j';
		case 'v':
			return 'p';
		case 'w':
			return 'f';
		case 'x':
			return 'm';
		case 'y':
			return 'a';
		case 'z':
			return 'q';
		default:
			return ' ';
	}
}

int main()
{
	ifstream f;
	ofstream of;
	f.open("A-small-attempt1.in");
	of.open("case.txt");
	int n = 0;
	int i = 0;
	while (!f.eof())
	{
		f >> n;
		f.ignore();
		char input[101];
		while (f.getline(input, 101))
		{
			of << "Case #" << ++i << ": ";
			for (int j = 0; input[j] != '\0'; j++)
				of << convert(input[j]);
			of << endl;
		}
	}
	f.close();
	of.close();
	return 0;
}
