#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
using namespace std;
#include <conio.h>



enum BO
{
	B, O
};

struct RobotGoal
{
	BO WhichRobot;
	int Position;
};

/*
const int N = 4;
RobotGoal AllGoals[N] = 
{
	{ O, 2 }, { B, 1 }, { B, 2 }, { O, 4 }
};

const int N = 2;
RobotGoal AllGoals[N] = 
{
	{ B, 2 }, { B, 1 }
};
*/

int N;
RobotGoal* AllGoals;
int Seconds;



struct RobotState
{
	int Position;
	bool Pressed;
};



int FindNextGoalIndex(BO, int);
void MakeAMoveWithRobot(RobotState&, int, bool, int, bool&);
void CalculateSecondsToDoTheJob();



int main()
{
	ifstream inputFileReader("input.txt");
	ofstream outputFileWriter("output.txt");

	if (!inputFileReader || !outputFileWriter)
	{
		return 1;
	}

	// Load number of test cases.

	string inputLine;
	stringstream inputLineReader;

	getline(inputFileReader, inputLine);
	inputLineReader << inputLine;

	int T;
	inputLineReader >> T;

	// For each testcase...

	for (int testCaseIndex = 0; testCaseIndex < T; testCaseIndex++)
	{
		// ...load goals,...

		inputLineReader.clear();
		getline(inputFileReader, inputLine);
		inputLineReader << inputLine;

		inputLineReader >> N;

		AllGoals = new RobotGoal [N];

		for (int goalIndex = 0; goalIndex < N; goalIndex++)
		{
			char whichRobot;
			inputLineReader >> whichRobot >> AllGoals[goalIndex].Position;

			if (whichRobot == 'B')
			{
				AllGoals[goalIndex].WhichRobot = B;
			}
			else
			{
				AllGoals[goalIndex].WhichRobot = O;
			}
		}

		// ...calculate result and...

		CalculateSecondsToDoTheJob();

		delete [] AllGoals;

		// ...save it to file.
		outputFileWriter << "Case #" << (testCaseIndex + 1) << ": " << Seconds << endl;
	}

	inputFileReader.close();
	outputFileWriter.close();

	return 0;
}



void CalculateSecondsToDoTheJob()
{
	// Set initial state, goal and mark if robot has completed its job...

	// ...for B and...

	RobotState bState = { 1, false };
	bool bCompleted = false;

	int bGoalIndex = FindNextGoalIndex(B, 0);

	if (bGoalIndex == -1)
	{
		bCompleted = true;
	}

	// ...for O.

	RobotState oState = { 1, false };
	bool oCompleted = false;

	int oGoalIndex = FindNextGoalIndex(O, 0);

	if (oGoalIndex == -1)
	{
		oCompleted = true;
	}

	// Make moves with robots and update their goals until both complete their jobs.

	Seconds = 0;	// Count seconds on the way.

	while (!bCompleted || !oCompleted)
	{
		// Make moves.

		bool bAchievedGoal = false;
		
		if (!bCompleted)
		{
			MakeAMoveWithRobot(bState, bGoalIndex, oCompleted, oGoalIndex, bAchievedGoal);
		}

		bool oAchievedGoal = false;

		if (!oCompleted)
		{
			MakeAMoveWithRobot(oState, oGoalIndex, bCompleted, bGoalIndex, oAchievedGoal);
		}

		Seconds++;

		// Moves done. Robots may have achieved some goals, so we may have to set next goals.

		if (bAchievedGoal)
		{
			bGoalIndex = FindNextGoalIndex(B, bGoalIndex + 1);

			if (bGoalIndex == -1)
			{
				bCompleted = true;
			}
		}

		if (oAchievedGoal)
		{
			oGoalIndex = FindNextGoalIndex(O, oGoalIndex + 1);

			if (oGoalIndex == -1)
			{
				oCompleted = true;
			}
		}
	}
}



void MakeAMoveWithRobot(RobotState& robotState, int robotGoalIndex, bool companionRobotCompleted, int companionRobotGoalIndex,
	bool& robotAchievedGoal)
{
	RobotGoal robotGoal = AllGoals[robotGoalIndex];
	robotAchievedGoal = false;	// With this move robot may achieve its goal.

	if (robotState.Pressed)
	{
		robotState.Pressed = false;
	}
		
	if (robotState.Position != robotGoal.Position)
	{
		if (robotState.Position < robotGoal.Position)
		{
			robotState.Position++;
		}
		else
		{
			robotState.Position--;
		}
	}
	else if (!robotState.Pressed)
	{
		// Instead of pressing the button the robot may have to wait.
		if (companionRobotCompleted || robotGoalIndex < companionRobotGoalIndex)
		{
			robotState.Pressed = true;
			robotAchievedGoal = true;
		}
	}
}



/* Returns -1 when no next goals for the robot exist. */
int FindNextGoalIndex(BO whichRobot, int indexToSearchFrom)
{
	int index = indexToSearchFrom;

	while (index < N)
	{
		if (AllGoals[index].WhichRobot == whichRobot)
		{
			return index;
		}

		index++;
	}

	return -1;
}