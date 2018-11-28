/* ========================================================================== //
//                        --= GOOGLE CODE JAM 2011 =--                        //
// ========================================================================== //
//                               CANDY SPLITTING                              //
// ========================================================================== //

	Qualification Round, Problem C.

// ========================================================================== */

// ========================================================================== //

//
#include <iostream>
#include <fstream>
using namespace std;
// ========================================================================== //


#define MAX_CANDIES (1024)


int checkPiles(int *list, int *mask, int count){

	int wrongA = 0;
	int wrongB = 0;
	int realA = 0;
	int realB = 0;
	for (int i = 0; i < count; i++){
		int candyValue = list[i];
		int candyMask = mask[i];
		if (0 == candyMask){
			wrongA ^= candyValue;
			realA += candyValue;
		}
		else{
			wrongB ^= candyValue;
			realB += candyValue;
		}
	}

	if (wrongA == wrongB){
		return max(realA, realB);
	}
	return 0;
}

int main(){

	ifstream fileIn;
	fileIn.open("C-small-attempt1.in");

	ofstream fileOut;
	fileOut.open("C-small-attempt1.out");

	int testCount = 0;
	fileIn >> testCount;

	int *candyList = new int[MAX_CANDIES];
	int *candyMask = new int[MAX_CANDIES];

	for (int i = 0; i < testCount; i++){

		int bestResult = 0;

		// Ready candy
		int candyCount = 0;
		fileIn >> candyCount;

		memset(candyList, 0, sizeof(int) * candyCount);
		memset(candyMask, 0, sizeof(int) * candyCount);
		for (int j = 0; j < candyCount; j++){
			fileIn >> candyList[j];
		}
		
		// Brute force check each possibility
		while (true){
			// Update mask
			int maskCount = 0;
			int maskCarry = candyMask[0];
			candyMask[0] = candyMask[0] ^ 1;
			maskCount += candyMask[0];
			for (int j = 1; j < candyCount; j++){
				int maskCarryLast = maskCarry;
				maskCarry = candyMask[j] & maskCarryLast;
				candyMask[j] = candyMask[j] ^ maskCarryLast;
				maskCount += candyMask[j];
			}
			if (maskCount >= candyCount)
				break;

			bestResult = max(bestResult, checkPiles(candyList, candyMask, candyCount));

		}

		fileOut << "Case #" << (i+1) << ": ";
		if (bestResult == 0)
			fileOut << "NO";
		else
			fileOut << bestResult;
		fileOut << "\n";

	}

	return 1;

}