#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

int posO, posB, pressedO, pressedB;
vector<char> order;
vector<int> buttonsO;
vector<int> buttonsB;

bool processRobot(char robot,bool hasTurn)
{
	int *pos, *pressedCount;
	vector<int> *buttons;

	switch (robot)
	{
	case 'O':
		pressedCount = &pressedO;
		buttons = &buttonsO;
		pos = &posO;
		break;
	case 'B':
		pressedCount = &pressedB;
		buttons = &buttonsB;
		pos = &posB;
		break;
	}

	if (*pressedCount == buttons->size())
		return false;

	int targetPos = buttons->at(*pressedCount);
	//cout << robot << ": " << *pos << ' ' << targetPos << endl;

	if (hasTurn)
	{
		if (targetPos == *pos)
		{
			(*pressedCount)++;
			return true;
		}
	}

	if (targetPos < *pos)
		(*pos)--;

	if (targetPos > *pos)
		(*pos)++;

	return false;
}

string processCase(int test)
{
	int seconds = 0;
	bool buttonPressed = false;
	ostringstream retVal;

	for (int i=0;i<order.size();)
	{
		seconds++;
		char c = order[i];
		if (c == 'O')
		{
			bool b1 = processRobot('O',true);
			bool b2 = processRobot('B',false);
			buttonPressed = b1 || b2;
		}
		else
		{
			bool b1 = processRobot('O',false);
			bool b2 = processRobot('B',true);
			buttonPressed = b1 || b2;
		}
		if (buttonPressed)
			i++;
	}

	retVal << "Case #" << test << ": " << seconds;
	return  retVal.str();
}

int main()
{
	ifstream inputFile;
	inputFile.open("A-small.in");
	int T;
	vector<string> output;

	inputFile >> T;
	//cin >> T;

	for (int t=1;t<=T;t++)
	{
		posO		= 1;
		posB		= 1;
		pressedO	= 0;
		pressedB	= 0;

		order.clear();
		buttonsO.clear();
		buttonsB.clear();

		int N;
		inputFile >> N;
		//cin >> N;

		for (int n=1;n<=N;n++)
		{
			char R;
			int pos;
			inputFile >> R >> pos;
			//cin >> R >> pos;

			order.push_back(R);
			switch (R)
			{
			case 'O':
				buttonsO.push_back(pos);
				break;
			case 'B':
				buttonsB.push_back(pos);
				break;
			}
		}
		output.push_back(processCase(t));
	}

	inputFile.close();
	ofstream outputFile;
	outputFile.open("A-large.out");
	for (int i=0;i<output.size();++i)
		outputFile << output.at(i) << endl;

	outputFile.close();
}
