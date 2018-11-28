#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;

char result[31][101];

char input[101];

char Convert(char x)
{
	char y;

	switch (x)
	{
	case 'a':
		y = 'y';
		break;
	case 'b':
		y = 'h';
		break;
	case 'c':
		y = 'e';
		break;
	case 'd':
		y = 's';
		break;
	case 'e':
		y = 'o';
		break;
	case 'f':
		y = 'c';
		break;
	case 'g':
		y = 'v';
		break;
	case 'h':
		y = 'x';
		break;
	case 'i':
		y = 'd';
		break;
	case 'j':
		y = 'u';
		break;
	case 'k':
		y = 'i';
		break;
	case 'l':
		y = 'g';
		break;
	case 'm':
		y = 'l';
		break;
	case 'n':
		y = 'b';
		break;
	case 'o':
		y = 'k';
		break;
	case 'p':
		y = 'r';
		break;
	case 'q':
		y = 'z';
		break;
	case 'r':
		y = 't';
		break;
	case 's':
		y = 'n';
		break;
	case 't':
		y = 'w';
		break;
	case 'u':
		y = 'j';
		break;
	case 'v':
		y = 'p';
		break;
	case 'w':
		y = 'f';
		break;
	case 'x':
		y = 'm';
		break;
	case 'y':
		y = 'a';
		break;
	case 'z':
		y = 'q';
		break;
	default:
		y = ' ';
		break;
	}

	return y;
}

void Compute(int i, int len)
{
	for(int x = 0; x<len; x++)
	{
		result[i][x] = Convert(input[x]);
	}
}

int main()
{
	int inputLen;

	int t;

	ifstream fileIn;
	ofstream fileOut;

	fileIn.open("input.in", ios::in|ios::_Nocreate);

	fileOut.open("ouput.out", ios::out);

	fileIn.getline(input, 101, '\n');		

	t = atoi(input);

	for(int i = 0; i<t; i++)
	{
		fileIn.getline(input, 101, '\n');

		inputLen = strlen(input);

		Compute(i, inputLen);


	}

	for(int i = 0; i<t; i++)
	{
		fileOut<<"Case #"<<i+1<<": "<<result[i]<<endl;
	}

	fileIn.close();
	fileOut.close();

	return 0;
}