#include <set>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

#define MAXX 2000000
set< pair<int, int> > S[MAXX + 1];

string toString(int I) {
	char buf[50];
	sprintf(buf, "%d", I);
	return string(buf);
}

int toInt(string S) {
	return atoi(S.c_str());
}

void preCal() {
	for (int N = 1; N <= MAXX; N++) {
		string str = toString(N);
		for (int i = 1; i < str.length(); i++) {
			int M = toInt(str.substr(i) + str.substr(0, i));
			if (M > N && M <= MAXX)
				S[N].insert(make_pair(N, M));
		}
	}
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	
	preCal();
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int A, B;
		cin >> A >> B;
		set< pair<int, int> > Set;
		set< pair<int, int> >::iterator it;
		for (int i = A; i <= B; i++) {
			for (it = S[i].begin(); it != S[i].end(); it++) {
				pair<int, int> P = *it;
				if (P.second <= B) Set.insert(P);
			}
		}
		cout << "Case #" << t << ": " << Set.size() << endl;
	}
	return 0;
}
