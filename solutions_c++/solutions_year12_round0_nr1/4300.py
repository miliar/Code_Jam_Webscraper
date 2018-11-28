#include <iostream>
#include <string>

using namespace std;

char letters[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main() {
	int tests;
	cin >> tests;
	cin.ignore();
	for (int i = 1; i <= tests; i++) {
		string s;
		getline(cin, s);
		for (int j = 0; j < s.length(); j++)
			if (s[j] >= 'a' && s[j] <= 'z')
				s[j] = letters[s[j] - 'a'];
		cout << "Case #" << i << ": " << s << endl;
	}
	return 0;
}
