#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>

using namespace std;

class Magicka {
	vector<string> combine, opposed;
	map<string, char> combine_map;
	set<string> opposed_set;
	string invoke;

public:
	void set_data(const vector<string>& com, const vector<string>& opp, const string& inv) {
		combine_map.clear();
		opposed_set.clear();

		combine = com;
		opposed = opp;
		invoke = inv;
		for (vector<string>::iterator p = combine.begin(); p != combine.end(); ++p) {
			string str;
			str = p->substr(0, 2);
			char c = (*p)[2];
			combine_map[str] = c;
			swap(str[0], str[1]);
			combine_map[str] = c;
		}
		for (vector<string>::iterator p = opposed.begin(); p != opposed.end(); ++p) {
			string str;
			str = p->substr(0, 2);
			opposed_set.insert(str);
			swap(str[0], str[1]);
			opposed_set.insert(str);
		}
	}

#if 0
	char check_combine(char a, char b) {
		for (vector<string>::iterator p = combine.begin(); p != combine.end(); ++p) {
			if (((*p)[0] == a && (*p)[1] == b) || ((*p)[0] == b && (*p)[1] == a))
				return (*p)[2];
		}
		return NULL;
	}

	bool check_opposed(char a, char b) {
		for (vector<string>::iterator p = opposed.begin(); p != opposed.end(); ++p) {
			if (((*p)[0] == a && (*p)[1] == b) || ((*p)[0] == b && (*p)[1] == a))
				return true;
		}
		return false;
	}
#endif

	string solve() {
		int combine_pos = -1;
		for (int i = 0; i < invoke.size() - 1; i++) {
			string str = invoke.substr(i, 2);
			//str = invoke.substr(i, 2);
			if (combine_map.find(str) != combine_map.end()) {
				invoke.erase(i+1, 1);
				invoke[i] = combine_map[str];
				combine_pos = max(combine_pos, i);
				//i = -1;
				i--;
				continue;
			}
#if 0
			if (combine_pos >= 0) {
			for (int j = i; j >= 0; j--) {
			//for (int j = i; j >= combine_pos; j--) {
				str[0] = invoke[j];
				if (opposed_set.find(str) != opposed_set.end()) {
					invoke.erase(j, i-j+2);
					if (invoke.empty()) return invoke;
					i = -1;
					break;
				}
			}
			}
#endif
//			if (combine_pos < 0) {
			//bool is_opposed = false;
				for (int j = i; j >= 0; j--) {
					str[0] = invoke[j];
					if (opposed_set.find(str) != opposed_set.end()) {
						invoke.erase(0, i+2);
						if (invoke.empty()) return invoke;
						i = -1;
						//is_opposed = true;
						break;
					}
				}
				//if (is_opposed) continue;
//			}

		}

		return invoke;
	}
};

int main()
{
	//fstream fs("test.in");
	//fstream fs("B-small-attempt0.in");
	//fstream fs("B-small-attempt1.in");
	//fstream fs("B-small-attempt2.in");
	//fstream fs("B-small-attempt3.in");
	fstream fs("B-large.in");

	int T, C, D, N;
	string str;
	vector<string> combine, opposed;
	string invoke;

	Magicka test;

	fs >> T;
	//cerr << T << endl; /////
	for (int i = 0; i < T; i++) {
		//cerr << i << endl; /////

		combine.clear();
		opposed.clear();

		fs >> C;
		for (int j = 0; j < C; j++) {
			fs >> str;
			combine.push_back(str);
		}
		fs >> D;
		for (int j = 0; j < D; j++) {
			fs >> str;
			opposed.push_back(str);
		}
		fs >> N;
		fs >> invoke;
		//cerr << invoke << endl; /////

		test.set_data(combine, opposed, invoke);
		string ans(test.solve());

		if (ans.empty()) cout << "Case #" << i + 1 << ": []" << endl;
		else {
			cout << "Case #" << i + 1 << ": [";
			cout << ans[0];
			for (string::iterator p = ans.begin() + 1; p != ans.end(); ++p)
				cout << ", " << *p;
			cout << "]" << endl;
		}
	}

	return 0;
}
