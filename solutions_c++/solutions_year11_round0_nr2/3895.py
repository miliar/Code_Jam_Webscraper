/*
 *  magicka.cpp
 *  codejam_11
 *
 *  Created by Donny Lee on 5/7/11.
 *  Copyright 2011 Gaussian Technologies. All rights reserved.
 *
 */

#include "magicka.h"
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
	
	string line; string line0; 
	int N; int No_com; int No_opp; int No_length; char char_1; char char_2; int check = 0;
	char new_char; int check2; char temp; int seq_size; int check_clear; int case_no = 0;
	
	// Open file.
	ifstream file( "magicka.in" , ifstream::in );
	
	// Create output file.
	ofstream out("magicka_output");			// <- We write to out using out << etc. //
	if(!out) { 
		cout << "Cannot open file.\n"; 
		return 1;
	}
	
	vector<char> sequence;
	
	getline( file, line );
	N = atoi(line.c_str());
	while( getline( file, line ) )
	{
		sequence.clear();
		No_com = atoi(line.c_str());
		line0 = line.substr(  line.find(" ") + 1  );
		
		// Read the combined elements.
		char combine[No_com][3];
		for (int i = 0; i < No_com; i++) {
			combine[i][0] = line0[0];
			combine[i][1] = line0[1];
			combine[i][2] = line0[2];
			line0 = line0.substr(  line0.find(" ") + 1  );
		}
		
		No_opp = atoi(line0.c_str());
		line0 = line0.substr(  line0.find(" ") + 1  );
		char opposed[No_opp][2];
		for (int i = 0; i < No_opp; i++) {
			opposed[i][0] = line0[0];
			opposed[i][1] = line0[1];
			line0 = line0.substr(  line0.find(" ") + 1  );
		}

		No_length = atoi(line0.c_str());
		line0 = line0.substr(  line0.find(" ") + 1  );
		
		// Insert the first element first.
		sequence.push_back(line0[0]);
		
		// This is for each new line.
		// Insert new character here.
		check_clear = 0;
		for (int i = 1; i < line0.length(); i++){
			
			if (check2 == 1)
			{
				sequence.push_back(line0[i]);
				check2 = 0;
				continue;
			}

			new_char = line0[i];
			sequence.push_back(line0[i]);
			//line0 = line0.substr(  line0.find(" ") + 1  );
			
			// Do the correct alterations to the sequence.
			
			// 1. Check on last two elements and see whether they in the combined list.
			

			
			check = 0;
			char_1 = sequence[sequence.size() - 2];
			char_2 = sequence[sequence.size() - 1];
			for ( int i = 0; i < No_com; i++ ) {
				if ( char_1 == combine[i][0] )
					if ( char_2 == combine[i][1] ){
						sequence.pop_back();
						sequence.pop_back();
						sequence.push_back(combine[i][2]);
						check = 1;
						new_char = combine[i][2];
						break;
					}
			}
				
			if (  check == 0 ){
				
				char_1 = sequence[sequence.size() - 1];
				char_2 = sequence[sequence.size() - 2];

				for ( int i = 0; i < No_com; i++ ) {
					if ( char_1 == combine[i][0] )
						if ( char_2 == combine[i][1] ){
							sequence.pop_back();
							sequence.pop_back();
							sequence.push_back(combine[i][2]);
							new_char = combine[i][2];
							break;
						}
				
				
				}
			}
			
			
			// 2. Check elements that opposed each other.
			
			seq_size = sequence.size();
			for ( int j = 0; j < No_opp; j++ ) {
				if ( new_char == opposed[j][0] ){
					for (int k = 0; k < seq_size - 1; k++) {
						temp = sequence[k];
						if ( temp == opposed[j][1] ) {
							sequence.clear();
							check2 = 1;
							check_clear = 1;
							break;
						}
					}
				}
				break;
			}
			
			// Do the reverse.
			if (check_clear == 0){
				for ( int j = 0; j < No_opp; j++ ) {
					if ( new_char == opposed[j][1] ){
						for (int k = 0; k < seq_size - 1; k++) {
							temp = sequence[k];
							if ( temp == opposed[j][0] ) {
								sequence.clear();
								check2 = 1;
								break;
							}
						}
					}
					break;
				}
			}
			
			 
			
			// End of number 2 check.
			/*
			cout << "The Sequence NOW is ";
			for (int i = 0; i < sequence.size(); i++){
				cout << sequence[i];
			}
			cout << endl;
			*/

			
		} // Changes for each line.
		cout << "The ANSWER is ";
		for (int i = 0; i < sequence.size(); i++){
			cout << sequence[i];
		}
		cout << endl;
		
		// Printing.
		
		case_no = case_no + 1;
		out << "Case #" << case_no << ": [";
		for (int i = 0; i < sequence.size(); i++){
			out << sequence[i];
			if (i != sequence.size() - 1){
			 out << ", ";	
			}
		}
		out << "]" << endl;
		
	} // End of while Loop.
	
	out.close(); 
	
	return 0;
}

