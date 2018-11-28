// google_code_jam_BotTrust.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <math.h>
#include <iostream>
using namespace std;

int numPress;
char color[105];
int button[105];
int step[105];

int orangeLoc, blueLoc;
int blueTimeGain, orangeTimeGain;
int orangeStep, blueStep;
char curColor;

void calculate(int);
void sameColor(char curColor, int i);
void diffColor(char curColor, int i);
int _tmain(int argc, _TCHAR* argv[])
{
	int numTestCase;

	cin >> numTestCase;
	for (int i = 1; i <= numTestCase; ++i){
		cin >> numPress;
		for (int j = 1; j <= numPress; ++j){
			cin >> color[j];
			cin >> button[j];
		}
		calculate(i);
	}
	return 0;
}

void calculate(int caseNum){
	orangeLoc = 1;
	blueLoc = 1;
	blueTimeGain = 0, orangeTimeGain = 0;

	int min = 0;  //minimun number of seconds

	curColor = color[1];
	for (int i = 1; i <= numPress; ++i){
		if(curColor == color[i]){
			sameColor(curColor, i);
		}else{
			curColor = color[i];
			diffColor(curColor, i);
		}
	}

	for (int x = 1; x <= numPress; ++x){
		min = min + step[x];
	}
	min = min + numPress;
	cout << "Case #" << caseNum << ": " << min << endl;
}

void sameColor(char curColor, int i){
	switch(curColor){
	case 'O':
		step[i] = abs(button[i] - orangeLoc);
		blueTimeGain = blueTimeGain + step[i] + 1;
		orangeLoc = button[i];
		break;
	case 'B':
		step[i] = abs(button[i] - blueLoc);
		orangeTimeGain = orangeTimeGain + step[i] + 1;
		blueLoc = button[i];
		break;
	}
}

void diffColor(char curColor, int i){
	switch(curColor){
	case 'O':
		orangeStep = abs(orangeLoc - button[i]);
		if (orangeStep > orangeTimeGain){
			step[i] = orangeStep - orangeTimeGain;
			blueTimeGain = step[i] + 1;
		}else{
			step[i] = 0;
			blueTimeGain = 1;
		}
		orangeLoc = button[i];
		break;
	case 'B':
		blueStep = abs(blueLoc - button[i]);
		if (blueStep > blueTimeGain){
			step[i] = blueStep - blueTimeGain;
			orangeTimeGain = step[i] + 1;
		}else{
			step[i] = 0;
			orangeTimeGain = 1;
		}
		blueLoc = button[i];
		break;
	}
}