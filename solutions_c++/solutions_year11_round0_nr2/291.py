#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>

#include <cstdio>
#include <cstring>
#include <cassert>
#include <cmath>
#include <ctime>

using namespace std;

typedef long long int64;
typedef long double ldouble;

#define PB(a) push_back(a)
#define MP(a, b) make_pair(a, b)

#define PROBLEM "B"

struct Pair {
	char a, b;
	Pair(char A, char B) : a(A), b(B) {}
};

struct Trio {
	char a, b, c;
	Trio(char A, char B, char C) : a(A), b(B), c(C) {}
};

vector <Trio> com;
vector <Pair> ann;

inline bool isBase(char c) {
	return (c == 'Q' || c == 'W' || c == 'E' || c == 'R' || 
			c == 'A' || c == 'S' || c == 'D' || c == 'F');
}

pair <char, char> getLastTwo(vector <char> &st) {
	assert(st.size() >= 2);
	int l = st.size();
	return MP(st[l-2], st[l-1]);
}

char existsTrio(pair <char, char> el) {
	char a = el.first, b = el.second;
	for (size_t i = 0; i < com.size(); i++) {
		if (com[i].a == a && com[i].b == b || com[i].a == b && com[i].b == a) {
			return com[i].c;
		}
	}
	return 0;
}

bool checkAnn(vector <char> &st) {
	assert(st.size() >= 2);
	int l = st.size();
	char last = st[l-1];
	for (int i = 0; i < l-1; i++) {
		for (size_t j = 0; j < ann.size(); j++) {
			if (ann[j].a == last && ann[j].b == st[i] || ann[j].b == last && ann[j].a == st[i]) {
				return true;
			}
		}
	}

	return false;
}

int main() {
	freopen(PROBLEM ".in", "rt", stdin);
	freopen(PROBLEM ".out", "wt", stdout);

	int T;
	scanf("%d\n", &T);

	for (int t = 1; t <= T; t++) {
		printf("Case #%d: ", t);

		com.clear();
		ann.clear();

		int n, m, l;

		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			string pr;
			cin >> pr;
			assert(pr.size() == 3);
			com.PB(Trio(pr[0], pr[1], pr[2]));
			assert(isBase(pr[0]) && isBase(pr[1]) && !isBase(pr[2]));
		}

		scanf("%d", &m);
		for (int i = 0; i < m; i++) {
			string pr;
			cin >> pr;
			assert(pr.size() == 2);
			ann.PB(Pair(pr[0], pr[1]));
			assert(isBase(pr[0]) && isBase(pr[1]));
		}

		scanf("%d", &l);
		string str;
		cin >> str;

		assert(str.size() == l);

		vector<char> st;
		st.clear();

		for (int j = 0; j < l; j++) {
			st.PB(str[j]);
			if (st.size() >= 2) {
				char c = existsTrio(getLastTwo(st));
				if (c != 0) {
					st.pop_back();
					st.pop_back();
					st.PB(c);
				}
				else {
					if (checkAnn(st)) {
						st.clear();
					}
				}
			}
		}

		printf("[");
		for (int i = 0; i < st.size(); i++) {
			if (i != 0) printf(", ");
			printf("%c", st[i]);
		}
		printf("]");

		printf("\n");
	}

	return 0;
}
