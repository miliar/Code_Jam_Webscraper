#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>

using namespace std;

string alpha = "yhesocvxduiglbkrztnwjpfmaq";
string s;
int n;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d\n", &n);
	for(int i = 0; i < n; ++i) {
		getline(cin, s);
		for(int j = 0; j < s.length(); ++j)
			if(s[j] >= 'a' && s[j] <= 'z')
				s[j] = alpha[s[j]-'a'];
		cout << "Case #" << i+1 << ": " << s << endl;
	}	
}