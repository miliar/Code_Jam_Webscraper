#include <string>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <conio.h>
using namespace std;



int N;
char** Results;

double* Rpis;



void CalculateRpis();



int main()
{
	ifstream inputFileReader("input.txt");
	ofstream outputFileWriter("output.txt");

	if (!inputFileReader || !outputFileWriter)
	{
		return 1;
	}

	// Load number of test cases.

	string inputLine;
	stringstream inputLineReader;

	getline(inputFileReader, inputLine);
	inputLineReader << inputLine;

	int T;
	inputLineReader >> T;

	// For each testcase...

	for (int testCaseIndex = 0; testCaseIndex < T; testCaseIndex++)
	{
		// ...load number of teams,...

		inputLineReader.clear();
		getline(inputFileReader, inputLine);
		inputLineReader << inputLine;

		inputLineReader >> N;

		// ...results,

		Results = new char* [N];

		for (int teamIndex = 0; teamIndex < N; teamIndex++)
		{
			Results[teamIndex] = new char [N];

			inputLineReader.clear();
			getline(inputFileReader, inputLine);
			inputLineReader << inputLine;

			for (int teamIndex2 = 0; teamIndex2 < N; teamIndex2++)
			{
				inputLineReader >> Results[teamIndex][teamIndex2];
			}
		}

		// ...calculate RPIs and...

		Rpis = new double [N];
		CalculateRpis();

		for (int teamIndex = 0; teamIndex < N; teamIndex++)
		{
			delete [] Results[teamIndex];
		}

		delete [] Results;

		// ...save them to file.

		outputFileWriter << "Case #" << (testCaseIndex + 1) << ":" << endl;

		for (int teamIndex = 0; teamIndex < N; teamIndex++)
		{
			outputFileWriter << fixed;
			outputFileWriter << setprecision(12) << Rpis[teamIndex] << endl;
		}

		delete [] Rpis;
	}

	inputFileReader.close();
	outputFileWriter.close();

	return 0;
}



void CalculateRpis()
{
	double* WPs = new double [N];
	double* OWPs = new double [N];
	double* OOWPs = new double [N];

	for (int teamIndex = 0; teamIndex < N; teamIndex++)
	{
		// Calculate WPs.

		int wins = 0;
		int numberOfOpponents = 0;

		for (int teamIndex2 = 0; teamIndex2 < N; teamIndex2++)
		{
			if (teamIndex2 == teamIndex)
			{
				continue;
			}

			char result = Results[teamIndex][teamIndex2];

			if (result == '1')
			{
				wins++;
				numberOfOpponents++;
			}
			else if (result == '0')
			{
				numberOfOpponents++;
			}
		}

		WPs[teamIndex] = (double)wins / numberOfOpponents;

		// Calculate opponents' WP, excluding this team.

		double AccummulatedOpponentsWPsExcludingMe = 0;
		numberOfOpponents = 0;

		for (int teamIndex3 = 0; teamIndex3 < N; teamIndex3++)
		{
			if (teamIndex3 == teamIndex)
			{
				continue;
			}

			if (Results[teamIndex3][teamIndex] == '.')
			{
				continue;
			}

			numberOfOpponents++;

			int wins2 = 0;
			int numberOfOpponents2 = 0;

			for (int teamIndex2 = 0; teamIndex2 < N; teamIndex2++)
			{
				if (teamIndex2 == teamIndex)
				{
					continue;
				}

				char result = Results[teamIndex3][teamIndex2];

				if (result == '1')
				{
					wins2++;
					numberOfOpponents2++;
				}
				else if (result == '0')
				{
					numberOfOpponents2++;
				}
			}

			AccummulatedOpponentsWPsExcludingMe += (double)wins2 / numberOfOpponents2;
		}

		// Calculate OWP.

		OWPs[teamIndex] = AccummulatedOpponentsWPsExcludingMe / numberOfOpponents;
	}

	for (int teamIndex = 0; teamIndex < N; teamIndex++)
	{
		// Calculate OOWP.

		double AccummulatedOWPs = 0;
		int numberOfOpponents = 0;

		for (int teamIndex2 = 0; teamIndex2 < N; teamIndex2++)
		{
			if (teamIndex2 == teamIndex)
			{
				continue;
			}

			if (Results[teamIndex2][teamIndex] == '.')
			{
				continue;
			}

			AccummulatedOWPs += OWPs[teamIndex2];
			numberOfOpponents++;
		}

		OOWPs[teamIndex] = AccummulatedOWPs / numberOfOpponents;

		// Calculate RPI.

		Rpis[teamIndex] = 0.25 * WPs[teamIndex] + 0.5 * OWPs[teamIndex] + 0.25 * OOWPs[teamIndex];
	}

	// Clean up.

	delete [] WPs;
	delete [] OWPs;
	delete [] OOWPs;
}