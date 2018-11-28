#include <iostream>
#include <map>
#include <string>

using namespace std;

int main() {
	string test = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc"
		"ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
		"de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string output = "our language is impossible to understand there"
			"are twenty six factorial possibilities"
			"so it is okay if you want to just give up";
	map<char, char> dictionary;
	for (int i = 0; i < test.size(); ++i) {
				dictionary[test[i]] = output[i];
	}
	dictionary['z'] = 'q';
	dictionary['q'] = 'z';
	int n_cases;
	cin >> n_cases;
	string line;
	getline(cin, line);
	for (int i = 1; i <= n_cases; ++i) {
		getline(cin, line);
		//cout << "line is " << line << endl;
		cout << "Case #" << i << ": ";
		for (int s = 0; s < line.size(); ++s) {
			cout << dictionary[line[s]];
		} 
		cout << endl;
	}
}
