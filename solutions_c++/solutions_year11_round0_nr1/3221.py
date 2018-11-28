#include <math.h>
#include <stdlib.h>

#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

#define MAX_TEST 100

class Robot {
	bool orange;
	unsigned int P[100], currentPos, nextButton, noOfPos;

public:

	Robot() {
		orange = true;
		currentPos = nextButton = 0;
		noOfPos = 0;
	}

	void SetColor(bool inOrange) {
		orange = inOrange;
	}

	void SetPosition(unsigned int position) {
		P[noOfPos] = position;
		noOfPos++;
	}

	bool ReachedNext() {
		if (currentPos == P[nextButton])
			return true;
		return false;
	}
	bool Done(){
		if (noOfPos == 0)
			return true;
		if (nextButton >= noOfPos)
			return true;
		return false;
	}

	bool Update(bool inOrange) {
		if (currentPos == P[nextButton]) {
			if (orange == inOrange){
				nextButton++;
				return true;
			}
		} else {
			if (currentPos < P[nextButton]) {
				currentPos++;
			} else {
				currentPos--;
			}
		}
		return false;
	}
};

int main() {
	unsigned int T, N[MAX_TEST], y[MAX_TEST], inPos;
	bool R[100][MAX_TEST];
	char item;
	bool nOrange[MAX_TEST];
	Robot robot[2][MAX_TEST];

	ifstream in("inputFile");
	ofstream out("outputFile");

	for (int i = 0; i < MAX_TEST; i++) {
		robot[0][i].SetColor(true);
		robot[1][i].SetColor(false);
	}

	in >> T;
	cout << T <<endl;

	for (unsigned int i = 0; i < T; i++) {

		in >> N[i];
		cout << N[i] << " " ;

		for (unsigned int j = 0; j < N[i]; j++) {
			in >> item;
			if (item=='O') {R[j][i] = true;} else{R[j][i] = false;}

			if (R[j][i]) {
				in >> inPos;
				robot[0][i].SetPosition(inPos-1);
			} else {
				in >> inPos;
				robot[1][i].SetPosition(inPos-1);
			}
			cout << item << " " << inPos << " ";
		}
		cout << endl;
	}

	in.close();

	cout << "----------------------------" << endl;

	for (unsigned int i = 0; i < T; i++) {
		y[i] = 0;
		unsigned int currentPoint = 0;
		nOrange[i] = R[0][i];
		while (!((robot[0][i].Done()) && (robot[1][i].Done()))) {
			if (nOrange[i]) {
				robot[1][i].Update(nOrange[i]);
				if (robot[0][i].Update(nOrange[i])) {
					currentPoint++;
					nOrange[i] = R[currentPoint][i];
				}
			} else {
				robot[0][i].Update(nOrange[i]);
				if (robot[1][i].Update(nOrange[i])) {
					currentPoint++;
					nOrange[i] = R[currentPoint][i];
				}
			}
			y[i]++;
		}
		out << "Case #" << i+1 << ": " << y[i] << endl;
	}

	out.close();

	cin >> T;
	return 0;
}
