#include <iostream>
#include <vector>
#include <conio.h>
using namespace std;


bool find(char* s, int length, char c) {
	for (int i = 0; i < length; i++) {
		if (s[i] == c) {
			return true;
		}
	}
	return false;
}


int main() {
	int T, C, D, N;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		vector<char*> c;
		cin >> C;
		while (C--) {
			char tmp[4];
			cin >> tmp;
			c.push_back(tmp);
		}

		vector<char*> d;
		cin >> D;
		while (D--) {
			char tmp[3];
			cin >> tmp;
			d.push_back(tmp);
		}

		cin >> N;
		char *s = new char[N + 1];
		char *b = new char[N + 1];
		cin >> s;

		int j = 0;
		for (int i = 0; i < N; i++) {
			b[j] = s[i];
			if (j > 0) {
				// combine
				for (int l = 0; l < c.size(); l++) {
					if (b[j] == c[l][0] && b[j-1] == c[l][1] ||
					    b[j] == c[l][1] && b[j-1] == c[l][0]) {
						b[--j] = c[l][2];
						break;
					}
				}

				// oppose
				for (int l = 0; l < d.size(); l++) {
					if (b[j] == d[l][0] && find(b, j, d[l][1]) ||
						b[j] == d[l][1] && find(b, j, d[l][0])) {
						j = -1;
						break;
					}
				}
			}
			++j;
		}

		

		cout << "Case #" << t << ": [";
		for (int i = 0; i < j; i++) {
			if (i < j -1) {
				cout << b[i] << ", ";
			} else {
				cout << b[i];
			}
		}
		cout << "]" << endl;
	}
}