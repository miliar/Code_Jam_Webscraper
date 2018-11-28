#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <set>

using namespace std;

int main(int argc, char ** argv){
    ifstream inFile;
    ofstream outFile;

    int count;
    int count2;
    int count3;

    int lowLimit;
    int highLimit;

    int tempValue;
    int tempValue2;

    int limit;
    int cipher;

    int realCount;

    int numberOfTestCase;

    set<int> tempSet;

    pair<set<int>::iterator, bool> overlapTest;

    inFile.open(argv[1]);
    outFile.open(argv[2]);

    inFile >> numberOfTestCase;

    for(count = 0 ; numberOfTestCase > count ; count++){
	outFile << "Case #" << count + 1 << ": ";

	inFile >> lowLimit;
	inFile >> highLimit;

	realCount   = 0;

	for(count2 = lowLimit ; highLimit >= count2 ; count2++){
	    limit   = static_cast<int>(floor(log10(static_cast<double>(count2))));
	    cipher  = static_cast<int>(pow(10., static_cast<double>(limit)));

	    tempValue	= count2;
	    tempSet.clear();

	    for(count3 = 0 ; limit > count3 ; count3++){
		tempValue2  = tempValue %10;
		tempValue   /= 10;
		tempValue   += (tempValue2 * cipher);

		if((tempValue > count2) && (tempValue <= highLimit)){
		    overlapTest	= tempSet.insert(tempValue);
		    if(overlapTest.second == true){
			realCount++;
		    }
		}
	    }
	}
	outFile << realCount << endl;
    }
    outFile.close();
    inFile.close();

    return EXIT_SUCCESS;
}

