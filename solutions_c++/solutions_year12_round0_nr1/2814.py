#include <iostream>
#include <cstdio>
#include <string>
#include <sstream>

using namespace std;
string w = "yhesocvxduiglbkrztnwjpfmaq";
int main () {
	freopen("sit.in", "r", stdin);
	freopen("sit.out", "w", stdout);
	string s;
	int n;
	getline(cin, s);
	stringstream ss(s);
	ss >> n;
	for (int k = 1; k <= n; k++) {
		getline(cin, s);
		printf("Case #%d: ", k);
		int m = s.length();
		for (int i = 0; i < m; i++) {
            char q = s[i];
            if ('a' <= q && q <= 'z')
                printf("%c", w[q - 'a']);
            else {
                if ('A' <= q && q <= 'Z')
                    printf("%c", w[q - 'A'] - 32);
                else
                    printf("%c", q);
            }

		}
		puts("");
	}



}
