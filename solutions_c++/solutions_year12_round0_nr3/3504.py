
/*
Written By Jack Vucemillo.
On 14/04/2012.
Last known email address: shadow.wraith.12@gmail.com
*/


#include <fstream>
#include <string>
#include <iostream>
#include <sstream>
#include <math.h>


int main()
{
	// open/create the input/output files
	std :: fstream inFile("C-small-attempt1.in", std :: ios :: in);
	std :: fstream outFile("C-small-attempt1.out", std :: ios :: out | std :: ios :: trunc);


	// read the number of test cases
	int problemCount = 0;
	inFile >> problemCount;


	// for each problem in the problem set
	for(int problem = 0; problem < problemCount; problem ++)
	{
		std :: cout << "Case: " << problem + 1 << std :: endl;

		// get the parameters
		int valueA = 0;
		inFile >> valueA;
		int valueB = 0;
		inFile >> valueB;

		int nMin = valueA;
		int nMax = valueB - 1;
		int mMax = valueB;




		// A <= n < m <= B
		// valueA <= nNumber < mNumber <= valueB
		// for each number n between valueA and valueB-1
		// for each number m between n+1 and valueB
		// for each valid permutation of the value string
		// mark true and continue if the permutation is valid

		
		// abcdefg
		// (abcdefg[3] = 'd')
		// cut position = 1
		// abcdefg[1] = 'b'
		// size = 7
		// abcdefg.substr(cutPosition, size - cutPosition) + abcdefg.substr(0, cutPosition)


		// for each possible pair of numbers
		
		std :: string nString;
		std :: stringstream nss;
		std :: string mString;
		std :: stringstream ss;
		std :: string newString;
		int pairCount = 0;
		for(int n = nMin; n <= nMax; n ++) // for each low number
		{
			nString.clear();
			nss.clear();
			nss << n;
			nss >> nString;
			for(int m = n + 1; m <= mMax; m ++) // for each number above that
			{
				// capture m as a string
				mString.clear();
				ss.clear();
				ss << m;
				ss >> mString;
				int mStringSize = mString.size();


				if(mString.find_first_not_of(nString) != std :: string :: npos)
					continue;

				if(nString.find_first_not_of(mString) != std :: string :: npos)
					continue;


				for(int cutPosition = 1; cutPosition < mStringSize; cutPosition ++) // for each permutation of m
				{
					newString = mString;
					newString.replace(0, cutPosition, mString, mStringSize - cutPosition, cutPosition);
					newString.replace(cutPosition, mStringSize - cutPosition, mString, 0, mStringSize - cutPosition);
					if(newString == nString)
					{
						pairCount ++;
						break;
					}
				}
			}
		}


		// output the solution
		outFile << "Case #" << problem + 1 << ": " << pairCount;
		if(problem + 1 < problemCount)
			outFile << std :: endl;
	}


	// close the input/output files
	inFile.close();
	outFile.close();
}
