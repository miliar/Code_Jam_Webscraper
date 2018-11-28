#include <string>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <conio.h>
using namespace std;



unsigned short N;
unsigned _int64 L;
unsigned _int64 H;
unsigned _int64* OtherPlayerFrequencies;

unsigned _int64 Frequency;



void CalculateFrequency();



int main()
{
	ifstream inputFileReader("input.txt");
	ofstream outputFileWriter("output.txt");

	if (!inputFileReader || !outputFileWriter)
	{
		return 1;
	}

	string inputLine;
	stringstream inputLineReader;

	getline(inputFileReader, inputLine);
	inputLineReader << inputLine;

	int T;
	inputLineReader >> T;

	for (int testCaseIndex = 0; testCaseIndex < T; testCaseIndex++)
	{
		inputLineReader.clear();
		getline(inputFileReader, inputLine);
		inputLineReader << inputLine;

		inputLineReader >> N >> L >> H;

		OtherPlayerFrequencies = new unsigned _int64 [N];

		inputLineReader.clear();
		getline(inputFileReader, inputLine);
		inputLineReader << inputLine;

		for (unsigned short playerIndex = 0; playerIndex < N; playerIndex++)
		{
			inputLineReader >> OtherPlayerFrequencies[playerIndex];
		}

		CalculateFrequency();
		delete [] OtherPlayerFrequencies;

		outputFileWriter << "Case #" << (testCaseIndex + 1) << ": ";

		if (Frequency != 0)
		{
			outputFileWriter << Frequency;
		}
		else
		{
			outputFileWriter << "NO";
		}

		outputFileWriter << endl;
	}

	inputFileReader.close();
	outputFileWriter.close();

	return 0;
}



void CalculateFrequency()
{
	unsigned _int64 H2 = H + 1;

	for (Frequency = L; Frequency < H2; Frequency++)
	{
		bool takeNext = false;

		for (unsigned short playerIndex = 0; playerIndex < N; playerIndex++)
		{
			if (Frequency < OtherPlayerFrequencies[playerIndex])
			{
				if (OtherPlayerFrequencies[playerIndex] % Frequency != 0)
				{
					takeNext = true;
					break;
				}
			}
			else
			{
				if (Frequency % OtherPlayerFrequencies[playerIndex] != 0)
				{
					takeNext = true;
					break;
				}
			}
		}

		if (!takeNext)
		{
			return;
		}
	}

	Frequency = 0;
}