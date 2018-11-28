//============================================================================
// Name        : Q1.cpp
// Author      : Mike
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

using namespace std;

int main() {
	int state[30];

	ifstream file ("in");
	if (file.is_open()){
		long numCases;
		file >> numCases;
		int number;
		long snaps;
		//Run each CASE
		for (int thisCase = 1; thisCase <= numCases; thisCase++){

			//Clear state
			for (int n=0; n<30; n++){
					state[n]=0;
			}

			//Get New Values
			file >> number;
			file >> snaps;

			//Run each Snap
			for (int s =0; s < snaps; s++){
				int n=0;

				//Find units with power
				while ((state[n])&&(n<number)) {
					n++;
				}
				//Switch Units with power
				for (int i=n; i >= 0; i--){
					state[i] = !state[i];
				}
				//for (int l=0; l<30; l++){
				//	cout<< snap[l];
				//}
				//cout << endl;
			}

			//Find if Power at Light
			string final = "OFF";
			int m=0;
			while ((state[m])&&(m<number)) {
				m++;
			}
			if (((number-1)<=m)&&state[number-1]) final = "ON";
			cout <<"Case #"<< thisCase << ": " << final << endl;
		}
	} else {
		cout << "Error opening file";
	}
	file.close();
	return 0;
}
