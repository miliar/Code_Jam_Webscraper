#include <iostream>
#include <string>
#include <sstream>
using namespace std;

#define si size()

int t;
string s, slo="yhesocvxduiglbkrztnwjpfmaq";

int main() {
	cin >> t;
	getline(cin, s);
	for(int i = 1; i <= t; i++) {
		getline(cin, s);
		for(int j = 0; j < s.si; j++) {
			if(s[j]!=' ')
				s[j] = slo[s[j]-'a'];
		}
		cout << "Case #" << i << ": " << s << "\n";
	}
	return 0;
}
