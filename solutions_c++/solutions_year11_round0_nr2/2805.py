#include <cstdio>
#include <cstring>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

typedef pair<int, int> pii;

const int h = 300;

int T, C, D, n;
char c[h][h];
bool d[h][h];
string s;
vector<pii> v;

int main() {
	//ifstream in("input.txt");
	ifstream in("B-large.in");
	freopen("B-large.out", "w", stdout);
	in >> T;
	for (int t = 0; t < T; t++) {
		memset(c, 0, sizeof c);
		memset(d, 0, sizeof d);
		in >> C;
		for (int i = 0; i < C; i++) {
			in >> s;
			c[s[0]][s[1]] = c[s[1]][s[0]] = s[2];
		}
		in >> D;
		for (int i = 0; i < D; i++) {
			in >> s;
			d[s[0]][s[1]] = d[s[1]][s[0]] = 1;
		}
		in >> n;
		in >> s;
		string res = "";
		for (int i = 0; i < n; i++) {
			if (res.length()) {
				if (c[res[res.length() - 1]][s[i]]) {
					res[res.length() - 1] = c[res[res.length() - 1]][s[i]];
				} else {
					for (int j = 0; j < res.length(); j++) {
						if (d[res[j]][s[i]]) {
							res = "";
							break;
						}
					}
					if (res.length())
						res += s[i];
				}
			}
			else
				res += s[i];
		}
		printf("Case #%d: [", t+1);
		for (int i = 0; i < res.length(); i++) {
			if (i)
				printf(", ");
			printf("%c", res[i]);
		}
		puts("]");
	}
}