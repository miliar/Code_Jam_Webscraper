#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <assert.h>

#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <string>

using namespace std;

const int MAXN = 50;
const int MAXL = MAXN * MAXN;

int N = 0;
string first = "";

void init(void) {
	first = "";
}

void read(void) {
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		string cur = "";
		cin >> cur;
		first += cur;
	}
}

bool ok(string & str) {
	for (int i = 0; i < N; ++i) {
		for (int j = i + 1; j < N; ++j) {
			if ('1' == str[i * N + j]) return false;
		}
	}
	return true;
}

int solve(void) {
	if (ok(first)) {return 0;}
	set < string > nnew;
	map < string, int > d;
	queue < string > q;
	q.push(first);
	nnew.insert(first);
	d[first] = 0;
	while (!q.empty()) {
		string cur = q.front();
		q.pop();
		for (int i = 0; i < N - 1; ++i) {
			string nstr = cur.substr(0, i * N);
			nstr += cur.substr((i + 1) * N, N);
			nstr += cur.substr(i * N, N);
			if (i != N - 2) nstr += cur.substr((i + 2) * N, N * N - (i + 2) * N);
			if (nnew.end() == nnew.find(nstr)) {
				nnew.insert(nstr);
				q.push(nstr);
				d[nstr] = d[cur] + 1;
				if (ok(nstr)) {return d[nstr];}
			}
		}
	}
	assert(false);
	return -1;
}

int main(void) {
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);

	int T = 0;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		printf("Case #%d: ", i + 1);
		init();
		read();
		printf("%d\n", solve());
	}

	return 0;
}
