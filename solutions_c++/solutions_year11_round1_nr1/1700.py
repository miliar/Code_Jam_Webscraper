/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- */
/*
 * main.cc
 * Copyright (C) Jirapong Manit 2011 <jirapong.manit@gmail.com>
 * 
 * CodeJamA1 is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * CodeJamA1 is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License along
 * with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string.h>
#include <math.h>

#define N 10
#define T 1000

using namespace std;

/******** Fucntion Declaretion ********/


/********* Global Variables ***********/
char inputfile[] = "inputfile.txt";
const char outfile[] = "outputfiles.txt";


int main(int argc, char *argv[])
{

	/* Variables */
	ifstream inputfd;
	ofstream outputfd;

	int nCase = 0, n = 0;
	
	
	/********************************************/

	if(argc > 1){	   // load the input file
		cout << "Read input from argc '" << argv[1] << "'" << endl;
		strcpy(argv[1], inputfile);	
	}else {
		cout << "Automatically read from '" << inputfile << "'" << endl;
	}

	inputfd.open(inputfile, fstream::in);

	if(inputfd.fail()){
		cerr << "error: cannot read file '" << inputfile << "'\n";
		inputfd.close();
		return -1;
	}

	outputfd.open(outfile);

	if(outputfd.fail()){
		cerr << "error: cannot create file '" << outfile << "'\n";
		outputfd.close();
		return -1;
	}

	inputfd >> nCase;	   //read case number
cout << "There is " << nCase << " cases." << endl;

	for(n = 0; n < nCase; n++){

		//read input file


		//process



		


		//write output file
		outputfd << "Case #" << n + 1 << ": " << endl;
		

	} // end process loop 
	
	inputfd.close();
	outputfd.close();
	return 0;
}








