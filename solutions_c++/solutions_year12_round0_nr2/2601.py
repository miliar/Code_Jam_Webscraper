#include "googlers.h"
#include <iostream>
#include <vector>


using namespace std;

googlers::googlers(int tot)
{
	total = tot;
	tripletEqual = false;

	for (int i=0; i<3; i++)
		scores[i]=3;

	strong=false;

	fillTripletWithTotalScore();

	//printTriplet();
}

void googlers::fillTripletWithTotalScore() {

	int q = total / 3;
	int r = total % 3;

	if (r==0) {

		for (int i=0; i<3; i++)
			scores[i]=q;
		tripletEqual = true;
	} else {
		scores[0]=q; // min
		scores[1]=q+1; // max
		scores[2]=total-scores[0]-scores[1];
	}
}


void googlers::fillStrong(int minScore, int& strongGooglers) {

	int i = 0;

	while(!strong &&  i<3) {
		if(scores[i]>=minScore) {
			strong = true;
			strongGooglers++;
		}
		i++;
	}
}

void googlers::printTriplet() {
	for (int i=0; i<3; i++)
		cout << scores[i] << " ";
	cout << endl;
}

void googlers::printStrong() {
	if (strong)
		cout <<  "Strong" << endl;
	else
		cout << "Not Strong" << endl;
}

void googlers::applySurprising(int minScore, int& strongGooglers, int& refNbSuprising) {
	// case 1 : all number equal => +2 and see
	if(total==0)
		return;

	if (tripletEqual) {
		scores[0]--;
		scores[1]++;

		if(scores[1] >= minScore ) {

			strong=true;
			strongGooglers=strongGooglers+1;
			refNbSuprising=refNbSuprising-1;
		}
	} else if (scores[2] == scores[1]){ 	// case 2 : number not equal => +1 sur le max and see

		scores[2]--;
		scores[1]++;

		if(scores[1] >= minScore ) {

			strong=true;
			strongGooglers=strongGooglers+1;
			refNbSuprising=refNbSuprising-1;
		}
	}
}


int main() {

	int strongGooglers = 0;
	int nbGooglers, nbSuprising = 0;
	int minScore;
	int total_score;
	int T;
	cin >> T;

	vector<googlers> vgooglers;

	for (int t=1; t<=T; t++) {
		strongGooglers = 0;

		cin >> nbGooglers;
		cin >> nbSuprising;
		cin >> minScore;

		//cout << "minscore " << minScore <<  " nb Sup " << nbSuprising << endl;


		for (int j=0; j<nbGooglers; j++) {
			cin >> total_score;
			//cout << "total score " << total_score << " ";

			googlers g = googlers(total_score);
			g.fillStrong(minScore, strongGooglers);
			//g.printStrong();
			vgooglers.push_back(g);
		}

		vector<googlers>::iterator it;
		it=vgooglers.begin();
		while( it < vgooglers.end() && nbSuprising>0  ) {
			// try to find a surprising triplet for not strong googlers
			if (!(*it).getStrong()) {
				(*it).applySurprising(minScore, strongGooglers, nbSuprising);
			}
			//(*it).printTriplet();
			it++;

		}


		cout << "Case #"<< t << ": " << strongGooglers << endl;
		vgooglers.clear();
	}
}
