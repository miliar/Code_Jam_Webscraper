#include "Common.h"
#include "Solver.h"
/*
const char* INPUT_FILE_NAME  = "input.txt";
const char* OUTPUT_FILE_NAME = "output.txt";
*/

const char* INPUT_FILE_NAME  = "D-small-attempt0.in";
const char* OUTPUT_FILE_NAME = "D-small-attempt0.out";

/*
const char* INPUT_FILE_NAME  = "D-large.in";
const char* OUTPUT_FILE_NAME = "D-large.out";
*/

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
		int k;
		inputFileStream >> k;
		string dataString;
		inputFileStream >> dataString;

		Solver solver(k, dataString);

		solver.addData();

		int result = solver.solve();

		outputFileStream << "Case #" << i+1 << ": " << result << endl;
		cout << "Case #" << i+1 << ": " << result << endl;
	}

	inputFileStream.close();
	outputFileStream.flush();
	outputFileStream.close();


	return 0;
}
