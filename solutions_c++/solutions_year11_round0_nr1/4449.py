/*
 *  bottrust.cpp
 *  codejam_11
 *
 *  Created by Donny Lee on 5/6/11.
 *  Copyright 2011 Gaussian Technologies. All rights reserved.
 *
 */

#include "bottrust.h"
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string>
#include <math.h>
#include <set>
#include <stdlib.h>
#include <sstream>
#include <iomanip>
#include <vector>

using namespace std;

int main(int argc, char * const argv[]){
	
	int N; int No; int index; int case_no = 0;
	int org_pos = 1; int org_current = 0;
	int blu_pos = 1; int blu_current = 0;
	int current = 1;
	int pushing = 0;
	int time = 0;
	
	// Open file.
	ifstream file( "bottest.in" , ifstream::in );
	
	// Create output file.
	ofstream out("bottrust_output");			// <- We write to out using out << etc. //
	if(!out) { 
		cout << "Cannot open file.\n"; 
		return 1; 
	}
	
	// Also open an output file.
	string line; string line0; string line_no; char car;
	getline( file, line );
	N = atoi(line.c_str());
	while( getline( file, line ) )
	{
		// We already got a line here.
		No = atoi(line.c_str());			// No is the number of buttons to press.
		int seq[100][2];					// 1 is for orange, 2 is for blue.
		for  (int i = 0; i < 100; i++){
			for (int j = 0; j < 2; j++){
				seq[i][j] = 0;
			}
		}
		line0 = line.substr( line.find(" ") + 1 );
		line0 = line0 + " ";
		
		// Start reading into array.
		index = 0;
		while (line0.length() > 0) {
		car = line0[0];
			if ( car == 'O'){
				seq[index][0] = 1;
				line0 = line0.substr( line0.find(" ") + 1 );
				line_no = line0.substr( 0, line0.find(" ") + 1);
				seq[index][1] = atoi(line_no.c_str());
				index = index + 1;
				line0 = line0.substr( line0.find(" ") + 1 );
				
			} else {
				seq[index][0] = 2;
				line0 = line0.substr( line0.find(" ") + 1 );
				line_no = line0.substr( 0, line0.find(" ") + 1);
				seq[index][1] = atoi(line_no.c_str());
				index = index + 1;
				line0 = line0.substr( line0.find(" ") + 1 );
			}
		
		} // Data has been read into the array.

		org_pos = 1;
		blu_pos = 1;			// Both robots start at button 1.
		org_current = 0;
		blu_current = 0;
		time = 0;
		current = 0;			// This variables tells us where in the sequence we are.
		while (No > 0) {
			pushing = 0;		// Tell us whether button is being pushed.
			// It is important to get the next wanted positions for each robot.
			// Orange.
			for ( int i = current; i < 100; i++ ) {
				if (seq[i][0] == 1) {
					org_current = seq[i][1];
					break;
				} else {
					org_current = 0;
				}
			}
			// Blue.
			for ( int i = current; i < 100; i++ ) {
				if (seq[i][0] == 2) {
					blu_current = seq[i][1];
					break;
				} else {
					blu_current = 0;
				}
			}
				
			// Orange move first.
			if (org_pos == org_current && seq[current][0] == 1){
				No = No - 1;
				current = current + 1;	// Push button.
				pushing = 1;
				cout << "Orange push button at " << org_pos;
			} else {
				if ( org_pos < org_current && org_current != 0) {
					org_pos = org_pos + 1;
				}
				if ( org_pos > org_current && org_current != 0) {
					org_pos = org_pos - 1;
				}
				cout << "Orange move to " << org_pos;
			}
			cout << " ||| ";

			// Then blue.
			if (blu_pos == blu_current && seq[current][0] == 2 && pushing == 0){
				No = No - 1;
				current = current + 1;	// Push button.
				cout << "Blue push button at " << blu_pos << endl;
			} else {
				if ( blu_pos < blu_current && blu_current != 0) {
					blu_pos = blu_pos + 1;
				}
				if ( blu_pos > blu_current && blu_current != 0) {
					blu_pos = blu_pos - 1;
				}
				cout << "Blue move to " << blu_pos << endl;
			}
			time = time + 1;
		}
		cout << "Time is " << time << endl;
		case_no = case_no + 1;
		out << "Case #" << case_no << ": " << time << endl;
	}
	
	out.close(); 
	return 0;
}