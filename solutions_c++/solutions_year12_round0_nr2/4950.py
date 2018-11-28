#include<iostream>
#include<fstream>
#include<cmath>


using namespace std;

int main()
{
	ifstream input;
	//input.open("B-small-attempt4.in");
	input.open("B-large.in");
	//input.open("Temp.txt");
	//input.open("checkFile.txt");
	ofstream output;
	//output.open("checkFile.txt");
	output.open("outFile.txt");
	//output.open("Temp2.txt");

	int numCases;
	int numGooglers;
	int numSurprisingScores;
	int bestResult;
	int totalPoints;
	
	input >> numCases;
	//output << numCases;
	//output << endl;

	for(int i = 0; i < numCases; i++)
	{
		input >> numGooglers;
		//output << numGooglers << " ";
		input >> numSurprisingScores;
		//output << numSurprisingScores << " ";
		input >> bestResult;
		//output << bestResult << " ";

		int counter = 0;

		for(int j = 0; j < numGooglers; j++)
		{
			//int myArray[3];
			input >> totalPoints;
		//	output << totalPoints << " ";

			//We get the average rounded off to the nearest whole number.

			double tempAverage = totalPoints/3.0;

			if(int(tempAverage+0.5) >= int(tempAverage+1))
				tempAverage = int(tempAverage)+1;
			else
				tempAverage = int(tempAverage);

			//Check to see if any values match the 'best result'

			if(tempAverage >= bestResult)
			{
				counter++;
				continue;
			}

			if((totalPoints - (2*tempAverage)) >= bestResult)
			{
				counter++;
				continue;
			}

			if(tempAverage == (bestResult - 1) && (totalPoints > 0))
			{
				if(numSurprisingScores > 0)
				{
					numSurprisingScores--;
					counter++;
					continue;
				}

			}

		}

		output << "Case #" << i+1 << ": " << counter << endl;
		//output << endl;
	}

		return 0;
}