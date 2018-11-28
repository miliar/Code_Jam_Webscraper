#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <iomanip>
#include <limits.h>

using namespace std;

#define FOR(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define FORD(i,a,b) for((i)=(a);(i)<=(int)(b);(i)++)

#define MAX_N 100

string table[MAX_N];

#define PEXIT { cout << "Impossible" << endl; return 0; }

int solve(int test)
{
	int r, c;
	int i, j;
	int result = 0;
	string line;

	cout << setiosflags(ios::fixed) << setprecision(10);
	
	cout << "Case #" << test << ": " << endl;

	cin >> r >> c;

	FOR(i, r) {
		cin >> table[i];
	}

	FOR(i, r) {
		FOR(j, c) {
			if (table[i][j] == '#') {
				if (j == c-1)
					PEXIT;
				if (table[i][j+1] == '.')
					PEXIT;
				table[i][j] = '/';
				table[i][j+1] = '\\';
				if (i == r-1)
					PEXIT;
				if (table[i+1][j] == '.')
					PEXIT;
				table[i+1][j] = '\\';
				if (table[i+1][j+1] == '.')
					PEXIT;
				table[i+1][j+1] = '/';
			}
		}
	}

	FOR(i, r) {
		cout << table[i] << endl;
	}

	return 0;
}

int main()
{
	int cases = 0;
	int i;

	cin >> cases;

	FOR(i, cases) {
		solve(i + 1);
	}
	
	return 0;
}
