#include <iostream>
#include <cstring>
#include <sstream>
#include <vector>
#include <fstream>
using namespace std;
#define firstHalf 1
#define secondHalf 2
#define _vec (*vec)[i]

long long i = 0;

class SnapperClass {
public:
	bool hasPower;
	bool isOn;
	
	SnapperClass() {
		hasPower = false;
		isOn = false;
	}
};

void reset(vector<SnapperClass> *vec) {
	long long sizeOfVec = vec->size();
	for (long long i = 0; i < sizeOfVec; i++) {
		_vec.hasPower = false;
		_vec.isOn = false;
		
	}
	(*vec)[0].hasPower = true;
}

void snap(vector<SnapperClass> *vec);

long long stringToInt (string toInt) {
	istringstream toIntSS(toInt);
	long long newInt;
	toIntSS >> newInt;
	return newInt;
}

void turnOffPower(vector<SnapperClass> *vec) {
	if (i >= (*vec).size()) {
		//cout << "ending turnoffpower because of size" << endl;
		i = 0;
		return;
	}
	
	_vec.hasPower = false; //Turn off the power until the end
	//cout << "turned off power of " << i << endl;
	
	i++;
	
	turnOffPower(vec); //Recurse
}

void givePower(vector<SnapperClass> *vec) {
	if (i >= (*vec).size()) {
		//cout << "ending give power because of size" << endl;
		i = 0;
		return;
	}
	
	if (i == 0) {
		if (_vec.isOn) {
			//cout << "giving power because i = 0 and it is on" << endl;
			i++;
			givePower(vec);
		}
		else {
			//cout << "turning off power because 1 is off" << endl;
			i++;
			turnOffPower(vec);
		}
	}
	
	else if (i > 0) {
		if ((*vec)[i-1].isOn && (*vec)[i-1].hasPower) { //If the last one is on and has power, give this one power
			_vec.hasPower = true;
			//cout << "giving power because on and powered before it to " << i << endl;
			i++;
			givePower(vec);
		}
		else if (!(*vec)[i-1].isOn or !(*vec)[i-1].hasPower) { //If the last one is not on or or doesn't have power, don't give power
			//cout << "turning off power because " << (i-1) << " is not on or has no power " << endl;
			i++;
			turnOffPower(vec);
		}
	}
}

long long parseStringFunction (long long half, string wholeNumber) {
	string parsedString = wholeNumber;
	long i = 0;
	long size = wholeNumber.size();
	long long parsedNumber;
	long long sizeToDelete;
	
	//Find the space
	for (; i < size; i++) {
		if (wholeNumber[i] == ' ') {
			break;
		}
	}
	
	if (half == firstHalf) {
		sizeToDelete = size - i;
		parsedString.erase(i, sizeToDelete);
	}
	
	if (half == secondHalf) {
		sizeToDelete = (size - (size - i)) + 1;
		parsedString.erase(0, sizeToDelete);
	}
	
	//Converting to long long
	istringstream ss(parsedString);
	ss >> parsedNumber;
	
	return parsedNumber;
}

int main () {
	
	fstream myfile;
	fstream writeFile;
	writeFile.open("output.txt");
	myfile.open("input.in");
	if (myfile.is_open() && writeFile.is_open())
	{
		while (! myfile.eof() )
		{
			long long n, k, t;
			
			string testCases;
			
			getline (myfile,testCases);
			
			t = stringToInt(testCases);
			
			for (long long counter = 1; counter <= t; counter++) {
				string input;
				getline(myfile, input);
				n = parseStringFunction(firstHalf, input);
				k = parseStringFunction(secondHalf, input);
				
				//cout << n << endl << k << endl;
				
				vector<SnapperClass> snappers (n);
				snappers[0].hasPower = true;
				
				for (long long snapCounter = 1; snapCounter <= k; snapCounter++) {
					snap(&snappers);
				}
				
				if (snappers[n-1].isOn && snappers[n-1].hasPower) {
					writeFile << "Case #" << counter << ": ON\n";
				}
				else {
					writeFile << "Case #" << counter << ": OFF\n";
				}
				reset(&snappers);
			}
		}
		myfile.close();
		writeFile.close();
	}
	
	else cout << "Unable to open file"; 
	
	
    return 0;
}

//1 (Click) Everything with power hears the click
//2 On and off swap
//3 Power check

void snap(vector<SnapperClass> *vec) {
	long long sizeOfVec = vec->size();
	
	for (long long i = 0 ; i < sizeOfVec; i++) {
		if (_vec.hasPower) { //If it has power, flip on/off
			_vec.isOn = !_vec.isOn;
		}
	}
	givePower(vec);
	
	for (long long i = 0 ; i < sizeOfVec; i++) {
		//cout << i << "  ON/OFF:  " << _vec.isOn << endl;
		//cout << i << "  POWER:  " << _vec.hasPower << endl;
	}
	//cout << "End Snap" << endl;
}