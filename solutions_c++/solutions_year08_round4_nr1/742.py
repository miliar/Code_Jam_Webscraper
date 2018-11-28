#include "Common.h"
#include "Solver.h"

/*
const char* INPUT_FILE_NAME  = "input.txt";
const char* OUTPUT_FILE_NAME = "output.txt";
*/
/*
const char* INPUT_FILE_NAME  = "A-small-attempt0.in";
const char* OUTPUT_FILE_NAME = "A-small-attempt0.out";
*/

const char* INPUT_FILE_NAME  = "A-large.in";
const char* OUTPUT_FILE_NAME = "A-large.out";



int main()
{
	int iNumTestCases = 0;

	fstream inputFileStream(INPUT_FILE_NAME, ios_base::in);
	fstream outputFileStream(OUTPUT_FILE_NAME, ios_base::out|ios_base::trunc);

	outputFileStream.setf(ios_base::floatfield, ios_base::fixed);
	outputFileStream.precision(6);
	cout.setf(ios_base::floatfield, ios_base::fixed);
	cout.precision(6);

	inputFileStream >> iNumTestCases;

	for(int i=0 ; i<iNumTestCases ; ++i)
	{
		int numNodes, desiredRoot;

		inputFileStream >> numNodes >> desiredRoot;

		int* array = new int[numNodes+1];
		int* changable = new int[numNodes+1];

		for(int currentIndex=1 ; currentIndex<=numNodes ; ++currentIndex)
		{
			inputFileStream >> array[currentIndex];

			if(currentIndex <= (numNodes-1)/2)
				inputFileStream >> changable[currentIndex];
		}

		int leafBegin = (numNodes-1)/2 + 1;
		Solver solver(array, changable, desiredRoot, leafBegin);

		int result = solver.solve();
		
		if(result==INT_MAX)
			outputFileStream << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
		else
			outputFileStream << "Case #" << i+1 << ": " << result << endl;
		cout << "Case #" << i+1 << ": " << result << endl;

		delete[] array;
		delete[] changable;
	}

	return 0;
}
