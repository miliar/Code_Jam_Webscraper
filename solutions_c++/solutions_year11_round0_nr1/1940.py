#include <iostream>
#include <xutility>

using namespace std;

void SolveTest();

void main()
{
	int numTests;
	cin >> numTests;

	for(int i = 0; i < numTests; ++i)
	{
		SolveTest();
	}
}


void SolveTest() 
{
	static int testNum = 0;
	++testNum;

	int result = 0;
	int bluePos = 1;
	int blueSlack = 0;
	int orangePos = 1;
	int orangeSlack = 0;

	int numOperations;
	cin >> numOperations;
	for(int i = 0; i < numOperations; ++i)
	{
		char nextColour;
		cin >> nextColour;
		
		int nextPos;
		cin >> nextPos;

		if(nextColour == 'O')
		{
			//Get orange to position, using up slack first then otherwise using up cycles
			const int distance = abs(orangePos - nextPos);
			const int slackUsed = min(distance, orangeSlack);
			const int extraTimeRequired = distance - slackUsed + 1; //1 to hit the button
			orangeSlack = 0;
			orangePos = nextPos;

			result += extraTimeRequired;
			blueSlack += extraTimeRequired; //Extra time for other bot to move in any dir
		}
		else
		{
			//Get blue to position, using up slack first then otherwise using up cycles
			const int distance = abs(bluePos - nextPos);
			const int slackUsed = min(distance, blueSlack);
			const int extraTimeRequired = distance - slackUsed + 1; //1 to hit the button
			blueSlack = 0;
			bluePos = nextPos;

			result += extraTimeRequired;
			orangeSlack += extraTimeRequired;
		}
	}

	cout << "Case #" << testNum << ": " << result << endl;
}
