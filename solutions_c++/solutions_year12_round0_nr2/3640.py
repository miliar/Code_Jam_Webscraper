#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

int main () {

	int cases;
	cin >> cases;

	for (int i = 0; i<cases; ++i){
		int nGooglers;
		cin >> nGooglers;

		int surprises;
		cin >> surprises;

		int scoreMinimum;
		cin >> scoreMinimum;

		vector<int> totalScores;
		//vector<int> majScore;

		int newScore;

		for (int j = 0; j<nGooglers; ++j) {
			cin >> newScore;
			totalScores.push_back(newScore);
		}

		/*
		cout << "Case #" << (i+1) <<": Googlers->" << nGooglers << ", surprises->" << surprises << ", scoreMinimum->" << scoreMinimum << ", scores->{";

		for (int j = 0; j<nGooglers; ++j) {
			if (j!=0){
				cout << ", ";
			}
			cout << totalScores[j];
		}
		cout << "}" << endl;
		*/

		int successNumber = 0;

		for (int j = 0; j<nGooglers; ++j){
			int totalGooglerScore = totalScores[j];
			int majScore = totalGooglerScore/3;
			if (totalGooglerScore%3 > 0){
				++majScore;
			}
			//cout << "Case" << (i+1) << " Googler" << (j+1) << " majScore:" << majScore << endl;
			if (majScore >= scoreMinimum){
				successNumber +=1;
			} else if ((surprises>0) && (majScore+1 == scoreMinimum) && ((totalGooglerScore%3 == 0 && totalGooglerScore/3 != 0) || (totalGooglerScore%3 == 2))) {
				surprises-=1;
				successNumber +=1;
			}
			//cout << "success:" << successNumber << endl;
			//majScore[j] = majGooglerScore;
		}
		cout << "Case #" << (i+1) << ": " << successNumber << endl;
	}

}