//solution 1

#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <strstream>
#include <stdio.h>
#include <conio.h>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

int nTestCases;
int caseNumber;
int N;
char RobotColor[100];
int Button[100];

int updatepos(char c, int pos, int button, int time)
{
	//time will be >=1
	//just move pos, not press btn
	for (int i=button+1; i<N; i++)
	{
		if (RobotColor[i] == c)
		{
			int nextButton = Button[i];
			int dist = nextButton - pos;
			int newpos;
			if (time <= abs(dist))
				if (dist>=0)
					newpos = pos + time;
				else
					newpos = pos - time;
			else
				newpos = pos + dist;
			return newpos;
		}
	}
	//no change
	return pos;
}

int ProcessCase()
{
	int OPos = 1;
	int BPos = 1;
	int buttonPressed = 0;
	int timeElapsed = 0;
	char curRobot;
	int curButton;
	while (true)
	{
		curRobot = RobotColor[ buttonPressed ];
		curButton = Button[ buttonPressed ];
		if (curRobot == 'O')
		{
			int distance = curButton - OPos;
			int timeNeeded = abs(distance)+1;
			BPos = updatepos('B', BPos, buttonPressed, timeNeeded);
			OPos += distance;
			buttonPressed++;
			timeElapsed += timeNeeded;
		}
		else
		{
			int distance = curButton - BPos;
			int timeNeeded = abs(distance)+1;
			OPos = updatepos('O', OPos, buttonPressed, timeNeeded);
			BPos += distance;
			buttonPressed++;
			timeElapsed += timeNeeded;
		}
		if (buttonPressed == N)
			break;
	}
	return timeElapsed;
}



int main()
{
	string file1;
	string file2;
	file1 = "e:\\A-large.in";
	file2 = "e:\\z2.out";
	FILE * ps;
	freopen_s(&ps, file1.c_str(), "rt", stdin);
	// add comment for console output:
	freopen_s(&ps, file2.c_str(), "wt", stdout);
	scanf("%d", &nTestCases);
	char st[2];
	for (int caseNumber=1; caseNumber<=nTestCases; caseNumber++)
	{
		scanf("%d", &N);
		for (int i=0; i<N; i++)
		{
			scanf("%1s", st);
			RobotColor[i] = st[0];
			scanf("%d", &(Button[i]));
		}
		int result = ProcessCase();
		cout << "Case #" << caseNumber << ": ";
		cout << result << endl;
	}
	return 0;
}
