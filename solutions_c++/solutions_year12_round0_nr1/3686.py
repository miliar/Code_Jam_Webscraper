#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;

#define forab(i, a, b) for (int i = a; i < int(b); ++i)
#define fordab(i, a, b) for (int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab (i, 0, n)
#define ford(i, n) fordab (i, 0, n)
#define forv(i, a) forn (i, a.size())

char p[26];

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	p[0] = 'y';
	p[1] = 'n';
	p[2] = 'f';
	p[3] = 'i';
	p[4] = 'c';
	p[5] = 'w';
	p[6] = 'l';
	p[7] = 'b';
	p[8] = 'k';
	p[9] = 'u';
	p[10] = 'o';
	p[11] = 'm';
	p[12] = 'x';
	p[13] = 's';
	p[14] = 'e';
	p[15] = 'v';
	p[16] = 'z';
	p[17] = 'p';
	p[18] = 'd';
	p[19] = 'r';
	p[20] = 'j';
	p[21] = 'g';
	p[22] = 't';
	p[23] = 'h';
	p[24] = 'a';
	p[25] = 'q';
	int t;
	cin >> t;
	string s;
	getline(cin, s);
	forn (i, t) {
		getline(cin, s);
		cout << "Case #" << i + 1 << ": ";
		forv (j, s) {
			if (s[j] == ' ') {
				cout << ' ';
			} else {
				forn (c, 26) {
					if (p[c] == s[j]) {
						cout << char(c + 'a');
					}
				}
			}
		}
		cout << endl;
	}
}
