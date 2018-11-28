#include<iostream>
#include<vector>
#include<map>
#include<string>

using namespace std;

map<char, int> base;
char combine[8][8];
bool oppose[8][8];
string invoke, elementList;

bool inBase(char c) {
	return base.find(c) != base.end();
};

string getOutput() {
	string output = "[";
	output.append(1, elementList[0]);
	for (int i = 1; i < elementList.size(); i++) {
		output += ", ";
		output.append(1, elementList[i]);
	}
	return output + "]";
};

int main() {
	base['Q'] = 0;
	base['W'] = 1;
	base['E'] = 2;
	base['R'] = 3;
	base['A'] = 4;
	base['S'] = 5;
	base['D'] = 6;
	base['F'] = 7;
	int T;
	cin >> T;
	for (int i = 0; T--; i++) {
		memset(combine, 0, sizeof(combine));
		memset(oppose, false, sizeof(oppose));
		invoke = "", elementList = "";
		int C, D, N;
		cin >> C;
		// read combinations
		while (C--) {
			string comb;
			cin >> comb;
			combine[base[comb[0]]][base[comb[1]]] = comb[2];
			combine[base[comb[1]]][base[comb[0]]] = comb[2];
		}
		cin >> D;
		// read opposed reactions
		while (D--) {
			string opp;
			cin >> opp;
			oppose[base[opp[0]]][base[opp[1]]] = true;
			oppose[base[opp[1]]][base[opp[0]]] = true;
		}
		cin >> N;
		cin >> invoke;
		elementList.append(1, invoke[0]);
		for (int j = 1; j < invoke.size(); j++) {
			char nonBase = 0;
			if (inBase(elementList[elementList.size() - 1]))
				nonBase = combine[base[elementList[elementList.size() - 1]]][base[invoke[j]]];
			if (nonBase) {
				elementList[elementList.size() - 1] = nonBase;
			} else {
				bool reacted = false;
				for (int k = 0; !reacted && k < elementList.size(); k++) {
					if (inBase(elementList[k]) && oppose[base[elementList[k]]][base[invoke[j]]]) {
						elementList = "";
						reacted = true;
					}
				}
				if (!reacted) elementList.append(1, invoke[j]);
			}			
		}
		cout << "Case #" << (i + 1) << ": " << getOutput() << endl;
	}
	return 0;
}