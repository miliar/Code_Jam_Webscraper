// Problem 1.cpp
// Klairic
// 
#define INPUT_FILENAME			"C:\\_Coding Competitions\\Code Jam\\Qualifying Round 2011\\Problem 1\\A-large.in"
#define OUTPUT_FILENAME			"C:\\_Coding Competitions\\Code Jam\\Qualifying Round 2011\\Problem 1\\A-large.out"

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







// Specific to this test

struct ButtonPress 
{
	bool _Orange;
	int _Place;
};
std::deque<ButtonPress> _Sequence;
std::deque<ButtonPress> _SequenceBlue;
std::deque<ButtonPress> _SequenceOrange;
int _BotPlaceOrange;
int _BotPlaceBlue;

void LoadBotTest()
{
	int linePlace(0);
	int count = atoi(_Line);
	AdvanceLinePlace(linePlace);

	ButtonPress current;

	for (int i = 0; i < count; i++)
	{
		switch (_Line[linePlace])
		{
		case 'o':
		case 'O':
			current._Orange = true;
			break;
		case 'b':
		case 'B':
			current._Orange = false;
			break;
		default:
			assert(false);
			break;
		}
		AdvanceLinePlace(linePlace);
		current._Place = atoi(&_Line[linePlace]);

		_Sequence.push_back(current);
		if (current._Orange)
			_SequenceOrange.push_back(current);
		else
			_SequenceBlue.push_back(current);
		AdvanceLinePlace(linePlace);
	}
}


bool TryToPushButton(int &BotPlace, std::deque<ButtonPress> &Sequence)
{
	if (BotPlace == Sequence[0]._Place)
	{
		_Sequence.pop_front();
		Sequence.pop_front();
		return true;
	}
	return false;
}
bool NextMove(int &BotPlace, std::deque<ButtonPress> &Sequence, bool Orange, bool CanPush)
{
	// Do nothing if we're done
	// Push a button if we're in the right spot
	// Move if we can't push
	if (Sequence.empty())
		return true;

	bool tryToPush = _Sequence[0]._Orange == Orange;
	if (tryToPush && CanPush)
	{
		if (TryToPushButton(BotPlace, Sequence))
			return false;
	}

	if (BotPlace > Sequence[0]._Place)
		BotPlace--;
	else if (BotPlace < Sequence[0]._Place)
		BotPlace++;
	return true;
}

void ProcessTest()
{
	LoadBotTest();

	_BotPlaceOrange = 1;
	_BotPlaceBlue = 1;
	int time(0);

	while (!_Sequence.empty())
	{
		bool canPush = NextMove(_BotPlaceOrange, _SequenceOrange, true, true);
		NextMove(_BotPlaceBlue, _SequenceBlue, false, canPush);
		time++;
	}
	OutputResult(time);
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

