#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <fstream>

using namespace std;

int solveA(ifstream & input) {
	int stepCount;
	input >> stepCount;
	vector<int> orange;
	vector<int> blue;
	vector<char> sequence;
	for (int i = 0; i < stepCount; ++i) {
		char s;
		int t;
		input >> s;
		input >> t;
		if (s == 'O') {
			orange.push_back(t);
		} else {
			blue.push_back(t);
		}
		sequence.push_back(s);
	}
	int time = 0;
	int oPos = 1;
	int bPos = 1;
	vector<int>::iterator oPressed = orange.begin();
	vector<int>::iterator bPressed = blue.begin();
	vector<char>::iterator progress = sequence.begin();

	while (progress != sequence.end()) {
		bool oStep = false;
		bool bStep = false;
		if (*progress == 'O' && *oPressed == oPos) {
			++oPressed;
			++progress;
			oStep = true;
		} else {
			if (*progress == 'B' && *bPressed == bPos) {
				++bPressed;
				++progress;
				bStep = true;
			}
		}
		if (!oStep && oPressed != orange.end() && oPos < *oPressed) {
			++oPos;
		}
		if (!oStep && oPressed != orange.end() && oPos > *oPressed) {
			--oPos;
		}
		if (!bStep && bPressed != blue.end() && bPos < *bPressed) {
			++bPos;
		}
		if (!bStep && bPressed != blue.end() && bPos > *bPressed) {
			--bPos;
		}
		++time;
	}
	return time;
}

void readDataB(ifstream & input, vector<string> * combines, vector<string> * opposed, string * invoked) {
	int combsCount;
	input >> combsCount;
	combines->resize(combsCount);
	for (int i = 0; i < combsCount; ++i) {
		input >> combines->at(i);
	}
	int oppCount;
	input >> oppCount;
	opposed->resize(oppCount);
	for (int i = 0; i < oppCount; ++i) {
		input >> opposed->at(i);
	}
	int t;
	input >> t;
	input >> *invoked;
}

string formatResult(const string & s) {
	string res = "[";
	for (int i = 0; i < s.size(); ++i) {
		if (i > 0) {
			res = res + ", ";
		}
		res = res + s[i]; 
	}
	res = res + "]";
	return res;
}

string solveB(ifstream & input) {
	string res = "";
	vector<string> combines;
	vector<string> opposed;
	string invoked;
	readDataB(input, &combines, &opposed, &invoked);
	for (int i = 0; i < invoked.length(); ++i) {
		bool happend = false;
		if (res.length() > 0) {
			for (int j = 0; j < combines.size(); ++j) {
				if (combines[j][0] == res[res.length() - 1] && combines[j][1] == invoked[i] ||
					combines[j][1] == res[res.length() - 1] && combines[j][0] == invoked[i]) {
					res = res.substr(0, res.length() - 1) + combines[j][2];
					happend = true;
					break;
				}
			}
			if (!happend) {
				for (int j = 0; j < opposed.size(); ++j) {
					for (int k = 0; k < res.length(); ++k) {
						if (opposed[j][0] == res[k] && opposed[j][1] == invoked[i] ||
							opposed[j][1] == res[k] && opposed[j][0] == invoked[i]) {
							res = "";
							happend = true;
							break;
						}
					}
				}
			}
		}
		if (!happend) {
			res = res + invoked[i];
		}
	}
	return formatResult(res);
}

int main() {
	ifstream input("input.txt");
	ofstream output("output.txt");
	int testCount;
	input >> testCount;
	for (int test = 0; test < testCount; ++test) {
		output << "Case #" << test + 1 << ": " << solveB(input) << endl;
		//cout << "Case #" << test + 1 << ": " << solveB(input) << endl;
	}
	return 0;
}