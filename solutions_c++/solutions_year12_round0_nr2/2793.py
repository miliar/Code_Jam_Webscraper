#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <cassert>

using namespace std;

int findBestSurprising(int score, int p) {
	if (score == 0) return 0;
	int mean = score/3;
	int leeWay = score%3;

	if (leeWay == 0 || leeWay == 1)
		return mean+1;
	return mean+2;
}

int findBestNonSurprising(int score, int p) {
	if (score == 0) return 0;
	int mean = score/3;
	int leeWay = score%3;

	if (leeWay == 0)
		return mean;
	return mean+1;
}

struct BestScores {
	int surprising;
	int nonSurprising;

	BestScores (int s, int ns): surprising(s), nonSurprising(ns) {}
};

bool compSurprisingScores (BestScores a,BestScores b) { return (a.surprising>b.surprising); }
bool compScores (BestScores a,BestScores b) { return (a.nonSurprising>b.nonSurprising); }

int findMaxBest(int N, int S, int p, const vector<int>& scores) {
	vector<BestScores> googlers;
	for (unsigned int i = 0; i < scores.size(); i++)	{
		googlers.push_back(BestScores(findBestSurprising(scores[i], p), findBestNonSurprising(scores[i], p)));
	}

	sort(googlers.begin(), googlers.end(), compScores);
	int count = 0;
	for (int i = 0; i < N; i++) {
		if (googlers[i].nonSurprising >= p) {
			count++;
		} else if (googlers[i].surprising >= p && S > 0) {
			count++; S--;
		} else {
			break;
		}
	}
	return count;
}

int main() {
	int n;
	cin >> n;

	string line;

	getline(cin, line);
	assert(line == "");

	for (int i = 1; i <= n; i++) {
		getline(cin, line);

		istringstream iss(line);
		int N, S, p;
		int score;
		iss >> N >> S >> p;
		vector<int> scores;
		for (int j = 0; j < N && iss >> score; j++) {
			scores.push_back(score);
		}

		cout << "Case #" << i << ": " << findMaxBest(N, S, p, scores) << endl;
	}
	return 0;
}
