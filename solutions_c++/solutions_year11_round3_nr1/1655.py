//Solves "Square Tiles" from http://code.google.com/codejam/contest/dashboard?c=1128486
//Sam Moore
//2011

#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <cassert>

#include <string>
#include <stack>
#include <sstream>

#include <map>
#include <vector>
#include <algorithm>

//definitions and constants
#define DEBUG //Debug (prints debug messages to stdout)
#define SHOWMEWHERETHEPROGRAMISUPTOTO
typedef unsigned char Uint8; //0 -> 255
typedef short unsigned int SUint; //0 -> 6*10^4
typedef unsigned int Uint; //0 -> 4*10^9
typedef long unsigned int LUint; //0 -> 1*10^19
typedef long int Lint; //-9*10^18 -> +9*10^18

//function forward declarations
static void ReadInput(char * instr, char * outstr); //Function to read input from file identified by instr, put output to file identified by outstr if outstr is not NULL.


//global variables
char * gProgName; //The name of the program

using namespace std;

//the main function
int main(int argc, char ** argv)
{
	
	gProgName = argv[0]; //get program name
	assert(gProgName != NULL);

	

	if (argc < 2)
	{
		cerr << gProgName << ": Not enough arguments - expect: input [out]\n";
		exit(EXIT_FAILURE);
	}
	if (argc > 3)
	{
		cerr << gProgName << ": Too many arguments - expect: input [out]\n";
		exit(EXIT_FAILURE);
	}

	if (argc == 2)
		ReadInput(argv[1],NULL); //If only one argument, don't output
	else 
		ReadInput(argv[1],argv[2]);

	exit(EXIT_SUCCESS);
	return 0;
}

class Digit
{
	public:
		Digit(Uint v) : value(v), init(true) {}
		Digit(const Digit & d) : value(d.value), init(d.init) {}
		Digit() : init(false) {}
		~Digit() {}

		bool init;
		Uint value;
};

void ReadInput(char * instr, char * outstr)
{
	//Load the input file
	fstream input; input.open(instr, fstream::in);
	assert(input.good());
	//Load the output file if supplied
	fstream output;
	if (outstr != NULL)
	{
		output.open(outstr, fstream::out); 
		assert(output.good());
	}

	//Read number of cases
	Uint nCases;
	input >> nCases;
	input.ignore();


	//This seems too easy... I must have done something horribly wrong...
	//OK I got small right, but I still think I must have done something horribly wrong...
	for (Uint caseNumber = 0; caseNumber < nCases; caseNumber++)
	{
		char grid[50][50];
		Uint R; Uint C;
		input >> R; input >> C;

		for (Uint y = 0; y < R; y++)
		{
			for (Uint x = 0; x < C; x++)
			{
				input >> grid[x][y];
			}
		}

		bool possible = true;
		for (Uint y = 0; y < R; y++)
		{
			for (Uint x = 0; x < C; x++)
			{
				switch (grid[x][y])
				{

					case '#':
						if ((x+1 >= C)||(y+1 >= R))
							possible = false;
						if ((grid[x+1][y] == '#')&&(grid[x][y+1] == '#')&&(grid[x+1][y+1] == '#'))
						{
							grid[x][y] = '/'; grid[x+1][y] = '\\';
							grid[x][y+1] = '\\'; grid[x+1][y+1] = '/';
						}
						else
						{
							possible = false;
						}
							break;
					default:
						break;
				}
				if (!possible)
					break;
			}
			if (!possible)
				break;
		}

		
		stringstream s;
		if (!possible)
			s << "Impossible\n";
		else
		{
			for (Uint y = 0; y < R; y++)
			{
				for (Uint x = 0; x < C; x++)
				{
					s << grid[x][y];
				}
				s << "\n";
			}
		}

		if (output.good())
		{
			output << "Case #" << caseNumber+1 << ": \n"  << s.str();
		}
	
		#ifdef SHOWMEWHERETHEPROGRAMISUPTOTO
			cout << "Case #" << caseNumber+1 << ": \n"  << s.str();
		#endif //SHOWMEWHERETHEPROGRAMISUPTOTO
		
		
		


	}

	input.close();
	output.close();
	
}
