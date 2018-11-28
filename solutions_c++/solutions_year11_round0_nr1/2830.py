//Solves "Bot Trust" from http://code.google.com/codejam/contest/dashboard?c=975485
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

		Uint nButtons;
		input >> nButtons; input.ignore();
		
		map<char, list<int> > desiredPositions; //map bot identifier to a list of the positions that the bot needs to be at
		map<char, int> currentPositions;
		list<char> whoPresses; //List for which bot presses the buttons

		//Construct the lists of positions
		for (Uint ii=0; ii < nButtons; ii++)
		{
			char bot; int position;
			input >> bot; input >> position;
			desiredPositions[bot].push_back(position);
			whoPresses.push_back(bot);
		}

		Uint time = 0;

		currentPositions['O'] = 1; currentPositions['B'] = 1;
		#ifdef DEBUG
			cout << "At Time: " << time << "";
			cout << " Orange: " << currentPositions['O'] << "";
			cout << " Blue: " << currentPositions['B'] << "\n";
		#endif //DEBUG

		

		list<char>::iterator p = whoPresses.begin();
		while (p != whoPresses.end())
		{
			#ifdef DEBUG
				cout << (*p) << " needs to press " << desiredPositions[(*p)].front() << "\n";
			#endif //DEBUG

			int distance = currentPositions[(*p)] - (desiredPositions[(*p)].front()); //The time before the next button can be pressed
			currentPositions[(*p)] = (desiredPositions[(*p)].front()); //move the bot
			desiredPositions[(*p)].pop_front(); //remove the desired position.



			//Deal with the other bot...
			char otherBot;
			switch (*p)
			{
				case 'O': otherBot = 'B'; break;
				case 'B': otherBot = 'O'; break;
			}


			#ifdef DEBUG
				cout << "Meanwhile, " << otherBot << " tries to move towards " << desiredPositions[otherBot].front() << "\n";
			#endif //DEBUG		

			int otherDistance = currentPositions[otherBot] - desiredPositions[otherBot].front(); 
			if (otherDistance != 0)
			{
				if (abs(otherDistance) <= abs(distance)+1)
				{
					currentPositions[otherBot] = desiredPositions[otherBot].front(); //move the other bot to its button, since it takes less time
				}
				else
				{
					if (otherDistance > 0)
						currentPositions[otherBot] -= (abs(distance) + 1);
					else
						currentPositions[otherBot] += (abs(distance) + 1);
				}
			}
			
			
			time += abs(distance) + 1; //increase the time

			#ifdef DEBUG
			cout << "At Time: " << time << ", " << *p << " presses button\n";
			cout << " Orange: " << currentPositions['O'] << "";
			cout << " Blue: " << currentPositions['B'] << "\n";
			#endif //DEBUG

			p++;
		}

		
		if (output.good())
		{
			output << "Case #" << caseNumber+1 << ": "  << time << "\n";
		}
	
		#ifdef SHOWMEWHERETHEPROGRAMISUPTOTO
			cout << "Case #" << caseNumber+1 << ": "  << time << "\n";
		#endif //SHOWMEWHERETHEPROGRAMISUPTOTO
		
		
		


	}

	input.close();
	output.close();
	
}
