#include <iostream>
#include <xutility>
#include <vector>

using namespace std;

void SolveTest();

void main()
{
	int numTests;
	cin >> numTests;

	for(int i = 0; i < numTests; ++i)
	{
		SolveTest();
	}
}

void SolveTest() 
{
	static int testNum = 0;
	++testNum;

	int numPieces;
	cin >> numPieces;

	int smallestPiece = INT_MAX;

	int realSum = 0;
	int xorSum = 0;
	for(int i = 0; i < numPieces; ++i)
	{
		int nextNumber;
		cin >> nextNumber;

		realSum += nextNumber;
		xorSum = xorSum ^ nextNumber;

		if(smallestPiece > nextNumber)
			smallestPiece = nextNumber;
	}

	cout << "Case #" << testNum << ": ";
	if(xorSum == 0 && numPieces >= 2)
	{
		//There is a solution. Just give smallest piece to the kid and take realSum - smallestPiece
		cout << realSum - smallestPiece << endl;
	}
	else
	{
		cout << "NO" << endl;
	}
	const bool hasResult = xorSum == 0 && numPieces >= 2;	

}