#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
using namespace std;

int c[10];


int main() {
	ifstream fin("B-large.in");
	ofstream fout("bout.txt");
	int T;
	fin >> T;
	char ss[30];
	string s;
	for (int t = 0; t < T; t++) {
		fout << "Case #" << t+1 << ": ";
		fin >> ss;
		s = ss;
		s = "0" + s;
		memset(c, 0, sizeof(c));
		for (int i = s.length() - 1; i > 0; i--) {
			c[s[i] - '0']++;
			if (s[i] > s[i-1]) {
				c[s[i-1] - '0']++;
				for (int j = s[i-1] - '0' + 1; j <= 9; j++) {
					if (c[j]) {
						c[j]--;
						s[i-1] = (char)(j+'0');
						break;
					}
				}
				for (int j = i; j < s.length(); j++) {
					for (int k = 0; k <= 9; k++) {
						if (c[k]) {
							s[j] = (char)(k+'0');
							c[k]--;
							break;
						}
					}
				}
				break;
			}
		}
		if (s[0] == '0')
			s.erase(0, 1);
		fout << s << endl;
	}
	return 0;
}
