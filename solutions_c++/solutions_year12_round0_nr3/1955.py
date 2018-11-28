// round 1 problem C

// read in text file
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;
int main ()
{
    int intRead;
    char *filename = "C-large.in";
    ifstream infile(filename);
	int iType=0; // 0 is numCases, 1 is lower boundary, 2 is upper boundary
	int numCases;
	int caseUpTo=1;
	int numSuccesses=0;
	int lowerBound;
	int upperBound;
	int numDigits;
	int working;
	int potentialSuccesses[9];
	int firstDigit;
	int curDigit;
	int n;
	int possibleSuccess;
	bool unique;
	int i;
	int j;

    if (!infile) {
        cout << "There was a problem opening " << filename << endl;
        return 0;
    }

	 // open file to write
  ofstream outfile ("output.txt");

    while (infile >> intRead) {
        if (iType==0) {
			numCases=intRead;
			iType++;
		} else if (iType==1) {
			// lower boundary
			lowerBound=intRead;
			iType++;
		} else if (iType==2) {
			// upper boundary
			upperBound=intRead;
			iType--;
			// find number of successes
			for (n=lowerBound;n<=upperBound;n++) {
				for (i=0;i<9;i++) {
					potentialSuccesses[i]=0;
				}
				// first check for following digits that are greater than the first digit
				
				// get number of digits
				working=n;
				numDigits=0;
				while (working>0) {
					working=working/10; // integer division cuts off remainder
					numDigits++;
				}

				
				firstDigit=n/int(pow(float(10),(numDigits-1)));
				for (i=1;i<numDigits;i++) {
					curDigit=n%int((pow(float(10),(numDigits-i))))/int((pow(float(10),(numDigits-i-1))));
					//cout << int((pow(float(10),(numDigits-i)))) << '\n';
					//cout << n%int((pow(float(10),(numDigits-i)))) << '\n';
					//cout << int((pow(float(10),(numDigits-i-1)))) << '\n';
					if (curDigit>firstDigit) { // check for all digits greater than the first digit
						// place recycled number in potential successes array
						possibleSuccess=n%int(pow(float(10),(numDigits-i)))*int(pow(float(10),i)) + n/int(pow(float(10),(numDigits-i)));
						if (possibleSuccess<=upperBound) {
							potentialSuccesses[i]=possibleSuccess;
						}
					} else if (curDigit==firstDigit) { // check for all digits the same as the first digit
						possibleSuccess=n%int(pow(float(10),(numDigits-i)))*int(pow(float(10),i)) + n/int(pow(float(10),(numDigits-i)));
						if ((possibleSuccess>n)&(possibleSuccess<=upperBound)) {
							potentialSuccesses[i]=possibleSuccess;
						}
					}
				}

				// for each unique potentialSuccess, add 1 to the successes
				for (i=0;i<9;i++) {
					unique=true;
					if (potentialSuccesses[i]!=0) {
						// check if unique
						for (j=0;j<i;j++) {
							if (potentialSuccesses[i]==potentialSuccesses[j]) {
								unique=false;
								break;
							}
						}
						if (unique) {
							numSuccesses++;
						}
					}

				}

			}
			// print results
			outfile << "Case #" << caseUpTo << ": " << numSuccesses << "\n";
			cout << "Case #" << caseUpTo << ": " << numSuccesses << "\n";
			caseUpTo++;
			numSuccesses=0;



			
		}

	}
	
}