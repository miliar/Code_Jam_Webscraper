//////////////////////////////////////////////////////////////////////////////////////
// Google Code Jam Program #3: Theme Park, by Steven A. Dunn, stevendunn@gmail.com ///
//                                                                                 ///
// Usage: ./project3 "input filename"                                              ///
//////////////////////////////////////////////////////////////////////////////////////

#include <fstream>
#include <string>
#include <algorithm>
#include <iterator>
#include <stdlib.h>
#include <sstream>
#include <vector>
#include <stdio.h>
#include <iostream>

int main( int argc, char* argv[] ) {

	// Process the input file
	std::ifstream inputFile;
	std::string inputString;
	inputFile.open(argv[1]);

	if( inputFile.is_open() ) {
		std::getline(inputFile, inputString ); // first line; this is the number of test cases
	}

	int numTestCases = atoi( inputString.c_str() );

	std::vector< std::vector<int> > rknList; // Hold the R, k and n values
	rknList.resize(numTestCases);
	for(int i = 0; i < numTestCases; i++) {
		rknList[i].resize(3);
	}

	std::vector< std::vector<int> > gList; // Hold the g lists (b/c C++ hates text parsing)
	gList.resize(numTestCases);

	int listCounter = 0;
	while(!inputFile.eof() && listCounter < rknList.size() ) {
		std::vector< std::string > rknElems; // will hold R, k and n values
		std::vector< std::string > gElems; // will hold g values

		std::getline(inputFile, inputString); // these are the R, k and n values 
		std::istringstream iss(inputString);
		copy( std::istream_iterator<std::string>(iss), std::istream_iterator<std::string>(), std::back_inserter<std::vector<std::string> >(rknElems));
		std::getline(inputFile, inputString); // these are the g values
		std::istringstream test(inputString);
		copy( std::istream_iterator<std::string>(test), std::istream_iterator<std::string>(), std::back_inserter<std::vector<std::string> >(gElems));

		int r = atoi(rknElems[0].c_str());
		int k = atoi(rknElems[1].c_str());
		int n = atoi(rknElems[2].c_str());
		
		rknList[listCounter][0] = r;
		rknList[listCounter][1] = k;
		rknList[listCounter][2] = n;
		
		gList[listCounter].resize(gElems.size()); 
		for(int i = 0; i <  gElems.size(); i++) {
			gList[listCounter][i] = atoi(gElems[i].c_str());
		}	

		listCounter++;
	}
	inputFile.close();
	
	for(int i = 0; i < numTestCases; i++) {
		int totalFare = 0; // the total amount of money made per test case
		int currentSeating = 0;
		int totalSeating = rknList[i][1]; // the total space available ( that is to say, k )
		int groupDivider = 0; // points to index array of next available group to ride
		int groupDividerCount = 0; // to avoid having the same group on the coaster simultaneously

		for(int j = 0; j < rknList[i][0]; j++) { // j -> R; this is the fill-up loop
			groupDividerCount = 0;
			while( gList[i][groupDivider] <= (totalSeating - currentSeating) && (totalSeating - currentSeating >= 0) && groupDividerCount < gList[i].size()) {
					currentSeating += gList[i][groupDivider]; // update seating
					if( groupDivider == (gList[i].size() - 1) ) { // get next group in looping queue
						groupDivider = 0;
						groupDividerCount++;
					} else {
						groupDivider++;
						groupDividerCount++;
					}
				
					}
					totalFare += currentSeating; // update the fare
					currentSeating = 0; // new ride
		}

		std::ofstream outputFile;
		outputFile.open("outputFile.txt", std::ios::out | std::ios::app);
		if(outputFile.is_open()) {
			outputFile << "Case #" << i + 1 << ": " << totalFare << "\n";
		}
		outputFile.close();
	}
	return 0;
}

