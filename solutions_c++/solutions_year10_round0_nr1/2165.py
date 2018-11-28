//============================================================================
// Name        : BitTest.cpp
// Author      : lala
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <math.h>

using namespace std;

int main() {
	long long problems;
	long long snappers;
	long long snapps;
	cin >> problems;
	for(long long i = 0; i < problems; i++){
		cin >> snappers;
		cin >> snapps;
		long long power = 1 << snappers;
		if(snapps%power==power-1)
			cout << "Case #" << i+1 <<": "<<"ON"<< endl;
		else
			cout << "Case #" << i+1 <<": "<<"OFF"<< endl;
	}
	return 0;
}
