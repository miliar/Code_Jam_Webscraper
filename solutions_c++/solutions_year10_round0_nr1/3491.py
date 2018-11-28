// Solution to A. Snapper Chain
// Microsoft Visual Studio 2008 C++

//Includes
#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <cmath>

//Namespace
using namespace std;

//Functions
//

int main()
{
	//Req vars
	int T = 0; // number of terms
	int N = 0; // number of snappers
	int K = 0; // number of clicks
	int clicksForOn[30] = {0};
	bool stateIsOn = false;

	//Populate clicksForOn array
	clicksForOn[0] = 1;
	for (int x = 1; x < 30; x++)
	{
		clicksForOn[x] = (static_cast<int>(pow(2.0, (x+1))));
		//clicksForOn[x] = (static_cast<int>(pow(2.0, (x+1))))-1;
		//cout << (x+1) << " " << clicksForOn[x] << endl;
	}
	
	char inFileString[] = "C:\\Datasets\\Data.in";
	char outFileString[] = "C:\\Datasets\\Data.out";
	
	ifstream inFile;
	ofstream outFile;
	
	inFile.open(inFileString, ios::in);
	outFile.open(outFileString, ios::out);
	
	cout << "Openning specified files ..." << endl;
	
	if (inFile.is_open() && outFile.is_open())
	{
		cout << "Performing calculations ..." << endl;
		
		do
		{
			inFile >> T;

			for (int t = 0; t < T; t++)
			{
				inFile >> N;
				inFile >> K;				

				//cout << N << " " << K << endl;

				//K%clicksForOn[N-1] == 1 || 
				if ((K != 0) && ((((K/2)*2) != K) && (K%clicksForOn[N-1] == clicksForOn[N-1]-1)))
				{
					stateIsOn = true;
				}
				else
				{
					stateIsOn = false;
				}

				outFile << "Case #" << (t+1) << ": ";
				if (stateIsOn == true)
				{
					outFile << "ON" << endl;
				}
				else
				{
					outFile << "OFF" << endl;
				}
			}

			inFile >> T;
		} while (!inFile.eof());
		
		cout << "Calculations complete ..." << endl;

		inFile.close();
		outFile.close();
	}
	else
	{
		cout << "Could not open specified files" << endl;
	}	
	
	return 0;
}