// SpeakingInTongues.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <windows.h>
#include <string>
#include <fstream>

using namespace std;

#define			InputFileName		"A-small-attempt0.in"
#define			OutputFileName		"A-small-attempt0.out"

int _tmain(int argc, _TCHAR* argv[])
{
	// Initializing input/output
	ifstream	inputFile(InputFileName);
	ofstream	outputFile(OutputFileName);

	string EngChar = "abcdefghijklmnopqrstuvwxyz";
	string GooglereseChar = "yhesocvxduiglbkrztnwjpfmaq";

	string InputLine = "";

	// Variables
	int			numberCases = 0;

	// Read input file
	inputFile >> numberCases;
	getline(inputFile, InputLine);
	for (int i = 0; i < numberCases; i++)
	{
		getline(inputFile, InputLine);
		for (int j = 0; j < InputLine.length(); j++)
		{
			if (InputLine[j] != ' ')
			{
				InputLine[j] = GooglereseChar[int(InputLine[j]) - 97];
			}
		}
		outputFile << "Case #" << i + 1 << ": " << InputLine << endl;
	}

	return 0;
}

