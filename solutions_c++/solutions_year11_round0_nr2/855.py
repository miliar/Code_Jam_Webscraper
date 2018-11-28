#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <string>

using namespace std;

char table[26][26];
bool oppose[26][26];

int main() {
	int T;
	cin >> T;
	for(int t=1; t<=T; t++) {
		int C, D, N;
		for(int i=0; i<26; i++) {
			for(int j=0; j<26; j++) {
				table[i][j] = ' ';
				oppose[i][j] = false;
			}
		}
		cin >> C;
		for(int c=0; c<C; c++) {
			string tmp;
			cin >> tmp;
			table[tmp[0]-'A'][tmp[1]-'A'] = tmp[2];
			table[tmp[1]-'A'][tmp[0]-'A'] = tmp[2];
		}
		cin >> D;
		for(int d=0; d<D; d++) {
			string tmp;
			cin >> tmp;
			oppose[tmp[0]-'A'][tmp[1]-'A'] = true;
			oppose[tmp[1]-'A'][tmp[0]-'A'] = true;
		}
		cin >> N;
		string input;
		cin >> input;
		vector<char> current;
		for(int i=0; i<N; i++) {
			current.push_back(input[i]);
			while(true) {
				if(current.size()<2) break;
				char temp = table[current[current.size()-1]-'A'][current[current.size()-2]-'A'];
				if(temp==' ') {
					break;
				} else {
					current.pop_back();
					current.pop_back();
					current.push_back(temp);
				}
			}
			for(int j=0; j<current.size()-1; j++) {
				if(oppose[current[j]-'A'][current[current.size()-1]-'A']) {
					current.clear();
					break;
				}
			}
		}
		cout << "Case #" << t << ": [";
		for(int i=0; i<current.size(); i++) {
			cout << current[i];
			if(i<current.size()-1) cout << ", ";
		}
		cout << "]" << endl;
	}
	return 0;
}
