#include <iostream>
#include<fstream>
#include<string>
using namespace std;
#define fileIn "A-small-attempt2.in"
#define fileOut "A-small-attempt0.out"

int main()
{
	int nCases, i, j, k, length[30];
	ifstream input;
	ofstream output;
	input.open(fileIn, ios::in);
	output.open(fileOut, ios::in);
	
	input>>nCases;
	input.ignore(1);

	string G[30], S[30];
	for(j = 0; j < 30; j++)
	{
		getline(input, G[j]);
		length[j]  = G[j].length();
		S[j] = G[j];
	}

	for(j = 0; j < 30; j++)
	{
		for(i = 0; i < length[j]; i++)
		{
			switch(G[j][i])
			{
			case 'a':
				S[j][i] = 'y';
				break;
			case 'b':
				S[j][i] = 'h';
				break;
			case 'c':
				S[j][i] = 'e';
				break;
			case 'd':
				S[j][i] = 's';
				break;
			case 'e':
				S[j][i] = 'o';
				break;
			case 'f':
				S[j][i] = 'c';
				break;
			case 'g':
				S[j][i] = 'v';
				break;
			case 'h':
				S[j][i] = 'x';
				break;
			case 'i':
				S[j][i] = 'd';
				break;
			case 'j':
				S[j][i] = 'u';
				break;
			case 'k':
				S[j][i] = 'i';
				break;
			case 'l':
				S[j][i] = 'g';
				break;
			case 'm':
				S[j][i] = 'l';
				break;
			case 'n':
				S[j][i] = 'b';
				break;
			case 'o':
				S[j][i] = 'k';
				break;
			case 'p':
				S[j][i] = 'r';
				break;
			case 'q':
				S[j][i] = 'z';
				break;
			case 'r':
				S[j][i] = 't';
				break;
			case 's':
				S[j][i] = 'n';
				break;
			case 't':
				S[j][i] = 'w';
				break;
			case 'u':
				S[j][i] = 'j';
				break;
			case 'v':
				S[j][i] = 'p';
				break;
			case 'w':
				S[j][i] = 'f';
				break;
			case 'x':
				S[j][i] = 'm';
				break;
			case 'y':
				S[j][i] = 'a';
				break;
			case 'z':
				S[j][i] = 'q';
				break;
			default:
				S[j][i] = G[j][i];
				break;
			}
		}
	}

	for(k = 0; k < 30; k++)
	{
		output<<"Case #"<<k+1<<": "<<S[k]<<endl;
	}
}