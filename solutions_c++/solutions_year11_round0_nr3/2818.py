#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int getValue (const vector<int>& vec1, const vector<int>& vec2) {
	if (vec1.empty() || vec2.empty()) return 0; 

	int value1 = 0, value2 = 0; 
	int realValue1 = 0, realValue2 = 0; 
	for (int i=0; i<vec1.size(); i++) {
		value1 ^= vec1[i];
		realValue1 += vec1[i];
	}
	for (int i=0; i<vec2.size(); i++) {
		value2 ^= vec2[i];
		realValue2 += vec2[i];
	}

	if (value1 != value2) return 0; 
	return realValue1 > realValue2 ? realValue1 : realValue2;
}

int dividePile (const vector<int>& vec1, const vector<int>& vec2, int maxBound) {
	int maxValue = getValue(vec1, vec2);
	if (vec1.size() < maxBound) {
		// go on dividing
		vector<int> newVec1(vec1), newVec2(vec2);
		for (int i=0; i<newVec2.size(); i++) {
			newVec1.push_back(newVec2.back());
			newVec2.pop_back();
			int tempValue = dividePile(newVec1, newVec2, maxBound);
			maxValue = maxValue > tempValue ? maxValue : tempValue;
			newVec2.insert(newVec2.begin(), newVec1.back());
			newVec1.pop_back();
		}
	}
	return maxValue;
}

int main(int argc, char* argv[]) {
	if (argc != 2) {
		cerr << "wrong parameter" << endl;
		return -1;
	}

	ifstream inf(argv[1]);
	if (!inf) {
		cerr << "cannot open file " << argv[1] << endl;
		return -1;
	}

	string ln; 
	inf >> ln; 
	int caseNum = atoi(ln.c_str());
	for (int cn=0; cn<caseNum; cn++) {
		inf >> ln;
		int candyNum = atoi(ln.c_str());
		vector<int> pile1, pile2;
		for (int candn=0; candn<candyNum; candn++) {
			inf >> ln;
			pile2.push_back(atoi(ln.c_str()));
		}

		// find solution
		int cppBound = candyNum / 2; // means candy-per-pile
		int maxValue = dividePile(pile1, pile2, cppBound);
		cout << "Case #" << cn+1 << ": ";
		if (maxValue == 0) {
			cout << "NO" << endl;
		}
		else {
			cout << maxValue << endl;
		}
	}
	return 0; 
}