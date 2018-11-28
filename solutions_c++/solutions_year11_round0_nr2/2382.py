#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

// zzz
vector<string> combs, oppos;
vector<char> invoked;
int cases, comNum, oppNum, invNum;
string invoke, temp;

void check();

void combined(int i) {
	invoked.erase(invoked.end()-2, invoked.end());
	invoked.push_back(combs[i][2]);
	check();
}

void check() {
	if (invoked.size() < 2) return;

	// Check for any combinations
	for (int i = 0; i < comNum; i++) {
		if (combs[i][0] == invoked.back()) {
			if (combs[i][1] == invoked[invoked.size()-2]) {
				combined(i);
				break;
			}
		}
		if (combs[i][1] == invoked.back()) {
			if (combs[i][0] == invoked[invoked.size()-2]) {
				combined(i);
				break;
			}
		}
	}

	for (int i = 0; i < oppNum; i++) {
		for (int j = 0; j < invoked.size(); j++) {
			if (oppos[i][0] == invoked[j]) {
				for (int k = 0; k < invoked.size(); k++) {
					if (oppos[i][1] == invoked[k]) {
						invoked.clear();
						return;
					}
				}
			}
		}
	}
}

int main(int argc, const char *argv[])
{
	// Exit if we dont have a filename
	if (argc != 2) return 1;
	
	
	ifstream input;
	input.open(argv[1]);
	
	input >> cases;

	for (int i = 0; i < cases; i++) {
		combs.clear(); oppos.clear(); invoked.clear();

		// Read in combinations
		input >> comNum;
		for (int c = 0; c < comNum; c++) {
			input >> temp;
			combs.push_back(temp);
		}
		// Read in oppositions
		input >> oppNum;
		for (int o = 0; o < oppNum; o++) {
			input >> temp;
			oppos.push_back(temp);
		}

		input >> invNum;
		input >> invoke;

		for (int j = 0; j < invNum; j++) {
			invoked.push_back(invoke[j]);
			check();
		}
		
		cout << "Case #" << i+1 << ": [";
		for(int i = 0; i< invoked.size(); i++) {
			cout << invoked[i];
			if (i != invoked.size()-1) cout << ", ";
		}
		cout << "]" << endl;	
	}

	return 0;
}
