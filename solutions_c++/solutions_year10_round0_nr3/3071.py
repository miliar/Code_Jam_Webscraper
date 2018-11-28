#include <string>
#include <list>
#include <fstream>
#include <iostream>

using namespace std;

void main()
{
	ifstream inFile("c:\\CodeJam\\A-small.in");
	ofstream outFile("c:\\CodeJam\\out");

	__int64 R, K, N, numberOfCases;

	inFile >> numberOfCases;

	for(int caseNumber = 1; caseNumber <= numberOfCases ; caseNumber++)
	{
		inFile >> R >> K >> N;

		double groups[1000];

		for(int i = 0 ; i < N ; i++)
		{
			inFile >> groups[i];
		}

		__int64 result = 0;
		int pointer = 0;

		for(__int64 j = 0 ; j < R ; j++)
		{
			__int64 k = 0;
			int firstPointer = pointer;

			while(k + groups[pointer] <= K)
			{			
				k += groups[pointer];
				result += groups[pointer];

				if(++pointer == N)
					pointer = 0;

				if(firstPointer == pointer)
					break;

			}
		}

		outFile << "Case #" << caseNumber << ":" << " " << result << endl;
	}
}


