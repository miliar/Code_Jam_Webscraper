#include <iostream>
#include <string>
#include <list>
#include <vector>
#include <fstream>

using namespace std;

vector<string> split(string s) {
	vector<string> v;
	int one = 0;
	int two = s.find_first_of('/', 1);
	while(two != string::npos)
	{
		v.push_back(s.substr(one + 1, two - one - 1));
		one = two;
		two = s.find_first_of('/', one + 1);
	}
	v.push_back(s.substr(one + 1, s.length()));
	return v;
}

int insertDir(vector<string>& in, vector<vector<string>>& here) {
	vector<vector<string>>::iterator hereIter;
	hereIter = here.begin();
	int bestPos = 0;
	int rem = -1;
	int currPos = 0;

	while (hereIter != here.end()) {
		int i = 0;
		for(; ; i++) {
			if (i >= hereIter->size() || i >= in.size()) break;
			string here = hereIter->at(i);
			string ins = in.at(i);
			
			if (here.compare(ins) != 0) break;
		}

		if (i > bestPos) { bestPos = i; rem = currPos; }
		currPos++;
		++hereIter;
	}

	here.push_back(in);
	return in.size() - bestPos;
}

int main() {
	ofstream myFile;
	myFile.open ("out.out");
	ifstream input("A-large.in");

	int turns;
	input >> turns;

	for (int t = 1; t <= turns; t++) {
		int N = 0;
		int M = 0;

		input >> N;
		input >> M;

		vector<vector<string>> alreadyHere;
		for (int i = 0; i < N; i++) {
			string s;
			input >> s;
			alreadyHere.push_back(split(s));
		}

		vector<vector<string>> toAdd;
		for (int i = 0; i < M; i++) {
			string s;
			input >> s;
			toAdd.push_back(split(s));
		}

		vector<vector<string>>::iterator toAddIter;
		toAddIter = toAdd.begin();

		int total = 0;
		while (toAddIter != toAdd.end()) {
			vector<string> inserting = *toAddIter;
			++toAddIter;

			total += insertDir(inserting, alreadyHere);		
		}
		cout << total << ' ' << t << endl;
		myFile << "Case #" << t << ": " << total << endl;
	}
}