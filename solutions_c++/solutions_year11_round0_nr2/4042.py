#include <iostream>
#include <string>
#include <map>
using namespace std;

int main() {
	int t = 0;

	cin >> t;
	for (int caseId = 1; caseId <= t; caseId++) {
		int c = 0;
		int d = 0;
		int n = 0;
		map<string, string> combine;
		map<char, char> opposed;
		string buffer;
		string list;

		for (char i = 'A'; i <= 'Z'; i++) {
			for (char j = 'A'; j <= 'Z'; j++) {
				combine[string(1, i) + string(1, j)] = string(1, i) + string(1,
						j);
			}
			opposed[i] = '.';
		}

		cin >> c;
		for (int i = 0; i < c; i++) {
			cin >> buffer;
			combine[string(1, buffer[0]) + string(1, buffer[1])]
					= buffer.substr(2);
			combine[string(1, buffer[1]) + string(1, buffer[0])]
					= buffer.substr(2);
		}
		cin >> d;
		for (int i = 0; i < d; i++) {
			cin >> buffer;
			opposed[buffer[0]] = buffer[1];
			opposed[buffer[1]] = buffer[0];
		}
		cin >> n;
		cin >> buffer;

		for (int i = 0; i < buffer.size(); i++) {
			list.push_back(buffer[i]);
			if (list.size() >= 2) {
				list = list.substr(0, list.size() - 2) + combine[list.substr(
						list.size() - 2)];
			}

			if (list.size() > 0 && list.find(opposed[list[list.size() - 1]])
					!= string::npos) {
				list.clear();
			}
		}
		cout << "Case #" << caseId << ": [";
		if (list.size() > 0) {
			cout << list[0];
		}
		for (int i = 1; i < list.size(); i++) {
			cout << ", " << list[i];
		}
		cout << "]" << endl;
	}
	return 0;
}
