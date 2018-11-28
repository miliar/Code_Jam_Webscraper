//Bot trust

#include <iostream>
#include <cmath>
using namespace std;

int main ()
{
	//Declare
	int i, j, N, command, previousCommandLength, buttons;
	int orangePosition, bluePosition;
	char robot, previousRobot;
	//Get number of inputs
	cin >> N;
	int numberSteps[N];
	//Iterate over inputs
	for (i = 1; i<=N; i++) {
		//Reset variables
		numberSteps[i] = 0;
		previousCommandLength = 0;
		previousRobot = ' ';
		orangePosition = 1;
		bluePosition = 1;
		
		//First command
		cin >> buttons;
		cin >> robot;
		cin >> command;
		previousRobot = robot;
		if (robot == 'O') {
			numberSteps[i]	= command - orangePosition + 1;
			orangePosition = command;
		} else {
			numberSteps[i] = command - bluePosition + 1;
			bluePosition = command;
		}
		previousCommandLength = numberSteps[i];
		
		//Read input
		for(j = 2;  j<=buttons; j++){
			cin >> robot;
			cin >> command;
			if (robot == previousRobot) {
				//command is for same robot
				if (robot == 'O') {
					numberSteps[i] = numberSteps[i] + abs(command - orangePosition) + 1;
					previousCommandLength = previousCommandLength + abs(command - orangePosition) + 1;
					orangePosition = command;
				} else {
					numberSteps[i] = numberSteps[i] + abs(command - bluePosition) + 1;
					previousCommandLength = previousCommandLength + abs(command - bluePosition) + 1;
					bluePosition = command;
				}
			} else {
				//command is for other robot
				if (robot == 'O'){
					if (abs(command - orangePosition) <= previousCommandLength) {
						//enough time to move robot
						numberSteps[i] = numberSteps[i] + 1;
						previousCommandLength = 1;
					} else {
						//not enough time to move robot
						numberSteps[i] = numberSteps[i] + abs(command - orangePosition) - previousCommandLength + 1;
						previousCommandLength = abs(command - orangePosition) - previousCommandLength + 1;
					}
					orangePosition = command;
				} else {
					if (abs(command - bluePosition) <= previousCommandLength) {
						//enough time to move robot
						numberSteps[i] = numberSteps[i] + 1;
						previousCommandLength = 1;
					} else {
						//not enough time to move robot
						numberSteps[i] = numberSteps[i] + abs(command - bluePosition) - previousCommandLength + 1;
						previousCommandLength = abs(command - bluePosition) - previousCommandLength + 1;
					}
					bluePosition = command;
				}
			}
			previousRobot = robot;
		}
	}
	for(i=1;i<=N;i++){
		cout << "Case #" << i << ": " << numberSteps[i] << endl;
	}
	return 0;
}
