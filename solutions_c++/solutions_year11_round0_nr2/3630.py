// Problem 2.cpp
// Klairic
// 
#define INPUT_FILENAME			"C:\\_Coding Competitions\\Code Jam\\Qualifying Round 2011\\Problem 2\\B-large.in"
#define OUTPUT_FILENAME			"C:\\_Coding Competitions\\Code Jam\\Qualifying Round 2011\\Problem 2\\B-large.out"

#include "stdafx.h"
#include <string>
#include <iostream>
#include <assert.h>
#include <deque>

int _TestCount;
int _Tested;
std::string _CurrentTest;
std::string _Output;
FILE *_File;
int _FileSize;
int _ResultId;

char _Test[500001];
char _Line[500001];
char buffer[100];
int _TestPlace;


// Generic load/unload

void LoadTestData()
{
	_ResultId = 1;
	_TestPlace = 0;
	_File = fopen(INPUT_FILENAME, "r");
	_FileSize = fread(_Test, 1, 500000, _File);
	_Test[_FileSize] = 0;
}

void CloseTestData()
{
	fclose(_File);
	_File = fopen(OUTPUT_FILENAME, "w+b");
	assert(_File);
	fwrite(_Output.data(), 1, _Output.length(), _File);
	fclose(_File);
}
bool GetLine()
{
	char *place = strstr(&_Test[_TestPlace], "\n");
	if (place != nullptr)
	{
		int count = place - &_Test[_TestPlace];
		memcpy(_Line, &_Test[_TestPlace], count);
		_Line[count] = 0;
		_TestPlace += count + 1;
		return count > 0;
	}
	return false;
}

void GetTestCount()
{
	GetLine();
	_TestCount = atoi(_Line);
}
bool LoadTestInput()
{
	return GetLine();
}
void AdvanceLinePlace(int &place)
{
	char *found = strstr(&_Line[place], " ");
	if (found == nullptr)
		place = -1;
	else
		place = found - _Line + 1;
}
void OutputResult(int Result)
{
	_Output += "Case #";
	_Output += itoa(_ResultId, buffer, 10);
	_Output += ": ";
	_Output += itoa(Result, buffer, 10);
	_Output += "\r\n";
	_ResultId++;
}
void OutputResult(std::string &Result)
{
	_Output += "Case #";
	_Output += itoa(_ResultId, buffer, 10);
	_Output += ": ";
	_Output += Result;
	_Output += "\r\n";
	_ResultId++;
}

// Specific to this test

struct MagicCode
{
	char _Code[2];
	char _To;
};

std::deque<MagicCode> _Combine;
std::deque<MagicCode> _Opposed;

void ProcessTest()
{
	_Combine.clear();
	_Opposed.clear();
	int linePlace(0);

	int countCombine = atoi(&_Line[linePlace]);
	AdvanceLinePlace(linePlace);

	for (int i = 0; i < countCombine; i++)
	{
		MagicCode code;
		memcpy(&code, &_Line[linePlace], 3);
		AdvanceLinePlace(linePlace);
		_Combine.push_back(code);
	}

	int countOpposed = atoi(&_Line[linePlace]);
	AdvanceLinePlace(linePlace);

	for (int i = 0; i < countOpposed; i++)
	{
		MagicCode code;
		memcpy(&code, &_Line[linePlace], 2);
		AdvanceLinePlace(linePlace);
		_Opposed.push_back(code);
	}

	int countInput = atoi(&_Line[linePlace]);
	AdvanceLinePlace(linePlace);

	int countOutput(0);

	char input[100];
	char output[100];
	memcpy(input, &_Line[linePlace], countInput);

	for (int i = 0; i < countInput; i++)
	{
		output[countOutput] = input[i];
		countOutput++;

		bool check(true);
		while (check && countOutput >= 2)
		{
			// Check for combines
			check = false;
			for (int j = 0; j < _Combine.size(); j++)
			{
				if (_Combine[j]._Code[0] == output[countOutput - 2] && _Combine[j]._Code[1] == output[countOutput - 1] ||
					_Combine[j]._Code[1] == output[countOutput - 2] && _Combine[j]._Code[0] == output[countOutput - 1])
				{
					output[countOutput - 2] = _Combine[j]._To;
					countOutput--;
					check = true;
					break;
				}
			}
		}

		if (countOutput >= 2)
		{
			// Check for wipeouts
			bool wipe = false;
			for (int j = 0; j < _Opposed.size(); j++)
			{
				for (int k = 0; k < countOutput; k++)
				{
					if (output[k] == _Opposed[j]._Code[0])
					{
						for (int l = 0; l < countOutput; l++)
						{
							if (l != k && output[l] == _Opposed[j]._Code[1])
							{
								wipe = true;
								break;
							}
						}			
					}
					if (wipe)
						break;
				}			
				if (wipe)
					break;
			}
			if (wipe)
				countOutput = 0;
		}
	}
	output[countOutput] = 0;

	std::string result = "[";
	for (int i = 0; i < countOutput - 1; i++)
	{
		result += output[i];
		result += ", ";
	}
	if (countOutput > 0)
		result += output[countOutput - 1];
	result += "]";
	OutputResult(result);
}
int _tmain(int argc, _TCHAR* argv[])
{
	LoadTestData();
	GetTestCount();
	while (LoadTestInput())
		ProcessTest();
	CloseTestData();
	return 0;
}

