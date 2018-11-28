#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#define FOR(i, a, b) for(int i = a; i < b; ++i)
using namespace std;

char mapping[26];

void preencher() {
	mapping[0] = 'y';
	mapping[1] = 'h';
	mapping[2] = 'e';
	mapping[3] = 's';
	mapping[4] = 'o';
	mapping[5] = 'c';
	mapping[6] = 'v';
	mapping[7] = 'x';
	mapping[8] = 'd';
	mapping[9] = 'u';
	mapping[10] = 'i';
	mapping[11] = 'g';
	mapping[12] = 'l';
	mapping[13] = 'b';
	mapping[14] = 'k';
	mapping[15] = 'r';
	mapping[16] = 'z';
	mapping[17] = 't';
	mapping[18] = 'n';
	mapping[19] = 'w';
	mapping[20] = 'j';
	mapping[21] = 'p';
	mapping[22] = 'f';
	mapping[23] = 'm';
	mapping[24] = 'a';
	mapping[25] = 'q';
}

int main() {
	int t;
	string s;
	preencher();
	scanf("%d\n", &t);
	FOR(i, 0, t) {
		getline(cin, s);
		FOR(j, 0, s.size()) {
			if(s[j] != ' ')
				s[j] = mapping[s[j]-'a'];
		}
		cout << "Case #" << i+1 << ": " << s << endl;
	}
	return 0;
}
