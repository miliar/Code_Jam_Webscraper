#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

void testCase( vector<char>& result, const map<pair<char,char>, char>& combinations, const map<char, char>& oppositions, const string& input ) {
	for (string::const_iterator it = input.begin(); it != input.end(); ++it) {
		char c = *it;

		if ( result.empty() ) {
			result.push_back(c);
			continue;
		}

		vector<char>::iterator res_it;

		res_it = result.end() - 1;
		char c1 = c;
		char c2 = *res_it;
		if (c1 > c2) {
			swap( c1, c2 );
		}
		
		map<pair<char,char>, char>::const_iterator comb_it;
		map<char, char>::const_iterator op_it;
		
		if ((comb_it = combinations.find(pair<char, char>(c1, c2))) != combinations.end()) {
			
			*res_it = comb_it->second;
		} else if ((op_it = oppositions.find(c)) != oppositions.end()) {
			if ((res_it = find(result.begin(), result.end(), op_it->second)) != result.end()) {
				result.erase(result.begin(), result.end());
			} else {
				result.push_back(c);
			}
			
			/*vector<char>::reverse_iterator res_rit;
			if ((res_rit = find(result.rbegin(), result.rend(), op_it->second)) != result.rend()) {
				result.erase(--res_rit.base(), result.end());
			} else {
				result.push_back(c);
			}*/
		} else {
			result.push_back(c);
		}
	}
}

int main(int argc, char** argv) {
	ifstream fin;

	string filename = "b.in";

	if (argc > 1) {
		filename = argv[1];
	}

	fin.open(filename, ios_base::in);

	int T;

	fin >> T;

	for (int i = 0; i < T; i++) {
		int C;
		fin >> C;
		map<pair<char,char>, char> combinations;
		for (int j = 0; j < C; j++) {
			string combination;

			fin >> combination;

			char c1 = combination[0];
			char c2 = combination[1];

			if (c1 > c2) {
				swap( c1, c2 );
			}

			combinations[ pair<char,char>(c1, c2) ] = combination[2];

			//combinations.push_back(combination);
		}

		int D;
		fin >> D;

		map<char, char> oppositions;
		for (int j = 0; j < D; j++) {
			string opposing;

			fin >> opposing;
			oppositions[opposing[0]] = opposing[1];
			oppositions[opposing[1]] = opposing[0];
		}

		int N;
		string input;
		fin >> N >> input;

		vector<char> result;
		testCase(result, combinations, oppositions, input);

		cout << "Case #" << (i+1) << ": [";

		for (vector<char>::const_iterator it = result.begin(); it != result.end(); ++it) {
			if (it != result.begin()) {
				cout << ", ";
			}
			cout << *it;
		} 

		cout << "]" << endl;
	}

	//cin.get();

	return 0;
}