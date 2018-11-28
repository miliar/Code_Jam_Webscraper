#include<iostream>
#include<fstream>
#include<string>

using namespace std;


int main()
{

	ifstream input;
	input.open("A-small-attempt0.in");

	ofstream output;
	output.open("output.txt");

	int numCases;

	string inputLine;

	input >> numCases;
	//getline(input, inputLine, '\n');
	//output << inputLine << endl;

	getline(input, inputLine, '\n');
	for(int i = 0; i < numCases; i++)
	{
		getline(input, inputLine, '\n');
		//output << inputLine << endl;
		//cout << inputLine << endl;
		output << "Case #" << i+1 << ": ";
		for(int j = 0; j < inputLine.size(); j++)
		{
			switch(inputLine[j])
			{
			case('a'):
				output << 'y';
				break;
			case('b'):
				output << 'h';
				break;
			case('c'):
				output << 'e';
				break;
			case('d'):
				output << 's';
				break;
			case('e'):
				output << 'o';
				break;
			case('f'):
				output << 'c';
				break;
			case('g'):
				output << 'v';
				break;
			case('h'):
				output << 'x';
				break;
			case('i'):
				output << 'd';
				break;
			case('j'):
				output << 'u';
				break;
			case('k'):
				output << 'i';
				break;
			case('l'):
				output << 'g';
				break;
			case('m'):
				output << 'l';
				break;
			case('n'):
				output << 'b';
				break;
			case('o'):
				output << 'k';
				break;
			case('p'):
				output << 'r';
				break;
			case('q'):
				output << 'z';
				break;
			case('r'):
				output << 't';
				break;
			case('s'):
				output << 'n';
				break;
			case('t'):
				output << 'w';
				break;
			case('u'):
				output << 'j';
				break;
			case('v'):
				output << 'p';
				break;
			case('w'):
				output << 'f';
				break;
			case('x'):
				output << 'm';
				break;
			case('y'):
				output << 'a';
				break;
			case('z'):
				output << 'q';
				break;
			case(' '):
				output << ' ';
				break;
			}
		
		}
		output << endl;
		
	}

	return 0;
}