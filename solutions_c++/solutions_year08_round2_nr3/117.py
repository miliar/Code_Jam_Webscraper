#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <algorithm>
#include <set>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cassert>
#include <utility>
#include <climits>

using namespace std;

#define EPS 1E-8
#define NMAX 111
#define KMAX 5555

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define all(a) a.begin(), a.end()
#define pb push_back
#define mp make_pair
#define VI vector<int>
#define VS vector<string>

int a[KMAX], b[KMAX];
bool u[KMAX];

map<int, set<int> > ps;

void solve(int tst) {

	int k;
	scanf("%d", &k);

	int n;
	scanf("%d", &n);

	ps.clear();

	forn (i, k) {
		a[i] = i + 1;
		ps[a[i]].insert(i);
	}

	forn (i, n) {
		scanf("%d", &b[i]);
	}

	memset(u, false, sizeof(u));

	int ptr = 0;
	int counter = 1;
	int sz = k;
	while (sz > 1) {
		if (ps[counter].size() > 0) {

			set<int>& poss = ps[counter];

			int ind = *poss.begin();
			ps[counter].erase(ind);

			ps[a[ptr]].erase(ptr);

			swap(a[ind], a[ptr]);			

			if (ind != ptr) 
				ps[a[ind]].insert(ind);

			counter = 1;
			u[ptr] = true;
						
			while (u[ptr]) {
				++ptr;
				if (ptr >= k) ptr -= k;								
			}
			--sz;
			continue;
		}
		++counter;
		++ptr;
		if (ptr >= k) ptr -= k;								
		while (u[ptr]) {
			++ptr;
			if (ptr >= k) ptr -= k;								
		}
	}

	printf("Case #%d:", tst);
	forn (i, n) printf(" %d", a[b[i] - 1]);
	printf("\n");

	cerr << tst << endl;
}

int main() {

	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tst;
	scanf("%d", &tst);

	forn (i, tst) solve(i + 1);

	return 0;
}

