// R1 - Problem 1.cpp : Defines the entry point for the console application.
// Klairic
// 
#define INPUT_FILENAME			"C:\\_Coding Competitions\\Code Jam\\Round 1 2011\\R1 - Problem 1\\A-large.in"
#define OUTPUT_FILENAME			"C:\\_Coding Competitions\\Code Jam\\Round 1 2011\\R1 - Problem 1\\A-large.out"

#include "stdafx.h"
#include <string>
#include <iostream>
#include <assert.h>
#include <deque>
#include <vector>
#include <algorithm>


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
void OutputData(double Result)
{
	_Output += _gcvt(Result, 10, buffer);
	_Output += "\r\n";
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


#define WIN		1
#define LOSS    0
#define NO		-1

struct Team
{
	int _Game[500];
	double _Games;
	double _Opp[500];
	double _OppPct;
	double _OppOpp;
	int _TeamNumber;
	Team()		
	{
		memset(this, 0, sizeof(Team));
	}
	double GetWinPct(int Exclude)
	{
		double wins(0);
		double games(0);
		for (int i = 0; i < _Games; i++)
		{
			if (i != Exclude)
			{
				switch (_Game[i])
				{
				case WIN:
					++wins;
				case LOSS:
					++games;
					break;
				}
			}
		}
		return wins / games;
	}
	double GetOpp()
	{
		return _OppPct;
	}
	double GetOppOpp()
	{
		return _OppOpp;
	}
	double GetRpi()
	{
		return (GetWinPct(_TeamNumber) * 0.25) + (GetOpp() * 0.5) + (GetOppOpp() * 0.25);
	}
};

Team *_Teams;


void ProcessTest()
{
	int count = atoi(_Line);

	_Teams = new Team[count];

	double wins(0);
	double losses(0);
	double games(0);
	for (int i = 0; i < count; i++)
	{
		GetLine();

		wins = 0;
		losses = 0;
		games = 0;

		for (int j = 0; j < count; j++)
		{
			switch (_Line[j])
			{
			case '1':
				_Teams[i]._Game[j] = WIN;
				games++;
				break;
			case '0':
				_Teams[i]._Game[j] = LOSS;
				games++;
				break;
			case '.':
				_Teams[i]._Game[j] = NO;
				break;
			}
		}
		_Teams[i]._Games = count;
		_Teams[i]._TeamNumber = i;
	}

	for (int i = 0; i < count; i++)
	{
		double opp(0);
		double oppCount(0);
		for (int j = 0; j < count; j++)
		{
			if (i != j)
			{
				if (_Teams[i]._Game[j] != NO)
				{
					_Teams[i]._Opp[j] = _Teams[j].GetWinPct(i);
					opp += _Teams[j].GetWinPct(i);
					oppCount++;
				}
			}
		}
		_Teams[i]._OppPct = opp / oppCount;
	}

	for (int i = 0; i < count; i++)
	{
		double opp(0);
		double oppCount(0);
		for (int j = 0; j < count; j++)
		{
			if (i != j)
			{
				if (_Teams[i]._Game[j] != NO)
				{
					opp += _Teams[j]._OppPct;
					oppCount++;
				}
			}
		}
		_Teams[i]._OppOpp = opp / oppCount;
	}

	OutputResult(std::string(""));
	for (int i = 0; i < count; i++)
	{
		OutputData(_Teams[i].GetRpi());
	}
	delete []_Teams;
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
