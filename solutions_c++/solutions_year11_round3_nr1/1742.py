/*
 *  magicka.cpp
 *  codejam_11
 *
 *  Created by Donny Lee on 5/7/11.
 *  Copyright 2011 Gaussian Technologies. All rights reserved.
 *
 */

#include "square.h"
#include "bottrust.h"
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string>
#include <cmath>
#include <set>
#include <stdlib.h>
#include <sstream>
#include <iomanip>
#include <vector>

using namespace std;

int check(double input) {
	int check = (int)input;
	int ret = 0;
	if ( input == check ) {
		return 1;
	} else {
		return 0;
	}
	return 0;
}


int main(int argc, char * const argv[]){
	
	// Necessary variables for reading.
	int N; int case_no = 0; int row; int col; int track; int rowpos; int colpos; int not_possible;
	string line; string line0;
	char data[50][50];
	
	// Variables here.
	
	// Open file.
	ifstream file( "square.in" , ifstream::in );
	
	// Create output file.
	ofstream out("square_output");			// <- We write to out using out << etc. //
	if(!out) { 
		cout << "Cannot open file.\n"; 
		return 1;
	}
	
	// This is to get the first line. We usually don't do anything with it.
	getline( file, line );
	
	N = atoi(line.c_str());
	while( getline( file, line ) )
	{
		// Clears certains identifiers.
		for (int i = 0; i < 50; i++) {
			for (int j = 0; j < 50; j++) {
				data[i][j] = '0';
			}
		}
		row = 0;
		col = 0;
		
		line0 = line.substr(  line.find(" ") + 1  );
		line = line.substr( 0, line.find(" ") );
		row = atoi(line.c_str());
		col = atoi(line0.c_str());
		
		//Read in the data.
		for (int i = 0; i < row; i++) {
			getline( file, line);
			for (int j = 0; j < col; j++) {
				line0 = line.substr( j, j+1);
				data[i][j] = line0[0]; 
			}
		}
		
		cout << "Row is " << row << " colume is " << col << endl;
		for (int i = 0; i < row; i++) {
			for (int j = 0; j < col; j++) {
				cout << data[i][j]; 
			}
			cout << endl;
		}
		
		
		track = 0;
		rowpos = 0; colpos = 0; not_possible = 0;
		// Read in the values and solve the problem. (May need additional getline( file, line ) commands).
		// SOLVE PROBLEM HERE.
		while (1) {
			rowpos = track / col;
			colpos = fmod((double)track, (double)col);
			
			// If it is a '#'.
			if (data[rowpos][colpos] == '#') {
				// Change if possible.
				if (data[rowpos][colpos+1] == '#' && data[rowpos+1][colpos] == '#' && data[rowpos+1][colpos+1] == '#') {
					data[rowpos][colpos] = '/';
					data[rowpos+1][colpos+1] = '/';
					data[rowpos+1][colpos] = '\\';
					data[rowpos][colpos+1] = '\\';
					track = 0;
				} else {
					// Not possible. Break and end.
					not_possible = 1;
					break;
					
				}	
		
			}	
			
			track = track + 1;
			if (track == row*col) {
				break;
			}
		}
		
		
		
		//cout << "Number " << 5 / 2 << endl;
		
		
		
		
		// For printing.
		case_no = case_no + 1;
		out << "Case #" << case_no << ":" << endl;
		if (not_possible == 1) {
			out << "Impossible" << endl;
		} else {
			for (int i = 0; i < row; i++) {
				for (int j = 0; j < col; j++) {
					out << data[i][j];
				}
				out << endl;
			}
			
		}
		
		
		// Do the necessary printing here.
		
		
		
		
	}
	
	out.close(); 
	
	
	
	
	
	cout << "The program has ended." << endl;
	return 0;
	
}