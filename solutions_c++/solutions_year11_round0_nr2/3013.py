#include<iostream>
#include<map>
#include<set>
#include<string>

using namespace std;

int getpos(char c){
	return c - 'A';
}

string solve() {
	map<string, string> combine;
	string oppose[100];

	int nc; cin >> nc;

	for (int i = 0; i < nc; i++) {
		string s; cin >> s;
		combine[s.substr(0, 2)] = s.substr(2,1);
		combine[s.substr(1, 1) + s.substr(0, 1)] = s.substr(2,1);
	}

	int no; cin >> no;

	for (int i = 0; i < no; i++) {
		string s; cin >> s;
		oppose[getpos(s[0])] += s.substr(1,1);
		oppose[getpos(s[1])] += s.substr(0,1);
	}

	int size; cin >> size;
	string elements; cin >> elements;

	string result = "";

	for (int i = 0; i < size; i++) {
		string previous = result;
		result += elements[i];
		while (true) {
			if (result.size() > 1) {
				char last1 = result[result.size() - 1];
				string last2 = result.substr(result.size() - 2,2);
				if (combine.find(last2) != combine.end()) {
					result = result.substr(0, result.size() - 2) + combine[last2];
					continue;
				}

				for (int j = 0; j < oppose[getpos(last1)].size(); j++) {
					if (previous.find(oppose[getpos(last1)].substr(j,1)) != string::npos) {
						result = "";
						continue;
					}
				}
			}
			break;
		}
	}

	string list = "[";

	for (int i = 0; i < result.size(); i++) {
		list += result[i];
		if (i < result.size() -1) list += ", ";
	}

	list += "]";

	return list;
}

int main() {
	int tc; cin >> tc;

	for (int t = 1; t <= tc; t++) cout << "Case #" << t << ": " << solve() << endl;

	return 0;
}
