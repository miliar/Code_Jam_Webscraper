/* ========================================================================== //
//                        --= GOOGLE CODE JAM 2011 =--                        //
// ========================================================================== //
//                                 BOT TRUST                                  //
// ========================================================================== //

	Qualification Round, Problem A.

// ========================================================================== */

// ========================================================================== //

//
#include <iostream>
#include <fstream>
using namespace std;
// ========================================================================== //


struct BotState{
	int position;	// Current position in the hallway
	int target;		// Target position in the hallway, -1 for find new target
	int index;		// Index in task array
};


int main(){

	ifstream fileIn;
	fileIn.open("A-large.in");

	ofstream fileOut;
	fileOut.open("A-large.out");

	int testCount = 0;
	fileIn >> testCount;

	for (int i = 0; i < testCount; i++){

		// Set up temp vars
		BotState botO = {1,-1, -1};
		BotState botB = {1,-1, -1};

		// Read button count
		int buttonCount = 0;
		fileIn >> buttonCount;

		// Read all and allocate task list
		int *taskList = new int[buttonCount];

		// Read button list
		for (int j = 0; j < buttonCount; j++){
			// Read robot name
			char botName = '_';
			fileIn >> botName;

			// Read target
			int buttonIndex = 1;
			fileIn >> buttonIndex;

			// Use negative value for O, positive for B
			if (botName == 'O'){
				if (botO.target < 0){
					botO.target = buttonIndex;
					botO.index = j;
				}
				buttonIndex = -buttonIndex;
			}
			else{
				if (botB.target < 0){
					botB.target = buttonIndex;
					botB.index = j;
				}
			}

			// Add task to list
			taskList[j] = buttonIndex;
		}
		// Put bot 0 on negative
		botO.target = -abs(botO.target);
		botO.position = -abs(botO.position);
		if (botO.index < 0)
			botO.index = buttonCount;
		if (botB.index < 0)
			botB.index = buttonCount;

		// Count moves
		int moveCount = 0;
		BotState *currentBot = NULL;
		BotState *otherBot = NULL;
		// Loop until neither bot has a target
		for (int j = 0; j < buttonCount; j++){
			// Set new task
			if (NULL == currentBot){
				currentBot = (botO.index < botB.index)? &botO:&botB;
				otherBot = (currentBot == &botO)? &botB:&botO;
			}
			// Find distance to next button
			int buttonDistance = abs(currentBot->position - currentBot->target);
			// Move other up to distance+1 and find new target
			int moveDistance = buttonDistance + 1; // 1 for press move
			moveCount += moveDistance;

			int maxOtherMove = abs(otherBot->position - otherBot->target);
			int otherMove = min(maxOtherMove, moveDistance);
			// Set direction
			if (otherBot->target < otherBot->position)
				otherMove = -otherMove;
			// Move other
			otherBot->position += otherMove;
			currentBot->position = currentBot->target;
			// Find new target for current and set to NULL
			for (int k = currentBot->index+1; k < buttonCount; k++){
				// Multiply t
				if (taskList[k] * currentBot->position > 0){
					currentBot->index = k;
					currentBot->target = taskList[k];
					break;
				}
				currentBot->index = buttonCount;
			}
			currentBot = NULL;

		}
		cout << "Case #" << (i+1) << ": " << moveCount << "\n";
		fileOut << "Case #" << (i+1) << ": " << moveCount << "\n";

	}

	return 1;
}
