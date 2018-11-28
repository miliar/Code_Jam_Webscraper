#include <iostream>
#include <sstream>
#include <fstream>
#include <string>

using namespace std;

char decode(char in);

int main()
{
	ifstream infile;
	ofstream outfile ("out.in");

	infile.open("A-small-attempt0.in");

	int T;
	//string instr;

	infile >> T;
	char x;
	infile.get(x); //clear buffer
	for(int i=0;i<T;i++)
	{
		string instr;
		getline(infile, instr);
		outfile << "Case #" << (i+1) << ": ";
		for(int j=0;j<instr.length();j++)
		{
			outfile << decode(instr[j]);
		}
		outfile << endl;
	}
	/*
	char x;
	infile.get(x);	//clear newline buffer
	while(infile.get(x))
		outfile << decode(x);
		*/

	infile.close();
	outfile.close();
	return 0;
}

char decode(char in)
{
	switch (in)
	{
		case 'a':
			return 'y';
			break;
		case 'b':
			return 'h';
			break;
		case 'c':
			return 'e';
			break;
		case 'd':
			return 's';
			break;
		case 'e':
			return 'o';
			break;
		case 'f':
			return 'c';
			break;
		case 'g':
			return 'v';
			break;
		case 'h':
			return 'x';
			break;
		case 'i':
			return 'd';
			break;
		case 'j':
			return 'u';
			break;
		case 'k':
			return 'i';
			break;
		case 'l':
			return 'g';
			break;
		case 'm':
			return 'l';
			break;
		case 'n':
			return 'b';
			break;
		case 'o':
			return 'k';
			break;
		case 'p':
			return 'r';
			break;
		case 'q':
			return 'z';
			break;
		case 'r':
			return 't';
			break;
		case 's':
			return 'n';
			break;
		case 't':
			return 'w';
			break;
		case 'u':
			return 'j';
			break;
		case 'v':
			return 'p';
			break;
		case 'w':
			return 'f';
			break;
		case 'x':
			return 'm';
			break;
		case 'y':
			return 'a';
			break;
		case 'z':
			return 'q';
			break;
		case ' ':
			return ' ';
			break;
	}
}