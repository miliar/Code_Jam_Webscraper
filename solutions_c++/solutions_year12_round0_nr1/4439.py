#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

/*string s, t;
int m[200];*/

char charToChar[200];
char s[105];
int len;

void init () {
	charToChar['a'] = 'y';
	charToChar['b'] = 'h';
	charToChar['c'] = 'e';
	charToChar['d'] = 's';
	charToChar['e'] = 'o';
	charToChar['f'] = 'c';
	charToChar['g'] = 'v';
	charToChar['h'] = 'x';
	charToChar['i'] = 'd';
	charToChar['j'] = 'u';
	charToChar['k'] = 'i';
	charToChar['l'] = 'g';
	charToChar['m'] = 'l';
	charToChar['n'] = 'b';
	charToChar['o'] = 'k';
	charToChar['p'] = 'r';
	charToChar['q'] = 'z';
	charToChar['r'] = 't';
	charToChar['s'] = 'n';
	charToChar['t'] = 'w';
	charToChar['u'] = 'j';
	charToChar['v'] = 'p';
	charToChar['w'] = 'f';
	charToChar['x'] = 'm';
	charToChar['y'] = 'a';
	charToChar['z'] = 'q';
}

void solve () {
	int i;

	gets(s);
	len = strlen(s);

	for (i = 0;i < len;i++) {
		if (s[i] != ' ')
			printf("%c", charToChar[s[i]]);
		else
			printf(" ");
	}
}

int main () {
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int test, t;

	init();

	scanf("%d\n",&test);
	for (t = 0;t < test;t++){
		if (t)
			printf("\n");
		printf("Case #%d: ",t + 1);
		solve();
	}

	/*cin >> s;
	cin >> t;

	for (int i = 0;i < s.size();i++) {
		m[s[i]] = t[i];
	}

	for (int i = 'a';i <= 'z';i++) {
		if (m[i] != 0) {
			printf("charToChar['%c'] = '%c';\n", i, m[i]);
		}
	}*/
	return 0;
}