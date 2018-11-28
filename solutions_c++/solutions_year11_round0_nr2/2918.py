/* ========================================================================== //
//                        --= GOOGLE CODE JAM 2011 =--                        //
// ========================================================================== //
//                                  MAGICKA                                   //
// ========================================================================== //

	Qualification Round, Problem B.

// ========================================================================== */

// ========================================================================== //

//
#include <iostream>
#include <fstream>
using namespace std;
// ========================================================================== //


struct Combination{
	char elements[2];
	char result;
};
struct Opposition{
	char elements[2];
};

char checkCombination(char a, char b, 
	Combination *combinations, int combinationCount);
bool checkOpposition(char *elements, int elementCount, 
	Opposition *oppositions, int oppositionCount);


int main(){

	ifstream fileIn;
	fileIn.open("B-large.in");

	ofstream fileOut;
	fileOut.open("B-large.out");

	int testCount = 0;
	fileIn >> testCount;

	Combination *combinations = NULL;
	Opposition *oppositions = NULL;
	char *elementList = NULL;
	char *resultList = NULL;
	int resultLength = 0;

	for (int i = 0; i < testCount; i++){

		// Read combinations
		int combinationCount = 0;
		fileIn >> combinationCount;
		combinations = new Combination[combinationCount];

		for (int j = 0; j < combinationCount; j++){
			char combinationIn[4];
			fileIn >> combinationIn;
			Combination c;
			c.elements[0] = combinationIn[0];
			c.elements[1] = combinationIn[1];
			c.result = combinationIn[2];
			combinations[j] = c;
		}

		// Read oppositions
		int oppositionCount = 0;
		fileIn >> oppositionCount;
		oppositions = new Opposition[oppositionCount];

		for (int j = 0; j < oppositionCount; j++){
			char oppositionIn[3];
			fileIn >> oppositionIn;
			Opposition o;
			o.elements[0] = oppositionIn[0];
			o.elements[1] = oppositionIn[1];
			oppositions[j] = o;
		}

		// Add elements to list, processing after each one
		int elementCount = 0;
		fileIn >> elementCount;
		elementList = new char[elementCount+1];
		resultList = new char[elementCount];
		resultLength = 0;
		fileIn >> elementList;

		for (int j = 0; j < elementCount; j++){
			// Read a character
			resultList[resultLength] = elementList[j];
			resultLength++;
			// Loop until too short, or no combination match
			while (resultLength > 1){
				char elementA = resultList[resultLength-1];
				char elementB = resultList[resultLength-2];
				char result = checkCombination(elementA, elementB, 
					combinations, combinationCount);
				if (result != 0){
					resultList[resultLength-2] = result;
					resultLength--;
					continue;
				}
				break;
			}
			// Check oppositions
			if (checkOpposition(resultList, resultLength, 
				oppositions, oppositionCount))
			{
				resultLength = 0;
			}

		}

		fileOut << "Case #" << (i+1) << ": [";
		for (int j = 0; j < resultLength; j++){
			fileOut << resultList[j];
			if (j < resultLength-1)
				fileOut << ", ";
		}
		fileOut << "]\n";
		//fileOut << "Case #" << (i+1) << ": " << moveCount << "\n";

	}

	return 1;

}


char checkCombination(char a, char b, 
	Combination *combinations, int combinationCount)
{
	for (int i = 0; i < combinationCount; i++){
		// Check this element
		Combination c = combinations[i];
		if ((c.elements[0] == a && c.elements[1] == b) ||
			(c.elements[1] == a && c.elements[0] == b))
		{
			return c.result;
		}
	}
	return 0;
}

bool checkOpposition(char *elements, int elementCount, 
	Opposition *oppositions, int oppositionCount)
{
	char endElement = elements[elementCount-1];
	for (int i = 0; i < elementCount; i++){
		char a = elements[i];
		for (int j = 0; j < oppositionCount; j++){
			Opposition o = oppositions[j];
			if ((o.elements[0] == a && o.elements[1] == endElement) ||
				(o.elements[1] == a && o.elements[0] == endElement))
			{
				return true;
			}
		}
	}
	return false;
}