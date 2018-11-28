#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void main()
{
	ifstream input;
	ofstream outfile;
	input.open("input.txt");
	outfile.open("output.txt");
	int n;
	input >> n;
	string line;
	string output;
	for(int i=0; i<n; i++)
	{
		getline(input, line);
		char *c = new char[line.length() + 1];
		if(line.empty())
		{
			i--;
			continue;
		}
		for(int i=0; i<line.length(); i++)
		{
			switch(line[i])
			{
			case ' ':
				c[i] = ' ';
				break;
			case 'a':
				c[i] = 'y';
				break;
			case 'b':
				c[i] = 'h';
				break;
			case 'c':
				c[i] = 'e';
				break;
			case 'd':
				c[i] = 's';
				break;
			case 'e':
				c[i] = 'o';
				break;
			case 'f':
				c[i] = 'c';
				break;
			case 'g':
				c[i] = 'v';
				break;
			case 'h':
				c[i] = 'x';
				break;
			case 'i':
				c[i] = 'd';
				break;
			case 'j':
				c[i] = 'u';
				break;
			case 'k':
				c[i] = 'i';
				break;
			case 'l':
				c[i] = 'g';
				break;
			case 'm':
				c[i] = 'l';
				break;
			case 'n':
				c[i] = 'b';
				break;
			case 'o':
				c[i] = 'k';
				break;
			case 'p':
				c[i] = 'r';
				break;
			case 'q':
				c[i] = 'z';
				break;
			case 'r':
				c[i] = 't';
				break;
			case 's':
				c[i] = 'n';
				break;
			case 't':
				c[i] = 'w';
				break;
			case 'u':
				c[i] = 'j';
				break;
			case 'v':
				c[i] = 'p';
				break;
			case 'w':
				c[i] = 'f';
				break;
			case 'x':
				c[i] = 'm';
				break;
			case 'y':
				c[i] = 'a';
				break;
			case 'z':
				c[i] = 'q';
				break;
			default:
				break;
			}
		}
		c[line.length()] = 0;
		output = c;
		outfile << "Case #" << i+1 << ": " << output << endl;
	}
	input.close();
}