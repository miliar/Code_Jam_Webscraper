//Solves "Magicka" from http://code.google.com/codejam/contest/dashboard?c=975485
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
		Uint C; //combine length
	 	Uint D; //destroy length
		Uint N; //invoke length


		
		map<pair<char, char> , char> combinations; //"each pair can only appear in one combination"
		map<char, set<char> > destructions;  //But I don't see anything that says you can't have one element opposed to more than one other element...

		list<char> invoke;

		input >> C;

		for (Uint ii = 0; ii < C; ii++)
		{
			string combo;
			input >> combo;
			assert(combo.length() == 3);
			
			combinations[pair<char, char>(combo.at(0), combo.at(1))] = combo.at(2);
			combinations[pair<char, char>(combo.at(1), combo.at(0))] = combo.at(2);
			#ifdef DEBUG
				cout << combo.at(0) << " + " << combo.at(1) << " = " << combo.at(2) << "\n";
			#endif //DEBUG
		}

		input >> D;
		for (Uint ii=0; ii < D; ii++)
		{
			string destroy;
			input >> destroy;
			assert(destroy.length() == 2);

			destructions[destroy.at(0)].insert(destroy.at(1));
			destructions[destroy.at(1)].insert(destroy.at(0));
			#ifdef DEBUG
				cout << destroy.at(0) << " HATES " << destroy.at(1) << "\n";
			#endif //DEBUG
			
		}

		input >> N;
		

		string elementList;
		for (Uint ii=0; ii < N; ii++)
		{

			char invoke;
			input >> invoke;
			#ifdef DEBUG
				cout << "index #" << ii << ": elementList: " << elementList << ", to invoke: " << invoke << "\n";
			#endif //DEBUG

			if (elementList.length() == 0)
			{
				elementList += invoke;
				continue;
			}

			//Look for a combination...
			map<pair<char, char> , char>::iterator f = combinations.find(pair<char, char>(invoke, elementList.at(elementList.length()-1)));
			#ifdef DEBUG
				cout << "Combinations for " << invoke << " and " << elementList.at(elementList.length()-1) << "...	";
			#endif //DEBUG

			//A combination was found
			if (f != combinations.end())
			{
				#ifdef DEBUG
					cout << (*f).second << "\n";
				#endif //DEBUG
				elementList.at(elementList.length()-1) = (*f).second; //replace last element with the combination
				continue;
			}
			#ifdef DEBUG
				else
				{
					cout << " none!\n";
				}
			#endif //DEBUG

			//Look for a destruction
			#ifdef DEBUG
				cout << "Destructions for " << invoke << "...	";
			#endif //DEBUG

			bool destroyed = false;
			string::iterator i = elementList.begin();
			while (i != elementList.end())
			{
				map<char, set<char> >::iterator e = destructions.find(invoke);
				if (e != destructions.end())
				{
					set<char>::iterator e2 = (*e).second.find(*i);
					if (e2 != (*e).second.end())
					{
						#ifdef DEBUG
							cout << (*e2) << " found! Killing EVERYTHING\n";
						#endif //DEBUG

						elementList.clear();
						destroyed = true;
						break;
					}
				}
				++i;
			}
			if (!destroyed)
				elementList += invoke;
			#ifdef DEBUG
				cout << " none!\n";
			#endif //DEBUG
			
			
			
		}

		string::iterator i = elementList.begin();

		stringstream s;

		s << '[';
		while (i != elementList.end())
		{
			s << (*i);
			if (i+1 != elementList.end())
				s << ", ";
			++i;
		}
		s << ']';

		

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
