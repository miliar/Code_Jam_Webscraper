#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <list>

using namespace std;

#define INDEX(c) (c - 'A')
#define CHAR(i) (char)(i + 'A') 

int main(int argc, char* argv[]) {
	if (argc != 2) {
		cout << "Invalid input parameters!" << endl;
		return -1;
	}

	ifstream in(argv[1]);
	if (in) {
		int total;
		in >> total;
		int caseNo = 1;
		while (total--) {
			int combine[26][26];
			bool opposed[26][26];
			for (int i = 0; i < 26; i++)
				for (int j = 0; j < 26; j++) {
					combine[i][j] = -1;
					opposed[i][j] = false;
				}
					
			int count;
			in >> count;
			while (count--) {
				char s[4];
				in >> s;
				combine[INDEX(s[0])][INDEX(s[1])] = INDEX(s[2]);	
				combine[INDEX(s[1])][INDEX(s[0])] = INDEX(s[2]);		
			}

			in >> count;
			while (count--) {
				char s[3];
				in >> s;
				opposed[INDEX(s[0])][INDEX(s[1])] = true;
			}

			cout << "Case #" << caseNo++ << ": [";
			string s;
			in >> count >> s;
			list<int> result;
			for (int i = 0; i < count; i++) {
				int current = INDEX(s[i]);
				if (result.size()) {
					int last = result.back();
					if (combine[last][current] > 0) {
						result.pop_back();
						result.push_back(combine[last][current]);
						continue;
					}
					
					bool hasOpposed = false;
					list<int>::iterator itr;
					for (itr = result.begin() ; itr != result.end(); itr++)
						if (opposed[*itr][current] || opposed[current][*itr]) {
							hasOpposed = true;
							break;
						}
					if (hasOpposed) {
						result.clear();
						continue;
					}
				}
				result.push_back(current);
			}
			
			list<int>::iterator itr = result.begin();
			while (itr != result.end()) {
				cout << CHAR(*itr);
				if (++itr != result.end())
					cout << ", ";
			}
			cout << "]" << endl;
		}
	}

	return 0;
}
