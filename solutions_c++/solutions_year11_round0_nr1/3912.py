#include <cstdio>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <sstream>
using namespace std;

int abs(int input) {
	if(input < 0) 
		return (-1) * input; 
	else
		return input;
}

int botTrust(char* command)
{
	stringstream ss;
	ss << command;

	int N;
	ss >> N;

	int i, curPosition, run, moresteps;
	int* steps = new int[N + 1];
	int prevPosition[256];  //saving old position
	int prevLoop [256];
	
	char robot, prevRobot;  

	//Initialization
	for (i = 0; i < N + 1; i++)
		steps[i] = 0;

	for(i = 0; i < 256; i++) {
		prevPosition[i] = 1;  //start from posistion 0
		prevLoop[i] = 0;
	}

	run = 0;
	prevRobot = '?';

	for(int i = 0; i < N; i++)
	{
		ss >> robot;
		ss >> curPosition;
        if((prevRobot == robot)  || (run == 0))
		{
			++run;
			steps[run] = abs(curPosition - prevPosition[robot]) + 1;
		}
		else
		{
			++run;
			moresteps = 0;
			for (int k = prevLoop[robot] + 1; k <= run -1; k++)
				moresteps += steps[k];

			moresteps = abs(curPosition - prevPosition[robot]) - moresteps;

			if(moresteps < 0)
				steps[run] = 1;
			else 
				steps[run] += (1 + moresteps);
		}

		prevRobot = robot;
		prevPosition[robot] = curPosition;
		prevLoop[robot] = run;
	}


	int Result = 0;
	for(i = 1; i <= run; i++)
		Result += steps[i];

	delete[] steps;
	return Result;
}

int main(int argc, char *argv[]) 
{
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);

	char command[4096];
	int i = 1;

	gets(command);
	while (gets(command))
	{
		int iResult = botTrust(command);
		printf("Case #%d: %d\n", i++, iResult);
	}
		
	




}