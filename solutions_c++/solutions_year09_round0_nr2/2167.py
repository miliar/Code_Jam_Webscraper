/* B.cpp
 * Watersheds Problem
 * Google Code Jam 2009
 * By: Michael Robertson
 * mikejrobertson AT gmail DOT com
 * Updated: 3 September 2009
 */

#include <iostream>
#include <fstream>

// Files
#define INFILE "B-large.in"
#define OUTFILE "out"

using namespace std;
char letter;

char getletter (int h, int w, int Case,int flowsTo[100][100][3],char basin[100][100][100]);

int main() {
	int numCases;
	int height, width;
	int altitudes[100][100];
	int flowsTo[100][100][3];
	char basin[100][100][100];
	//Read file and get number cases
	ifstream file;	
	file.open(INFILE);
	if (file.is_open()) {
		file >> numCases;
	} else {
		cerr << "Error opening file" << endl;
	}
	
	// Set up output file
	ofstream fileout;
	fileout.open(OUTFILE);
	
	// Repeat once for each Case
	for (int Case = 0; Case <numCases; Case++) {
		
		letter = 'a';
		
		// Read altitudes in to array
		file >> height;
		file >> width;
		for (int h = 0; h < height; h++) {
			for (int w = 0; w < width; w++) {
				file >> altitudes[h][w];
			}
		}
		
		// Find lowest neighboring cell and store in flowsTo
		// If its a sink store -1, -1, 0
		for (int h = 0; h < height; h++) {
			for (int w = 0; w < width; w++) {
				flowsTo[h][w][3] = 10001;
				
				// Test South
				if ((h+2 <= height) && (altitudes[h][w] > altitudes[h+1][w])) {
					flowsTo[h][w][1] = h+1;
					flowsTo[h][w][2] = w;
					flowsTo[h][w][3] = altitudes[h+1][w];
				}
				
				// Test East
				if ((w+2 <= width) && (altitudes[h][w] > altitudes[h][w+1])) {
					if (flowsTo[h][w][3] >= altitudes[h][w+1]) {
						flowsTo[h][w][1] = h;
						flowsTo[h][w][2] = w+1;
						flowsTo[h][w][3] = altitudes[h][w+1];
					}
				}
				
				// Test West
				if ((w-1 >= 0) && (altitudes[h][w] > altitudes[h][w-1])) {
					if (flowsTo[h][w][3] >= altitudes[h][w-1]) {
						flowsTo[h][w][1] = h;
						flowsTo[h][w][2] = w-1;
						flowsTo[h][w][3] = altitudes[h][w-1];
					}
				}
				
				// Test North
				if ((h-1 >= 0) && (altitudes[h][w] > altitudes[h-1][w])) {
					if (flowsTo[h][w][3] >= altitudes[h-1][w]) {
						flowsTo[h][w][1] = h-1;
						flowsTo[h][w][2] = w;
						flowsTo[h][w][3] = altitudes[h-1][w];
					}
				}
				// Else sink
				if (flowsTo[h][w][3] == 10001) {
					flowsTo[h][w][1] = -1;
					flowsTo[h][w][2] = -1;
				}			
				//cout << "[" << flowsTo[h][w][1] << " ";
				//cout << flowsTo[h][w][2] << " ";
				//cout << flowsTo[h][w][3] << "] ";
			}
			//cout << endl;
		}
		
		// Find letters
		for (int h = 0; h < height; h++) {
			for (int w = 0; w < width; w++) {
				getletter(h, w, Case, flowsTo, basin);
			}
		}
		
		
		// Write output to file
		if (fileout.is_open()) {
			cout << "Case #" << Case+1 << ":\n";
			fileout << "Case #" << Case+1 << ":\n";
			for (int h = 0; h < height; h++) {
				for (int w = 0; w < width; w++) {
					cout << basin[h][w][Case] << " ";
					fileout << basin[h][w][Case] << " ";
				}
				cout << endl;
				fileout << endl;
			}	
		} else {
			cerr << "Error can't open file to write" << endl;
		}
	}
	file.close();
	return 0;
}

char getletter (int h, int w, int Case,int flowsTo[100][100][3],char basin[100][100][100]) {
	if (flowsTo[h][w][3] == -1) {
		return basin[h][w][Case];	
	} else if (flowsTo[h][w][3] == 10001) {
		basin[h][w][Case] = letter++;
		flowsTo[h][w][3] = -1;
		return basin[h][w][Case];
	} else {
		int h1 = flowsTo[h][w][1];
		int w1 = flowsTo[h][w][2];
		return basin[h][w][Case] = getletter(h1, w1, Case, flowsTo, basin);
	}
}
