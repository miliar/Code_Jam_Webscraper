#include <iostream>
#include <set>
#include <string>
#include <cstdio>

using namespace std;

int main() {

	int test;
	cin >> test;
	for (int i = 1; i <= test; i++) {
		int engines, queries;
		cin >> engines;
		int count = 0;
		set<string> names;
		while (getchar() != '\n');
		for (int j = 0; j < engines; j++) {
			string temp;
			getline(cin, temp);
			names.insert(temp);
		}
		cin >> queries;
		while (getchar() != '\n');
		set<string> tempnames;
		for (int j = 0; j < queries; j++) {
			string temp;
			getline(cin, temp);
			tempnames.insert(temp);
			if (tempnames.size() == names.size()) {
				count++;
				tempnames.clear();
				tempnames.insert(temp);
			}
		}
		cout << "Case #" << i << ": " << count << endl;
	}
}
