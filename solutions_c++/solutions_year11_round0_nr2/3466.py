
#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

vector<char> combinations(26 * 26);
vector<bool> rejections(26 * 26);

inline char combination(char c1, char c2) {
	return combinations[(c1 - 'A') * 26 + (c2 - 'A')];
}

inline void combine(char c1, char c2, char c) {
	combinations[(c1 - 'A') * 26 + (c2 - 'A')] = c;
	combinations[(c2 - 'A') * 26 + (c1 - 'A')] = c;
}

inline bool opposed(char c1, char c2) {
	return rejections[(c1 - 'A') * 26 + (c2 - 'A')];
}

inline void reject(char c1, char c2) {
	rejections[(c1 - 'A') * 26 + (c2 - 'A')] = true;
	rejections[(c2 - 'A') * 26 + (c1 - 'A')] = true;
}

int
main()
{
	int ncases; cin >> ncases;
	for (int i = 1; i <= ncases; i++) {
		fill(combinations.begin(), combinations.end(), '\0');
		fill(rejections.begin(), rejections.end(), false);
		int nc; cin >> nc;
		for (int k = 0; k < nc; k++) {
			string s; cin >> s; combine(s[0], s[1], s[2]);
		}
		int nr; cin >> nr;
		for (int k = 0; k < nr; k++) {
			string s; cin >> s; reject(s[0], s[1]);
		}
		int n; cin >> n;
		string magic; cin >> magic;
		char potion[256], *t = potion; *t = 0;
		for (unsigned k = 0; k < magic.size(); k++) {
			char c = magic[k];
			if (potion == t) {
				*t++ = c;
				*t = 0;
			} else {
				char c1 = combination(c, *(t - 1));
				if (c1) {
					*(t - 1) = c1;
				} else {
					bool collided = false;
					for (char *p = potion; p < t; p++) {
						if (opposed(*p, c)) {
							t = potion; collided = true;
							break;
						}
					}
					if (!collided) {
						*t++ = c;
						*t = 0;
					}
				}
			}
		}
		cout << "Case #" << i << ": [";
		for (char *p = potion; p < t; p++) {
			cout << *p;
			if (t - p > 1) {
				cout << ", ";
			}
		}
		cout << "]" << endl;
	}
}
