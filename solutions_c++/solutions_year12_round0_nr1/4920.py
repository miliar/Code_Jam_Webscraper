#include <iostream>
#include <stdint.h>
#include <string>
#include <cstring>

using namespace std;

int main() {
	int32_t n;
	
	cin >> n;
	
	char c[101];
	cin.getline(c, 101);
	for (int32_t i = 0; i < n; i++) {

		memset(c, 0, sizeof(c));
		
		cin.getline(c, 101);
		
		string s(c);

		string b;
		for (int32_t j = 0; j < s.length(); j++) {
			b += (s[j] == ' ') ? ' ' : "yhesocvxduiglbkrztnwjpfmaq"[s[j] - 'a'];
		}
		cout << "Case #" << i + 1 << ": " << b << endl;
	}
}
