#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

int cases, charsTyped, charsTotal;
double aD, minorMean;
vector <double> mistakeProbability;
vector <double> phases;
vector <int> strokes;
vector <string> results;
int cD; //currentDestination

struct aPhase
{
        int keyStrokes, currentIndex, nErase;
        double prob;
        int dest;
        vector <bool> chars;
};

bool checkWordIsCorrect (vector <bool> charsVeracity) {
	for (int i = 0; i<charsVeracity.size(); ++i){
		if (!charsVeracity[i]){
			return false;
		}
	}
	return true;
}

void performPhases (aPhase thePhase) {
	thePhase.currentIndex++;
	aPhase newPhase = thePhase;
	if (thePhase.currentIndex == 0){

		if (mistakeProbability[thePhase.currentIndex] != 0) {
		//WIN
		newPhase = thePhase;
		newPhase.prob = mistakeProbability[thePhase.currentIndex];
		newPhase.chars.push_back(true);
		newPhase.keyStrokes = 0;
		performPhases(newPhase);
		}

		if (mistakeProbability[thePhase.currentIndex] != 1) {
		//FAIL
		newPhase = thePhase;
		newPhase.prob = 1 - mistakeProbability[thePhase.currentIndex];
		newPhase.chars.push_back(false);
		newPhase.keyStrokes = 0;
		performPhases(newPhase);
		}

		
	} else {

		if (thePhase.currentIndex<charsTyped){
			//TYPE NEW CHARACTER
			if (mistakeProbability[thePhase.currentIndex] != 0) {
				//WIN
				newPhase = thePhase;
				newPhase.prob *= mistakeProbability[thePhase.currentIndex];
				newPhase.chars.push_back(true);

				performPhases(newPhase);
			}

			if (mistakeProbability[thePhase.currentIndex] != 1) {
				//FAIL
				newPhase = thePhase;
				newPhase.prob *= 1 - mistakeProbability[thePhase.currentIndex];
				newPhase.chars.push_back(false);

				performPhases(newPhase);
			}

		} else {
			//cout << "WORKING: nErase: " << thePhase.nErase << ", Prob: " << thePhase.prob << ", Keystrokes: " << thePhase.keyStrokes << endl;
			//ENDED TYPING FIRST CHARACTERS

			//TYPE REMAINING LETTERS

			if (thePhase.nErase>0){
				for (int i = 0; i<thePhase.nErase; ++i){
					thePhase.chars.pop_back();
					thePhase.keyStrokes += 2;
				}
				for (int i = 0; i<thePhase.nErase; ++i){
					thePhase.chars.push_back(true);
				}
			}

			for (int i = charsTyped; i<charsTotal; i++) {
				thePhase.keyStrokes++;
			}

			//ENTER KEY
			thePhase.keyStrokes++;

			if (!checkWordIsCorrect(thePhase.chars)) {
				for (int i = 0; i<charsTotal; i++) {
					thePhase.keyStrokes++;
				}
				//ENTER KEY
				thePhase.keyStrokes++;
			}
			//phases.push_back(thePhase.prob);
			//strokes.push_back(thePhase.keyStrokes);
			//cout << "nErase: " << thePhase.nErase << ", Prob: " << thePhase.prob << ", Keystrokes: " << thePhase.keyStrokes << endl;
			//cout << "FU" << endl;
			if (thePhase.nErase == -1) thePhase.nErase = charsTyped+1;
			phases[thePhase.nErase] += thePhase.prob * thePhase.keyStrokes;
		}
	}
}

int main () {

	cout.setf(ios::fixed);
 	cout.precision(6);

	cin>>cases;

	for (int i = 0; i<cases; i++) {
		mistakeProbability.clear();
		cin>>charsTyped>>charsTotal;
		for (int j=0; j<charsTyped; j++) {
			cin>>aD;
			mistakeProbability.push_back(aD);
		}
		phases.clear();
		strokes.clear();

		cD = 0;

		for (int j = 0; j<charsTyped+1; j++){
			//cout << "Phase " << j << endl;
			aPhase newPhase;
			newPhase.currentIndex = -1;
			newPhase.dest = cD;
			newPhase.nErase = j;
			phases.push_back(0);
			performPhases (newPhase);
			cD++;
			
		}

		//Straight away
		aPhase newPhase;
		newPhase.currentIndex = charsTyped;
		newPhase.keyStrokes = 1 + charsTyped;
		newPhase.dest = cD;
		newPhase.prob = 1;
		newPhase.nErase = -1;
		phases.push_back(0);
		performPhases (newPhase);
		cD++;
		

		minorMean = -1;
		for (int j = 0; j<=charsTyped+1; j++){
			if (minorMean == -1 || minorMean>phases[j]){
				//cout << "YAY" << endl;
				minorMean = phases[j];
			}
		}
		//results.push_back("Case#" + (i+1) + ": " << minorMean);
		cout << "Case #" << (i+1) << ": " << minorMean << endl;
	}
	/*
	for (int i = 0; i<results.size(); i++){
		cout << results[i] << endl;
	}
	*/
}