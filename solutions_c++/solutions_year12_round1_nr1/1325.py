// CodeJam2012Round1AProblemA.cpp : Defines the entry point for the console application.
//
//Include some standard headers for windows/STL
#include <tchar.h>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
using namespace std;
#define MAXIMUM 999999
double vectorMin(vector<double> A)
{
double minSoFar = MAXIMUM;
for( int i=0;i<A.size();i++)
{
	if (A[i]<minSoFar)
		minSoFar=A[i];
}

return minSoFar;
}


int _tmain(int argc, _TCHAR* argv[])
{
		std::ifstream infile("A-large.in");	
		std::ofstream outfile("A-large.out");
		outfile<<setprecision(10);


		int totalCases = 0;

		infile>>totalCases;
		for (int i = 1;i<=totalCases;i++)
		{
			int numberTyped, numberTotal;
			infile>>numberTyped>>numberTotal;
			vector<double> probabilityCorrect;
			vector<double> expectedNumberOfStrokes;
			expectedNumberOfStrokes.push_back(numberTotal+2); //press Enter Right Away

			double tempProbability;
			//double oddsOfFirstWrong
			probabilityCorrect.push_back(1);
			for (int j = 1;j<=numberTyped;j++)
			{
				infile>>tempProbability;
				probabilityCorrect.push_back(tempProbability);
			}
			double CurrentCorrectProbability = 1;
			for (int numberOfBackspaces = numberTyped;numberOfBackspaces>=0;numberOfBackspaces--)
			{
				CurrentCorrectProbability = CurrentCorrectProbability*probabilityCorrect[numberTyped-numberOfBackspaces];
				double expectedCost = CurrentCorrectProbability*(numberOfBackspaces*2+1+numberTotal-numberTyped)+(1-CurrentCorrectProbability)*(numberOfBackspaces*2+1+numberTotal-numberTyped+numberTotal+1);
				expectedNumberOfStrokes.push_back(expectedCost);

			}

			
			//expectedNumberOfStrokes.push_back(
			outfile<<"Case #"<<i<<": "<<vectorMin(expectedNumberOfStrokes)<<endl;



		}
		return 0;

}