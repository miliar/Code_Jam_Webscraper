// Ben Foxworthy
// 5-22-10

#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
	const char *inputFileName = NULL;
	char inputFileBuffer[256];
	if (argc == 2){
		inputFileName = argv[1];
	} else {
		cout << "Input file: ";
		cin >> inputFileBuffer;
		inputFileName = inputFileBuffer;
		cout << inputFileName << endl;
	}

	ifstream input(inputFileName);
	//ofstream output("output.txt");
	
	if (input.fail()){// || output.fail()){
		cout << "Error: Files couldn't be opened" << endl;
		system("PAUSE");
		return 1;
	}
	
	int numTestCases = 0;
	input >> numTestCases;
	
	for (int iCase = 0; iCase < numTestCases; iCase++){
		int numChicks;  //N
		int numRequired; //K
		int barnDist; //B
		int maxTime;  //T
		int chickPos[100];
		int chickSpeed[100];

		int numSwaps = 0;

		input >> numChicks;
		input >> numRequired;
		input >> barnDist;
		input >> maxTime;

		for (int i = 0; i < numChicks; i++){
			input >> chickPos[i];
		}
		for (int i = 0; i < numChicks; i++){
			input >> chickSpeed[i];
		}


		for (int i = numChicks-1; i >=0 ; --i){

			if (numRequired == 0){
				break;
			}

			if ((chickPos[i] + (chickSpeed[i] * maxTime)) >= barnDist){
				--numRequired;
			} else {
				numSwaps += numRequired;
			}
		}

		if (numRequired == 0){
			cout << "Case #" << iCase+1 << ": " << numSwaps << endl;
		} else {
			cout << "Case #" << iCase+1 << ": " << "IMPOSSIBLE" << endl;
		}
	}
	
    return EXIT_SUCCESS;
}
