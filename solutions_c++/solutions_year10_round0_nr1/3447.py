/*
 * SnapperChain.cpp
 * --------------------------------
 * Firstly, the snapper chain is simply a binary counter.
 * In fact, it is a D-flip-flop asynchronous counter, with
 * the snap being the clock signal. In this case, the snapper
 * closest to the wall is the LSB because it alternates every
 * clock, whereas the snapper just before the lamp is the
 * MSB. Second, in order to have the lamp turn on, this means
 * that all the snappers must be ON. In other words, the count
 * must be at 2^N-1 + 2^N-2 + ... = 2^N - 1.
 * It is then a simple matter to code a program that tests
 * that the remainder when K is divided by 2^N (getting rid of
 * all complete loops) is equal to this number.
 *
 * In order to run this program, simple put the exe in a folder
 * with the input file, give it read/write permission, and
 * run it from a Command Prompt.
 */

#include "stdafx.h"
#include <iostream>
#include <fstream> //Used to read/write from the files
#include <math.h>

using namespace std;


int main(void)
{
	//Defining variables
	int cases; //The number of total cases
	int c_count; //Keeps track of which case we're on
	int remainder; //Remainder when 2^N - 1 is divided by K
	int* n;
	int* k; //Declare pointers to dynamic arrays

	ofstream output; //Output stream
	ifstream input; //Input stream

	input.open("A-small.in");
	if(input.is_open()) //Make sure file opened correctly
	{
		input >> cases; //Get the number of cases first

		n = new int[cases];
		k = new int[cases]; //Create dynamic arrays to store the N and K data that follows

		for(c_count = 1; c_count <= cases; c_count++) //Loop through all the cases and input the data
		{
			input >> n[c_count-1];
			input >> k[c_count-1];
		}
	}
	else
	{
		cout << "Could not open input." << endl;
	}
	//All input has now been processed
	input.close();

	output.open("output.txt"); //Open the output stream for an output file
	if(output.is_open()) //Make sure file opened correctly
	{
		for(c_count = 1; c_count <= cases; c_count++) //Loop through all the cases and process it this time
		{
			remainder = k[c_count-1]%int(pow(2.0f,n[c_count-1])); //Have to do some funky typecasting to avoid errors here
			output << "Case #" << c_count << ": ";
			if(remainder == int(pow(2.0f, n[c_count-1])) - 1) //Remainder is a multiple of 2^N - 1
			{
				output << "ON" << endl; //Output "ON"
			}
			else //Remainder is not a multiple of 2^N - 1
			{
				output << "OFF" << endl; //Output "OFF"
			}
		}
	}
	else //File did not open correctly
	{
		cout << "Could not open output file!" << endl;
	}

	return 0;
}

