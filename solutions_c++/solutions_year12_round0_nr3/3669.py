#include <iostream>
#include <map>
#include <math.h>
#include <stdio.h>
#include <vector>
#include <string>
#include <sstream>

using namespace std;



int numberFromStringWithShift (string number, int dernierIndex) {
	string newNumber;
	for (int i=dernierIndex+1; i<number.size(); ++i) {
		newNumber.push_back(number[i]);
	}
	for (int i=0; i<=dernierIndex; ++i) {
		newNumber.push_back(number[i]);
	}
	//cout << "Number " << number << " shifted to " << newNumber << endl;
	return atoi(newNumber.c_str());
}

int main () {

	int cases;

	int A;
	int B;

	cin >> cases;

	for (int i = 0; i<cases; ++i){
		vector<int> errors (10001000, 0);
		cin >> A;
		cin >> B;

		

		int success = 0;

		for (int j = A; j<=B; ++j) {
			stringstream out;
			out.flush();
			out << j;

			string initialNumber = out.str();

			int dernierIndex = 0;

			

			while (dernierIndex < initialNumber.size()-1){
				int shiftedNumber = numberFromStringWithShift(initialNumber, dernierIndex);
				if (A<=shiftedNumber && shiftedNumber<=B && shiftedNumber!=j){
					//cout << "Sucess with shifted number:" << shiftedNumber << " from number:" << initialNumber << endl;
					
					int index;
					if (shiftedNumber>j){
						index = j * pow(10,initialNumber.size()) + shiftedNumber;
					} else {
						index = j + shiftedNumber * pow(10,initialNumber.size());
					}
					++errors[index];
					if (errors[index]>2){
						//cout << "Error on " << index << " with value " << errors[index] << " (from numbers " << shiftedNumber << " and " << initialNumber << endl;
					} else {
						++success;
					}
				}
				dernierIndex++;
			}
		}
		success = success/2;
		cout << "Case #" << (i+1) << ": " << success << endl;
		/*
		for (int j = A; j <= 22222222; ++j){
			if (errors[j]>2) {
				cout << "Error on " << j << " with value " << errors[j] << endl;
			}
		}
		*/
	}

}