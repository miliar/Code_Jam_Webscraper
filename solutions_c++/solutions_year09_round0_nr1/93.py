
#include <cstdio>
#include <iostream>
#include <set>
#include <string>

using namespace std;

string dic[5000];
int L, D, N;

void Process(int casei, string &tmp) {
	set<char> p[15];
	int pn = 0;
	for (int i = 0; i < tmp.length(); ++i) {
		if (tmp[i] == '(') {
			++i;
			while (tmp[i] != ')') {
				p[pn].insert(tmp[i++]);
			}
			pn++;
		} else {
			p[pn].insert(tmp[i]);
			pn++;
		}
	}
	int cnt = 0;
	for (int j = 0; j < D; ++j) {
		bool found = true;
		for (int k = 0; k < L; ++k) {
			if (p[k].find(dic[j][k]) == p[k].end()) {
				found = false;
				break;
			}
		}
		if (found) {
			cnt++;
		}
	}
	printf("Case #%d: %d\n", casei, cnt);
}

int main() {
	cin >> L >> D >> N;

	for (int i = 0; i < D; ++i) {
		cin >> dic[i];
	}
	for (int j = 0; j < N; ++j) {
		string tmp;
		cin >> tmp;
		Process(j+1, tmp);
	}
	return 0;
}
