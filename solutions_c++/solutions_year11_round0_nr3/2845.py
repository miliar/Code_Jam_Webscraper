//Solves "Candy Splitting" from http://code.google.com/codejam/contest/dashboard?c=975485
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
#include <list>
#include <set>

//definitions and constants
//#define DEBUG //Debug (prints debug messages to stdout)
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



	for (Uint caseNumber = 0; caseNumber < nCases; caseNumber++)
	{
		Uint N;
		input >> N; 

		//fill the bag with candy
		list<Uint> candy;
		for (Uint ii=0; ii < N; ii++)
		{
			Uint latest;
			input >> latest;
			candy.push_back(latest);
		}
		
		//Need to step divide candy into equal piles... one obtained by XORing and one by adding...
		//Conditions: 1. value is the same
		//2. value is the maximum possible
	
		//Solution:
		//Take smallest possible element from candy, put in Patrick's pile (except we don't actually need to store his pile anywhere)
		//If value of Patrick's pile == value of remaining candy, then we are done; Sean takes the remaining candy
		//Otherwise, repeat

		//Sort the candy
		candy.sort();

		
	
		

	
		Uint sean = 0;
		Uint patrick = 0;
		Uint seanCountedByPatrick = 0; //Sean's pile must be counted BY PATRICK

		//calculate total value of candy; sean starts with this value
		list<Uint>::iterator i = candy.begin();
		while (i != candy.end())
		{
			sean += (*i);
			++i;
		}	

		//step through candy and try giving to Patrick

		do
		{
			Uint piece = candy.front();
			#ifdef DEBUG
				cout << "Piece value: " << piece << "\n";
				cout << "Sean: " << sean << " Patrick: " << patrick << "\n";
			#endif //DEBUG

			patrick = piece ^ patrick; //That first year boolean algebra finally pays off...
			sean -= piece; //Presumably Sean can also do subtraction?

			seanCountedByPatrick = 0;

			candy.pop_front();

			i = candy.begin();
			while (i != candy.end())
			{
				#ifdef DEBUG
					cout << "Patrick adds " << (*i) << " to what he thinks Sean has, " << seanCountedByPatrick << "\n";
				#endif //DEBUG
				seanCountedByPatrick = seanCountedByPatrick ^ (*i);
				++i;
			}
		
			#ifdef DEBUG
				cout << "Sean: " << sean << " Patrick: " << patrick << "\n";
				cout << "Patrick THINKS that Sean has: " << seanCountedByPatrick << "\n";
			#endif //DEBUG

		

			
		}
		while ((patrick != seanCountedByPatrick)&&(candy.size() > 0));

		bool solution = (patrick == seanCountedByPatrick);		
		
		stringstream s;
		if (solution)
			s << sean;
		else
			s << "NO";
		

		if (output.good())
		{
			output << "Case #" << caseNumber+1 << ": "  << s.str()  << "\n";
		}
	
		#ifdef SHOWMEWHERETHEPROGRAMISUPTOTO
			cout << "Case #" << caseNumber+1 << ": "  << s.str() << "\n";
		#endif //SHOWMEWHERETHEPROGRAMISUPTOTO
		
		
		


	}

	input.close();
	output.close();
	
}
