#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <fstream>
#include <cmath>
#include "Score.h"
//#include <ctime>

using namespace std;

const int N = 0;
const int S = 1;
const int P = 2;
const int TVALSTART = 3;
const int MAXN = 1000;
const int MAXT = 100;
const int MAXP = 10;
const int MAXSCORE = 30;

vector<int> tokenize(const string &s);
int maximize(vector<int> &values, int surprises, int goodScore);

int main(int argc, char *argv) {
	string infile = "D:/input.txt";
	string outfile = "D:/output.out";
	
	ifstream in;
	ofstream out;

	string s = "";
	int count = 0;
	int size = 0;
	vector<int> outputs;

	in.open(infile);
	while ((getline(in, s)) && (count <= size)) {
		if (count == 0) {
			size = atoi(s.c_str());
		}
		else {
			vector<int> tokens = tokenize(s);
			vector<int> tvalues;

			for (unsigned int i = 0; i < tokens.size(); i++) {
				cout << tokens[i] << " ";
			}
			cout << endl;

			if (((tokens[N] >= 1) && (tokens[N] <= MAXN))) {
				//cout << "test N" << endl;
				if ((tokens[S] >= 0) && (tokens[S] <= tokens[N])) {
					//cout << "test S" << endl;
					if ((tokens[P] >= 0) && (tokens[P] <= MAXP)) {
						//cout << "test P" << endl;
						if (((tokens.size() - 1) - 2) == tokens[N]) {
							//cout << "test" << endl;
							for (unsigned int i = TVALSTART; i < tokens.size(); i++) {
								tvalues.push_back(tokens[i]);
								cout << "TVALUE: " << tokens[i] << endl;
							}

							outputs.push_back(maximize(tvalues, tokens[S], tokens[P]));
						}
					}
				}
			}
		}

		count++;
	}

	//Output the results
	out.open("D:/output.out", ios::trunc);
	for (unsigned int i = 0; i < outputs.size(); i++) {
		out << "Case #" << i + 1 << ": " << outputs[i] << endl;
	}

	out.close();
	in.close();

	//cin >> s;

	return 0;
}

vector<int> tokenize(const string &s) {
	vector<int> tokens;
	int start = 0;
	int end = 0;
	int ptr = 0;

	while (ptr != string::npos) {
		ptr = s.find_first_of(" ", start);

		if (ptr == string::npos) {
			end = s.length();
		}
		else {
			end = ptr;
		}

		tokens.push_back(atoi(s.substr(start, end - start).c_str()));

		start = end + 1;
	}

	return tokens;
}

int maximize(vector<int> &values, int surprises, int goodScore) {
	vector<vector<Score>> scores;

	//Fill scores with the googlers
	for (unsigned int i = 0; i < values.size(); i++) {
		vector<Score> scorelist;
		scores.push_back(scorelist);
	}

	//Compute list of possible scores for each total value
	for (unsigned int i = 0; i < values.size(); i++) {
		for (int j1 = 0; j1 <= MAXP; j1++) {
			for (int j2 = 0; j2 <= MAXP; j2++) {
				for (int j3 = 0; j3 <= MAXP; j3++) {
					bool hasGoodNormalScore = false;
					bool hasGoodSurpriseScore = false;

					if ((j1 + j2 + j3) == values[i]) {
						if ((abs(j2 - j1) <= 2) && ((abs(j3 - j1) <= 2) && ((abs(j3 - j2) <= 2)))) {
							//Possible Score Candidate

							if ((abs(j2 - j1) == 2) || ((abs(j3 - j1) == 2) || ((abs(j3 - j2) == 2)))) {
								//Surprise Score

								if ((j1 >= goodScore) || (j2 >= goodScore) || (j3 >= goodScore)) {
									//Surprise Score Candidate
									hasGoodSurpriseScore = true;
								}
							}

							if (!hasGoodSurpriseScore) {
								if ((j1 >= goodScore) || (j2 >= goodScore) || (j3 >= goodScore)) {
									//Normal Good Score Candidate
									hasGoodNormalScore = true;
								}
							}
						}
					}

					if (hasGoodNormalScore) {
						Score score(j1, j2, j3);
						score.setBestScore(hasGoodNormalScore, Score::_BESTSCORE_NORMAL);
						scores[i].push_back(score);
					}
					else if (hasGoodSurpriseScore) {
						Score score(j1, j2, j3);
						score.setBestScore(hasGoodSurpriseScore, Score::_BESTSCORE_SURPRISE);
						scores[i].push_back(score);
					}
				}
			}
		}
	}

	//Go through piece by piece and compute maximum outcome
	int totalSurprises = 0;
	vector<int> googlersWithSurprisesOnly;
	vector<int> googlersWithNormalOnly;
	vector<int> googlersWithBoth;

	//First, find googlers with only surprise good scores
	for (unsigned int i = 0; i < values.size(); i++) {
		//Traverse Googler's score list
		int googlersurprises = 0;
		bool validCandidate = true;
		for (unsigned int j = 0; j < scores[i].size(); j++) {
			if (scores[i][j].hasBestScore(Score::_BESTSCORE_NORMAL)) {
				validCandidate = false;
			}
			else if (scores[i][j].hasBestScore(Score::_BESTSCORE_SURPRISE)) {
				googlersurprises++;
			}
		}

		if ((validCandidate) && (googlersurprises > 0)) {
			googlersWithSurprisesOnly.push_back(i);
		}
	}

	//Second, find googlers with only normal good scores
	for (unsigned int i = 0; i < values.size(); i++) {
		//Traverse Googler's score list
		int googlernormals = 0;
		bool validCandidate = true;
		for (unsigned int j = 0; j < scores[i].size(); j++) {
			if (scores[i][j].hasBestScore(Score::_BESTSCORE_NORMAL)) {
				googlernormals++;
			}
			else if (scores[i][j].hasBestScore(Score::_BESTSCORE_SURPRISE)) {
				validCandidate = false;
			}
		}

		if ((validCandidate) && (googlernormals > 0)) {
			googlersWithNormalOnly.push_back(i);
		}
	}

	//Third, find googlers with both normals and surprises
	for (unsigned int i = 0; i < values.size(); i++) {
		//Traverse Googler's score list
		int googlernormals = 0;
		int googlersurprises = 0;
		for (unsigned int j = 0; j < scores[i].size(); j++) {
			if (scores[i][j].hasBestScore(Score::_BESTSCORE_NORMAL)) {
				googlernormals++;
			}
			else if (scores[i][j].hasBestScore(Score::_BESTSCORE_SURPRISE)) {
				googlersurprises++;
			}
		}

		if ((googlersurprises > 0) && (googlernormals > 0)) {
			googlersWithBoth.push_back(i);
		}
	}

	//Finally, compute the maximum amount of outcomes
	int total = 0;
	int surpriseonly = googlersWithSurprisesOnly.size();
	int normalonly = googlersWithNormalOnly.size();
	int both = googlersWithBoth.size();
	
	//Add up to the maximum amount of surprises from the surprises only group
	if (surpriseonly >= surprises) {
		total += surprises;
	}
	else {
		total += surpriseonly;
	}

	//Add up the normals only
	total += normalonly;

	//Add up the both group
	total += both;

	return total;
}