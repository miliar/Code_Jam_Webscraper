
#include <stdio.h>
#include <iostream>
#include <istream>
#include <fstream>
#include <sstream>
#include <map>

using namespace std;

template <class InputType>
bool ReadAtomicLine (InputType& returnValue, istream& inputStream) {

	
	/******************************/
	/* Read one entire line       */
	/******************************/


	string inputLine = "";
	
	while (inputLine.empty()) {
		if ( ! getline(inputStream, inputLine) ) {			
			return false;
		}
	}
	
	
	/******************************/
	/* Atomize line into tokens   */
	/******************************/


	istringstream inputLineStream(inputLine);	
	inputLineStream >> returnValue;
	
	return true;
}


int main(int argc, char **argv)
{
	/* I am too lazy for dynamic memory allocation here... */
	char DummyFileNameBuffer[255]; 
	/* Filename provided in input */
	char *pInputFileName = NULL;
	
	
	/******************************/
	/* Check input parameters     */
	/******************************/
	
	
	if (argc <= 1) { 
		
		/* No input parameters - read filename from std-in */
	
		cout << "No filename provided in input - please specify: ";
		cin >> DummyFileNameBuffer;
				
		pInputFileName = (char*) DummyFileNameBuffer;
		
	} else {
		
		/* Filename provided with input parameters */
		
		pInputFileName = (char*) argv[1];
	}
	

	/******************************/
	/* Open file                  */
	/******************************/
	

	ifstream currentLineStream;
	currentLineStream.open(pInputFileName);
	
	if ( ! currentLineStream.is_open()) {
		cout << "Unable to open file " << pInputFileName << " ... exit\n";
		return 1;
	}
	

	/******************************/
	/* Now Process Test Cases     */
	/******************************/


	unsigned int curTestCase;
	unsigned int totalNbTestCases;
	
	string curText = "";

	ReadAtomicLine<unsigned int>(totalNbTestCases, currentLineStream);
	
	unsigned int   nbDancingGooglers; /* N */
	unsigned short nbSpecialScores; /* S */
	unsigned short minimumP; /* p */
	
	unsigned short totalNbMatchingScores; /* output */
	
	
	for(curTestCase = 0; curTestCase < totalNbTestCases; curTestCase++) {
		
		/* Read next test case */
		
		string currentLine = "";
		
		getline(currentLineStream, currentLine);
		istringstream currentLineStream(currentLine);	
		
		currentLineStream >> nbDancingGooglers;
		currentLineStream >> nbSpecialScores;
		currentLineStream >> minimumP;
		
		/* Reinit variables */

		totalNbMatchingScores = 0;
		
		/* Get scores from input line & process */
		
		for(size_t pos = 0; pos < nbDancingGooglers; pos++) {
			
			unsigned int curGooglerScore = 0;
			unsigned int scoreClassification = 0;
			unsigned int scoreMinPoint = 0;
			
			currentLineStream >> curGooglerScore;
			
			/* either too bad or cheating ;) */
			if (curGooglerScore < minimumP || curGooglerScore > 30) {
				continue;
			}
			
			if (curGooglerScore == 30) {
				totalNbMatchingScores++;
				continue;
			}
			
			if (minimumP == 0) {
				totalNbMatchingScores++;
				continue;
			}			
						
			/* detect the score type */			
			scoreClassification = curGooglerScore % 3;
			scoreMinPoint       = curGooglerScore / 3;
						
			/* Now check if score matches criteria */	
			/*
			if (scoreMinPoint >= minimumP) {
				totalNbMatchingScores++;
			} else if ((scoreClassification == 1) && ((scoreMinPoint + 1) == minimumP) && (scoreMinPoint <= 9)) {
				totalNbMatchingScores++;
			} else if ((scoreClassification == 2) && ((scoreMinPoint + 1) == minimumP) && (scoreMinPoint <= 9)) {
				totalNbMatchingScores++;
			} else if ((scoreClassification != 1) && nbSpecialScores > 0) {
				
				if (((scoreMinPoint + 2) >= minimumP) && (scoreMinPoint <= 8)) {
					nbSpecialScores--;
					totalNbMatchingScores++;				
				}
			}
			 */
			if (scoreMinPoint >= minimumP) {
				totalNbMatchingScores++;
			} else if (scoreClassification == 0) {
				if (nbSpecialScores > 0 && scoreMinPoint+1 >= minimumP) {
					nbSpecialScores--;
					totalNbMatchingScores++;				
				}
			} else if (scoreClassification == 1) {
				if (scoreMinPoint+1 >= minimumP) {
					totalNbMatchingScores++;
				}
			} else { /* else if (scoreClassification == 2) */
				if (scoreMinPoint+1 >= minimumP) {
					totalNbMatchingScores++;
				} else if (nbSpecialScores > 0 && scoreMinPoint+2 >= minimumP && scoreMinPoint<=8) {
					nbSpecialScores--;
					totalNbMatchingScores++;				
				}
			}
		}
						
		cout << "Case #" << (curTestCase+1) << ": " << totalNbMatchingScores << endl; 
	}
	
	currentLineStream.close();
		
	return 0;
}
