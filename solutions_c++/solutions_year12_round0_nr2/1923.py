// round 1 problem B
// round 1 problem A

// read in text file
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>

using namespace std;
int main ()
{
    int intRead;
    char *filename = "B-large.in";
    ifstream infile(filename);
	int iType=0; // 0 is numCases, 1 is numGooglers, 2 is suprisings, 3 is p (the "best result" in question), 4 is a totalScore
	int numCases;
	int numGooglers;
	int numSurprisings;
	int caseUpTo=0;
	int p; // "best result"
	int numSuccesses;
	int totalScore;
	int scoreUpTo;

    if (!infile) {
        cout << "There was a problem opening " << filename << endl;
        return 0;
    }

	 // open file to write
  ofstream outfile ("output.txt");

    while (infile >> intRead) {
        if (iType==0) {
			// dealing with numCases
			numCases = intRead;
			iType++;
		} else if (iType==1) {
			// dealing with numGooglers
			numGooglers = intRead;
			iType++;
			// print out results from last time
			if (caseUpTo>0) { // starts from 1
				outfile << "Case #" << caseUpTo << ": " << numSuccesses << "\n";
			}
			// reset results from last time
			caseUpTo++;
			numSuccesses=0;
			scoreUpTo=0; // starts from 0
		} else if (iType==2) {
			// dealing with numSurprisings
			numSurprisings = intRead;
			iType++;
		} else if (iType==3) {
			// dealing with p
			p = intRead;
			if (numGooglers>0) {
				iType++;
			} else {
				// special case

				iType=1;
			}
		} else if (iType==4) {
			// dealing with totalScore
			totalScore = intRead;
			// check if can be done regularly
			if (totalScore>=(3*p-2)) {
				numSuccesses++;
			} else if ((numSurprisings>0)&(totalScore>=3*p-4)&(p>1)) { // check if can be done with a surprising
				numSuccesses++;
				numSurprisings--;
			}
			scoreUpTo++;
			// check if final number in line (scoreUpTo starts from 0)
			if (scoreUpTo==numGooglers) {
				iType=1;
			}
		}




    }

						// print out results from last time
			if (caseUpTo>0) { // starts from 1
				outfile << "Case #" << caseUpTo << ": " << numSuccesses << "\n";
			}
    return 0;





	


  return 0;
}

