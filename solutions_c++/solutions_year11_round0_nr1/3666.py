#include <iostream>
#include <fstream>
using namespace std;


int main(){
	char robotCommand[100];
	int buttonCommand[100],blueCommand[100],orangeCommand[100];
	int nCase,iCase,nCommand,iCommand,nSeconds,iOrange,iBlue,blueLoc,orangeLoc,steps;
	ifstream infile("input.dat");
	ofstream outfile("output.dat");

	infile >> nCase;
	for(iCase = 0; iCase < nCase; iCase++){
		infile >> nCommand;
		iBlue = 0;
		iOrange = 0;
		for (iCommand=0; iCommand < nCommand; iCommand++){
			infile >> robotCommand[iCommand] >> buttonCommand[iCommand];
			if (robotCommand[iCommand] == 'B') {
				blueCommand[iBlue] = buttonCommand[iCommand];
				iBlue++;
			}
			else if (robotCommand[iCommand] == 'O') {
				orangeCommand[iOrange] = buttonCommand[iCommand];
				iOrange++;
			}
		}

		nSeconds = 0;
		iCommand = 0;
		iBlue = 0;
		iOrange = 0;
		blueLoc = 1;
		orangeLoc = 1;
		for(iCommand = 0; iCommand < nCommand; iCommand++){
			// Blue robot is next to act
			if (robotCommand[iCommand] == 'B') {
				nSeconds = nSeconds + abs(blueLoc - blueCommand[iBlue]) + 1;
				for (steps=0; steps < abs(blueLoc - blueCommand[iBlue]) +1; steps++){
					if (orangeLoc > orangeCommand[iOrange]){
						orangeLoc--;
					}
					else if (orangeLoc < orangeCommand[iOrange]){
						orangeLoc++;
					}
				}
				blueLoc = blueCommand[iBlue];
				iBlue++;
			}
			// Orange robot is next to act
			else if (robotCommand[iCommand] == 'O') {
				nSeconds = nSeconds + abs(orangeLoc - orangeCommand[iOrange]) + 1;
				for (steps=0; steps < abs(orangeLoc - orangeCommand[iOrange])+1 ; steps++){
					if (blueLoc > blueCommand[iBlue]){
						blueLoc--;
					}
					else if (blueLoc < blueCommand[iBlue]){
						blueLoc++;
					}
				}
				orangeLoc = orangeCommand[iOrange];
				iOrange++;
			}
		}
		outfile << "Case #" << iCase+1 << ": " << nSeconds <<endl;
		cout << "Case #" << iCase+1 << ": " << nSeconds <<endl;
	}

	system("pause");


	return 0;
}
