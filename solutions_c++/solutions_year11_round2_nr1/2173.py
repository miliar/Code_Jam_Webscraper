/*
 *  magicka.cpp
 *  codejam_11
 *
 *  Created by Donny Lee on 5/7/11.
 *  Copyright 2011 Gaussian Technologies. All rights reserved.
 *
 */

#include "template.h"
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
	int N; int case_no = 0; int size_N;
	string line; string line0;
	char data[100][100];
	double score[100][5];		// NOTE: The first column is the total games played.
	double played; double won; vector<int> opp; vector<int> opp2; vector<int> opp3; double temp;
	double played2; double won2; double wonper; int temp_opp; vector<double> temp2;
	// Variables here.
	
	// Open file.
	ifstream file( "rpi_in" , ifstream::in );
	
	// Create output file.
	ofstream out("rpi_output");			// <- We write to out using out << etc. //
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
		// Clear up data[100][100].
		// Clear Data.
		for (int i = 0; i < 100; i++) {
			for (int j = 0; j < 100; j++) {
				data[i][j] = '0';
			}
		}
		// Clear Scores.
		for (int i = 0; i < 100; i++) {
			score[i][0] = 0;
			score[i][1] = 0;
			score[i][2] = 0;
			score[i][3] = 0;
			score[i][4] = 0;
		}
		played = 0;
		
		size_N = atoi(line.c_str());
		
		for (int i = 0; i < size_N; i++) {
			getline(file, line);
			for (int j = 0; j < size_N; j++) {
				line0 = line.substr( j, j+1);
				data[i][j] = line0[0];
			}
		}

		// Data is read into data.
		
		
		// Calculate games played.
		for (int i = 0; i < size_N; i++) {
			opp2.clear();
			opp.clear();
			played = 0;
			for (int j = 0; j < size_N; j++ ) {
				if ( data[i][j] != '.' ) {
					opp.push_back(j);
					opp2.push_back(j);
					played = played + 1;
				}
			}
			score[i][0] = played;
			
			//cout << "Played is " << played << endl;
			
			
			won = 0;
			for (int j = 0; j < size_N; j++ ) {
				if ( data[i][j] == '1' ) {
					won = won + 1;
				}
			}
			score[i][1] = won / score[i][0];
		}
		
		// opp and opp2 will have the opponents PLAYED.
		
		for (int i = 0; i < size_N; i++) {
			won = 0;
			for (int j = 0; j < size_N; j++ ) {
				if ( data[i][j] == '1' ) {
					won = won + 1;
				}
			}
			score[i][1] = won / score[i][0];
			cout << "WIN is: " << score[i][1] << endl;
		}
		
		// Check this.
		
		for (int i = 0; i < size_N; i++ ) {
			
			opp2.clear();
			opp.clear();
			for (int j = 0; j < size_N; j++ ) {
				if ( data[i][j] != '.' ) {
					opp.push_back(j);
					opp2.push_back(j);
				}
			}
			
			
			cout << "Dealing with player " << i << endl;
			temp = 0; temp2.clear(); wonper = 0;
			while ( opp.empty()!=1 ) {
				// Must recalculate winning %. Do the same long algorithm. But throw out i.
				temp_opp = opp.back();
				cout << "Calculating special WP for " << temp_opp << " ";
				// Calculate games played and won.
				//temp2.clear();
				played2 = 0; won2 = 0; wonper = 0;
				for (int j = 0; j < size_N; j++ ) {
					if ( data[temp_opp][j] != '.' && ( j != i ) ) {
						played2 = played2 + 1;
					}
					if ( data[temp_opp][j] == '1' && ( j != i ) ) {
						won2 = won2 + 1;
					}
				}
				temp2.push_back( won2 / played2 );
				opp.pop_back();
				cout << "OP is " << won2 / played2 << endl;
			}
			// Need to take the average of all the change winning percentage.
			
			wonper = 0;
			while ( temp2.empty()!=1 ) {
				wonper = wonper + temp2.back();
				temp2.pop_back();
			}
			//cout << 
			
			score[i][2] = wonper / score[i][0];
			cout << "RESULT IS " << score[i][2] << endl;
		}
		
		for (int i = 0; i < size_N; i++ ) {
			temp = 0;
			
			
			opp2.clear();
			for (int j = 0; j < size_N; j++ ) {
				if ( data[i][j] != '.' ) {
					opp2.push_back(j);
				}
			}
			
			
			
			
			while ( opp2.empty()!=1 ) {
				temp = temp + score[opp2.back()][2];
				opp2.pop_back();
			}
			score[i][3] = temp / score[i][0];
		}
		
		for (int i = 0; i < size_N; i++ ) {
			score[i][4] = 0.25 * score[i][1] + 0.50 * score[i][2] + 0.25 * score[i][3];
		}
		
		/*
		for (int i = 0; i < size_N; i++) {
			cout << score[i][0] << endl;
		}
		*/
		
		//line0 = line.substr(  line.find(" ") + 1  );
		//No_com = atoi(line0.c_str());
		
		// Read in the values and solve the problem. (May need additional getline( file, line ) commands).
		
		// For printing.
		case_no = case_no + 1;
		out << "Case #" << case_no << ":" << endl;
		for (int i = 0; i < size_N; i++) {
			out << score[i][4] << endl;
		}
		
		// Do the necessary printing here.
	}
	
	out.close(); 
	
	/*
	char sample[3];
	sample[0] = 'r';
	
	cout << (sample[0] == 'e') << endl;
	*/
	//cout << data[0][0] ==  << endl;
	
	cout << "The program has ended." << endl;
	return 0;
	
}