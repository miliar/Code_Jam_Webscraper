#include <cstdio>
#include <algorithm>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>

#define ALL(s) (s).begin(), (s).end()
#define FOREACH(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define FOR(i, a, b) for (int i = (a); i <= (b); i++)
#define REP(i, a) for (int i = 0; i < a; i++)

#define SZ(x) ((int) (x).size())
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))

using namespace std;

int n;
vector<int> numbers;

void solve() {
	vector<int> numbers2 = vector<int>(numbers);
	sort(ALL(numbers));
	
	int out_of_order = 0;
	
	REP (i, n) {
		if (numbers[i] != numbers2[i]) {
			out_of_order++;
		}
	}
	
	printf("%d.000000", out_of_order);
}

int main(int argc, char ** argv) {
	int ncases;
	cin >> ncases;

	FOR(t, 1, ncases) {
		printf("Case #%d: ", t);
		
		cin >> n;
		numbers = vector<int>(n);
		
		REP (i, n) {
			int e;
			cin >> e;
			numbers[i] = e;
		}
		
		solve();
		
		printf("\n");
	}
}
