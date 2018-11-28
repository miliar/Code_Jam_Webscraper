// Ben Foxworthy
// 5-8-10

#include <cstdlib>
#include <iostream>
#include <fstream>

#include "bigint.h"

using namespace std;


// from http://en.wikipedia.org/wiki/Euclidean_algorithm
RossiBigInt gcd(const RossiBigInt &a, const RossiBigInt &b)
{
	if (a == b){
		return a;
	}
	if (b == RossiBigInt(0)){
		return a;
	} else {
		return gcd(b, a%b);
	}
}


int main(int argc, char *argv[])
{
	char buffer[64001];
	int x;
	
	if (argc != 2){
		cout << "No input file (usage: blah.exe <input file>)" << endl;
		return 1;
	}

	ifstream input(argv[1]);
	//ofstream output("output.txt");
	
	if (input.fail()){// || output.fail()){
		cout << "Error: Files couldn't be opened" << endl;
		system("PAUSE");
		return 1;
	}
	
	input.getline(buffer, 64000);
	int numLines = atoi(buffer);
	
	for (int iLine = 0; iLine < numLines; iLine++){
		input.getline(buffer, 64000);
		unsigned int numValues = atoi(buffer);
		
		RossiBigInt *intArray = new RossiBigInt[numValues];

		int numberIndex = 0;
		char *pos = buffer;
		while (pos && *pos && *pos != ' '){
			pos++;
		}
		while (pos && *pos && *pos == ' '){
			pos++;
		}
		char *startPos = pos;
		while (pos && *pos && numberIndex < numValues){
			if (*pos == ' '){
				*pos = '\0';
				pos++;
				intArray[numberIndex++] = RossiBigInt(string(startPos), 10);
				//cout << intArray[numberIndex-1] << endl;
				startPos = pos;
			}
			pos++;
		}
		if (!(*pos) && numberIndex < numValues){
			intArray[numberIndex] = RossiBigInt(string(startPos), 10);
			//cout << intArray[numberIndex] << endl;
		}
		
		// Find GCD
		RossiBigInt iGcd;
		if (intArray[0] > intArray[1]){
			iGcd = (intArray[0] - intArray[1]);
		} else {
            iGcd = (intArray[1] - intArray[0]);
		}
		
		for (int i = 1; i < numValues-1; i++){
			RossiBigInt diff;
			if (intArray[i] > intArray[i+1]){
				diff = (intArray[i] - intArray[i+1]);
			} else {
	            diff = (intArray[i+1] - intArray[i]);
			}
			
			iGcd = gcd(iGcd, diff);
		}
		
		RossiBigInt iAnswer = iGcd - (intArray[0] % iGcd);
		if (iGcd == RossiBigInt(1)){
			iAnswer = RossiBigInt(0);
		}
		if (iAnswer == iGcd){
			iAnswer = RossiBigInt(0);
		}

		cout << "Case #" << iLine+1 << ": " << iAnswer << endl;
		
	}
	
    return EXIT_SUCCESS;
}
