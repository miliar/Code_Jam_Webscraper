#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <map>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

int main() {
	int num_cases, casen = 1;
	int C, D, N;
	string combine, opposite;
	map <string,char> combines;
	map <char, char> opposites;
	string base_elements;
	int i, j;
	vector<char> answer;
	string base, temp;
	stringstream ss;
	vector<char>::iterator it;

	cin >> num_cases;
	while (num_cases > 0) {
		answer.clear();
		combines.clear();
		opposites.clear();
		temp.clear();
		base.clear();
		cin >> C;
		for (i = 0; i < C; i++) {
			cin >> combine;
			ss.clear();
			temp.clear();
			ss << combine[1] << combine[0];
			ss >> temp;
			combines[combine.substr(0,2)] = combine[2];
			combines[temp] = combine[2];
			//combines[combine[2]] = combine.substr(0,2);
		}
		cin >> D;
		for (i = 0; i < D; i++) {
			cin >> opposite;
			opposites[opposite[0]] = opposite[1];
			opposites[opposite[1]] = opposite[0];
		}
		cin >> N;
		cin >> base_elements;

		for (i = 0; i < N; i++) {
			answer.push_back(base_elements[i]);
			if (answer.size() > 1) {
				ss.clear();
				base.clear();
				ss << answer[answer.size()-1] << answer[answer.size()-2];
				ss >> base;
				//cout << "Aqui: " << base << endl;
				if (combines[base] != 0) {
					answer.pop_back();
					answer.pop_back();
					answer.push_back(combines[base]);
				}
				else {
					//cout << "entrei:" << opposite[base_elements[i] << endl;
					it = find (answer.begin(), answer.end()-1, opposites[base_elements[i]]);
					if (it != answer.end()-1) {
						//cout << "cheguei" << endl;
						answer.clear();
					}
				}
			}
		}
		cout << "Case #" << casen++ << ": [";
		for (i = 0; i < answer.size(); i++)
			if (i != answer.size()-1) cout << answer[i] << ", ";
			else cout << answer[i];

		cout << "]" << endl;

		num_cases--;
	}

}


