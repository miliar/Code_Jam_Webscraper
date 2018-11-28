#include <iostream>
#include <fstream>

using namespace std;
void print_suprise(int *suprise, int num) {
	for(int i = 0; i < num; ++i)
		cout << suprise[i] << " ";
}

int max_no_suprise(int score) {
	float avg = score/3.0;

	if(avg == score/3)
		return score/3;
	else
		return score/3 + 1;
}

int max_suprise(int score) {
	float avg = score/3.0;

	// Can't give an 11
	if(score > 28 || score < 2)
		return -1;

	if(avg == score/3)
		return score/3+1;
	if(avg - score/3 > .5)
		return score/3+2;
	else
		return score/3+1;
}

int calculate_max(int p, int *scores, int *sIndex, int num_scores) {
	int max = 0;
	for(int i = 0; i < num_scores; ++i) {
		if(sIndex[i] == 1) {
			if(max_suprise(scores[i]) >= p)
				max++;
		}
		else {
			if(max_no_suprise(scores[i]) >= p)
				max++;
		}
	}
	/*
	print_suprise(sIndex, num_scores);
	cout << " p: " << max << endl;
	*/

	return max;
}

int max_googlers_recurse(int p, int remaining_suprises, int *scores, int *canSuprise, int num_scores) {

	int max = 0;

	// Check whether a suprise can fit anywhere else
	/*
	bool foundSuprise = false;
	for(int i = 0; i < num_scores; ++i) {
		if(canSuprise[i] == 0) {
			foundSuprise = true;
			break;
		}
	}

	if(!foundSuprise)
		return calculate_max(p, scores, canSuprise, num_scores);
	*/
	if(remaining_suprises <= 0)
		return calculate_max(p, scores, canSuprise, num_scores);
	else if(remaining_suprises == 1) {
		for(int i = 0; i < num_scores; ++i) {
			if(canSuprise[i] == 0) {
				canSuprise[i] = 1;
				int t = calculate_max(p, scores, canSuprise, num_scores);
				if(t > max) {
					max = t;
				}
				canSuprise[i] = 0;
			}	
		}
	}
	else {
		for(int i = 0; i < num_scores; ++i) {
			if(canSuprise[i] == 0) {
				canSuprise[i] = 1;
				int t = max_googlers_recurse(p, remaining_suprises - 1, scores, canSuprise, num_scores);
				if(t > max) max = t;
				canSuprise[i] = 0;
			}
		}
	}
	return max;
}

// 0 - can suprise, not assigned
// 1 - assigned to suprise
// -1 - cannot suprise
int max_googlers(int p, int *scores, int num_scores, int num_suprise) {
	int *canSuprise = new int[num_scores];

	for(int i = 0; i < num_scores; ++i)
		canSuprise[i] = (max_suprise(scores[i]) == -1 ? -1 : 0);

	if(num_suprise == 0)
		return calculate_max(p, scores, canSuprise, num_scores);

	int max = 0;
	for(int i = 0; i < num_scores; ++i) {
		if(canSuprise[i] == 0) {
			canSuprise[i] = 1;
			int t = max_googlers_recurse(p, num_suprise - 1, scores, canSuprise, num_scores);
			if(t > max) max = t;
			canSuprise[i] = 0;
		}
	}

	delete canSuprise;

	return max;
}

int main(int argc, char **argv) {
	ifstream in(argv[1]);
	ofstream out(argv[2]);

	int num;
	in >> num;

	char s[256];

	// Finish the line
	in.getline(s,256);

	for(int i = 0; i < num; ++i) {
		int numG; in >> numG;
		int numS; in >> numS;
		int p; in >> p;

		int *scores = new int[numG];

		for(int j = 0; j < numG; ++j)
			in >> scores[j];

		// Finish the line
		in.getline(s,256);

		int max = max_googlers(p, scores, numG, numS);

		out << "Case #" << i + 1 << ": " << max << endl;
		//cout << "Case #" << i + 1 << ": " << max << endl;

		delete scores;
	}

	in.close();
	out.close();
}
