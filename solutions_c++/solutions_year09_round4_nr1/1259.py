#include <algorithm>
#include <cassert>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <string>
#include <utility>
#include <vector>

using namespace std;

struct Sequence {
	vector<int> p;
	bool operator<(const Sequence& other) const {
		assert(this->p.size() == other.p.size());
		for (int i = 0; i < this->p.size(); i++) {
			if (this->p[i] < other.p[i])
				return true;
			else if (this->p[i] > other.p[i])
				return false;
		}
		return true;
	}
	bool operator==(const Sequence& other) const {
		assert(this->p.size() == other.p.size());
		for (int i = 0; i < this->p.size(); i++) {
			if (this->p[i] != other.p[i])
				return false;
		}
		return true;
	}
};

bool is_bad(string s, int row) {
	for (int i = row + 1; i < s.length(); i++) {
		if (s[i] == '1')
			return true;
		else
			assert(s[i] == '0');
	}
	return false;
}

int main() {
	int num_test_cases; cin >> num_test_cases;
	for (int test_case = 1; test_case <= num_test_cases; test_case++) {
		int N; cin >> N;
		vector<string> matrix;
		matrix.resize(N);
		string temp;
		for (int i = 0; i < N; i++) {
			cin >> matrix[i];
		}
		map<string, int> seen_sequence;
		string s = "";
		for (int i = 0; i < N; i++) {
			s = s + char(i + '0');
			//s.p[i] = i;
		}
		seen_sequence[s] = 0;
		list<string> bfs;
		bfs.push_back(s);
		int answer = -1;
//cout << "1" << endl;
		while (!bfs.empty()) {
			s = bfs.front();
			bfs.pop_front();
//cout << "2: " << s << endl;
			// check if sequence is bad
			assert(s.length() == N);
			bool found_answer = true;
			for (int i = 0; i < N; i++) {
				if (is_bad(matrix[s[i] - '0'], i)) {
//cout << "failed: " << matrix[s[i] - '0'] << ", " << i << endl;
					found_answer = false;
					break;
				}
			}
			if (found_answer) {
				answer = seen_sequence[s];
				break;
			}
			// recurse
			int curr = seen_sequence[s];
			for (int i = 0; i < N - 1; i++) {
				char temp = s[i];
				s[i] = s[i + 1];
				s[i + 1] = temp;
				if (seen_sequence.find(s) == seen_sequence.end()) {
//cout << "3: "<< bfs.size() << endl;
					bfs.push_back(s);
					seen_sequence[s] = curr + 1;
				}
				s[i + 1] = s[i];
				s[i] = temp;
			}
		}
		assert(answer != -1);
		// print answer
		cout << "Case #" << test_case << ": " << answer << endl;
	}
}
