/*
 *  
 */

#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
using namespace std;

int main() {
		
	ifstream file;

	file.open("sample.txt");
	if(file.fail()) {
		cout << "ERROR OPENING";
		return 23;
	}
	ofstream outFile;
	outFile.open("output.txt");

	int amount;
	
	file >> amount;

	int snappers, clicks, power;
	bool on = false;
	string on2;

	for(int i = 0; i < amount; ++i) {
		file >> snappers >> clicks;

		power = pow(2, snappers);

		//if(clicks == 1 && snappers == 1) {
			//on = true;
		//}
		if(clicks % power == power - 1) {
		on = true;
		}
		else {
			on = false;
		}
		
		if(on)
			on2 = "ON";
		else
			on2 = "OFF";

		outFile << "Case #" << i+1 << ": " << on2 << endl;

	}

	return 0;
} 

