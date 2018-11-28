#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

bool isOn(int N, int K) {
	unsigned int min = pow(2., N);
	if (((K+1) % min) == 0) return true;
	else return false;
}

int main() {

	ofstream myFile;
	myFile.open ("out.out");
	ifstream in("A-large.in");

	int turns;
	in >> turns;

	for (int t = 1; t <= turns; t++) {
		unsigned int N;
		unsigned int K;
		in >> N;
		in >> K;
		
		cout << t << endl;
		myFile << "Case #" << t << ": ";
		if (isOn(N, K)) myFile << "ON";
		else myFile << "OFF";
		myFile << endl;
	}
}
