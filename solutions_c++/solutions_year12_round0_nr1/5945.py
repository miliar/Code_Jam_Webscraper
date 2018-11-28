#include <string.h>
//#include <conio.h>
#include <string>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <queue>
using namespace std;

string translateBack(string expressionBefore)
{
	string expressionAfter = "";

	for (unsigned int i = 0; i < expressionBefore.size(); i++)
	{
		char temp = expressionBefore.at(i);

		switch (temp)
		{
		case 'y':
		{
			expressionAfter += 'a';
			break;
		}
		case 'n':
		{
			expressionAfter += 'b';
			break;
		}
		case 'f':
		{
			expressionAfter += 'c';
			break;
		}
		case 'i':
		{
			expressionAfter += 'd';
			break;
		}
		case 'c':
		{
			expressionAfter += 'e';
			break;
		}
		case 'w':
		{
			expressionAfter += 'f';
			break;
		}
		case 'l':
		{
			expressionAfter += 'g';
			break;
		}
		case 'b':
		{
			expressionAfter += 'h';
			break;
		}
		case 'k':
		{
			expressionAfter += 'i';
			break;
		}
		case 'u':
		{
			expressionAfter += 'j';
			break;
		}
		case 'o':
		{
			expressionAfter += 'k';
			break;
		}
		case 'm':
		{
			expressionAfter += 'l';
			break;
		}
		case 'x':
		{
			expressionAfter += 'm';
			break;
		}
		case 's':
		{
			expressionAfter += 'n';
			break;
		}
		case 'e':
		{
			expressionAfter += 'o';
			break;
		}
		case 'v':
		{
			expressionAfter += 'p';
			break;
		}
		case 'z':
		{
			expressionAfter += 'q';
			break;
		}
		case 'p':
		{
			expressionAfter += 'r';
			break;
		}
		case 'd':
		{
			expressionAfter += 's';
			break;
		}
		case 'r':
		{
			expressionAfter += 't';
			break;
		}
		case 'j':
		{
			expressionAfter += 'u';
			break;
		}
		case 'g':
		{
			expressionAfter += 'v';
			break;
		}
		case 't':
		{
			expressionAfter += 'w';
			break;
		}
		case 'h':
		{
			expressionAfter += 'x';
			break;
		}
		case 'a':
		{
			expressionAfter += 'y';
			break;
		}
		case 'q':
		{
			expressionAfter += 'z';
			break;
		}
		case ' ':
		{
			expressionAfter += ' ';
			break;
		}
		default:
		{
			break;
		}
		}

	}//for

	return expressionAfter;

}

///////////////////////////////////////////////////////////////////////
int main(int argc, char *argv[]) {
	string fileName = argv[1];
	ifstream infile(argv[1]);

	string expression;
	getline(infile, expression);
	int numOfLines = atoi(expression.c_str());

	ofstream outFile("output.txt");
	for(int i = 1; i <= numOfLines; i++)
	{
		getline(infile, expression);

		outFile << "Case #" << i << ": " << translateBack(expression) << endl;
	}

	infile.close();
	outFile.close();
	return 0;
}
