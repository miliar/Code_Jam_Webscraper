#include <iostream>
#include <cassert>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <utility>
using namespace std;

const int maxlen = 300;

int T, C, D, N;
pair<char, bool> d[maxlen][maxlen];
string s;
vector<char> v;
char x;

void print(int t) {
	cout << "Case #" << t << ": [";
	if (v.size()) {
		for (int i = 0; i < v.size() - 1; i++) cout << v[i] << ", ";
		cout << v[v.size() - 1] << "]" << endl;
	} else {
		cout << "]" << endl;
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> T;

	for (int t = 1; t <= T; t++) {
		for (int i = 0; i < maxlen; i++) for (int j = 0; j < maxlen; j++) d[i][j] = make_pair('0', false);
		//assert(0);
		cin >> C;
		for (int i = 0; i < C; i++) {
			cin >> s;
			d[s[0]][s[1]].first = d[s[1]][s[0]].first = s[2];
		}
		//assert(0);
		cin >> D;
		for (int i = 0; i < D; i++) {
			cin >> s;
			d[s[0]][s[1]].second = d[s[1]][s[0]].second = true;
		}
		//assert(0);
		cin >> N;
		v.clear();

		for (int i = 0; i < N; i++) {
			cin >> x;
			//if (i == 3) print();
			if (v.size()) {
				if (d[x][v[v.size() - 1]].first != '0') {
					v[v.size() - 1] = d[x][v[v.size() - 1]].first;
				} else {
					bool is = false;
					for (int j = 0; j < v.size() && !is; j++) {
						if (d[x][v[j]].second) is = true;
					}
					if (is) v.clear();
					else v.push_back(x);
				}
			} else v.push_back(x);
		}
		//assert(0);
		print(t);
		//assert(0);
	}
}