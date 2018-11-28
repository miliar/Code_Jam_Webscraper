// C. Theme Park Solution
// Microsoft Visual Studio 2008 C++

//Includes
#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <cstring>

//Namespace
using namespace std;

//Functions
//

int main()
{
	//Req vars
	int T = 0; // Test cases
	int R = 0; // Rides per day
	int K = 0; // Max people per ride
	int N = 0; // Number of groups
	int totalEarnings = 0; // Total roller coaster earnings
	int rate = 1; // Rate per ride
	int totalMembers = 0;

	//Other vars
	int temp = 0;
	int inRide = 0;
	bool rideFull = false;
	int pointer = 0;
	totalEarnings = 0;
	
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
		
		while (!inFile.eof())
		{
			inFile >> T;

			for (int t = 0; t < T; t++)
			{
				inFile >> R;
				inFile >> K;
				inFile >> N;

				int *groups = new int[N];

				for (int i = 0; i < N; i++)
				{
					inFile >> groups[i];
					totalMembers += groups[i];
				}

				if (totalMembers > K)
				{

					for (int r = 0; r < R; r++)
					{
						cout << " Run : " << r+1;
						
						do
						{
							if ((inRide+groups[pointer]) < K)
							{
								inRide = inRide + groups[pointer];
								rideFull = false;
							}
							else
							{
								if ((inRide+groups[pointer]) == K)
								{
									inRide = inRide + groups[pointer];
									pointer++;
									rideFull = true;
								}
								else
								{
									if (inRide+groups[pointer] > K)
									{
										rideFull = true;
									}
								}
							}
							
							if (pointer < N && rideFull != true)
							{
								pointer++;
							}
							else
							{
								rideFull = true;
								totalEarnings += rate*inRide;
							}

						} while (rideFull != true);

						cout << " Total so far: " << totalEarnings << endl;

						for (int x = 0; x < pointer; x++)
						{
							temp = groups[0];
							
							for (int z = 0; z < (N-1); z++)
							{
								groups[z] = groups[z+1];
								cout << groups[z];
							}
							
							groups[N-1] = temp;	
							cout << groups[N-1] << endl;
						}
						pointer = 0;
						inRide = 0;
					}
				}
				else
				{
					totalEarnings = totalMembers*R;
				}

				delete [] groups;

				outFile << "Case #" << (t+1) << ": " << totalEarnings << endl;
				temp = 0;
				inRide = 0;
				rideFull = false;
				pointer = 0;
				totalEarnings = 0;
				totalMembers = 0;
			}

			inFile >> T;
		}
		
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
