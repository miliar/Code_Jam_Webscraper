#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;
#define FOR(i, n) for (int i = 0; i < (int) (n); i++)

int opposed[32][32];
int combine[32][32];

void solve(void)
{
	memset(opposed, 0, sizeof(opposed));
	memset(combine, 0, sizeof(combine));
	
	int nc;
	char t[128];
	scanf("%d", &nc);
	FOR(i, nc) {
		scanf("%s", t);
		combine[t[0] - 'A'][t[1] - 'A'] = t[2] - 'A';
		combine[t[1] - 'A'][t[0] - 'A'] = t[2] - 'A';
	}
	int nd;
	scanf("%d", &nd);
	FOR(i, nd) {
		scanf("%s", t);
		opposed[t[0] - 'A'][t[1] - 'A'] = 1;
		opposed[t[1] - 'A'][t[0] - 'A'] = 1;
	}
	//
	int n;
	scanf("%d", &n);
	scanf("%s", t);
	vector<int> l;
	FOR(i, n) {
		int x = t[i] - 'A';
		l.push_back(x);
		int ls = (int) l.size();
		int combo;
		if (ls > 1 && (combo = combine[l[ls - 2]][l[ls - 1]]) != 0) {
			l.pop_back();
			l.pop_back();
			l.push_back(combo);
			continue;
		}
		FOR(i, ls) FOR(j, ls) if (i < j && opposed[l[i]][l[j]]) {
			l.clear();
			ls = 0;
		}
	}
	printf("[");
	FOR(i, l.size()) {
		if (i) printf(", ");
		printf("%c", 'A' + l[i]);
	}
	printf("]\n");
}

int main(void)
{
	int T;
	scanf("%d", &T);
	FOR(i, T) {
		printf("Case #%d: ", i+1);
		solve();
	}
	return 0;
}
