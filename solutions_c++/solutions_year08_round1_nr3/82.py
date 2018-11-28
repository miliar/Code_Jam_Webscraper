#include <iostream>
#include <string>
using namespace std;

int main() {
	string s;
	getline(cin, s);
	int i = 0;
	while (getline(cin, s)) {
		s = "000"+s;
		for (int j = 0; j < s.length()+3; j++) if (s[j+3] == '.') cout << "Case #" << ++i << ": " << s[j] << s[j+1] << s[j+2] << endl;
	}
}
