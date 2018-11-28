//Solves "RPI" from http://code.google.com/codejam/contest/dashboard?c=1150485
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
#include <set>

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
		char games[100][100];

		float WP[100];
		float nGames[100];
		float OWP[100];
		float OOWP[100];


		LUint N;
		input >> N;
		for (LUint ii = 0; ii < N; ii++)
		{
			float wins = 0; nGames[ii] = 0;
			for (LUint jj = 0; jj < N; jj++)
			{
				char c;
				input >> c; games[ii][jj] = c;
				switch (games[ii][jj])
				{
					case '.':
						break;
					case '0':
						nGames[ii] += (float)(1);
						break;
					case '1':
						nGames[ii] += (float)(1);
						wins++;
						break;
				}
			}
			WP[ii] = (float)(wins)/(float)(nGames[ii]);
			//cout << "WP for " << ii << " is " << wins << "/" << nGames[ii] << " = " << WP[ii] << "\n";
		}

		for (LUint ii = 0; ii < N; ii++)
		{
			float sum = 0;
			for (LUint jj = 0; jj < N; jj++)
			{
				//cout << ii << " vs " << jj << "\n";
				switch (games[jj][ii])
				{					
					case '.':
						//if (ii != jj)
						//	sum += WP[jj];
						break;
					case '0':
						sum += (float)(WP[jj] * (nGames[jj])) / (float)((float)(nGames[jj] - (float)(1)));
						//cout << "sum += (" << WP[jj] << " * " << nGames[jj] << ") / (" << nGames[jj] << " - 1) = " << sum << "\n";
						break;
					case '1':
						sum += (float)((WP[jj] * (nGames[jj])) - (float)(1)) / (float)((float)(nGames[jj] - (float)(1)));
						//cout << "sum += ((" << WP[jj] << " * " << nGames[jj] << ") - 1) / (" << nGames[jj] << " - 1) = " << sum << "\n";
						break;
							
				}
					

					

			}
			OWP[ii] = sum/nGames[ii];
			//cout << "OWP for " << ii << " is " << sum << "/" << nGames[ii] << " = " << OWP[ii] << "\n";
		}

		for (LUint ii = 0; ii < N; ii++)
		{
			float sum = 0;
			for (LUint jj=0; jj < N; jj++)
			{
				
				switch(games[ii][jj])
				{
			
					case '.':
						break;
					case '0':
					case '1':
						sum += OWP[jj];
						break;
				}
				
			}
			OOWP[ii] = sum / nGames[ii];
			//cout << "OOWP for " << ii << " is " << sum << "/" << nGames[ii] << " = " << OWP[ii] << "\n";
		}

		stringstream s; s.precision(12); s.setf(ios::fixed,ios::floatfield);
		for (LUint ii = 0; ii < N; ii++)
		{
				s << (float)(0.25) * (float)(WP[ii] + (float)(2)*OWP[ii] + OOWP[ii]) << "\n";
		}
		
		if (output.good())
		{
			output << "Case #" << caseNumber+1 << ": \n" << s.str();
		}

	
		#ifdef SHOWMEWHERETHEPROGRAMISUPTOTO
			cout << "Case #" << caseNumber+1 << ": \n"  << s.str();
		#endif //SHOWMEWHERETHEPROGRAMISUPTOTO
		
		
		


	}

	input.close();
	output.close();
	
}
