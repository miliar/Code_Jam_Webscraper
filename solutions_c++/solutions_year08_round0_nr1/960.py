#include <cstdio>
#include <iostream>
#include <fstream>
#include <map>
#include <string>
using namespace std;

const char FILEIN[] = "date.in";		// input file
const char FILEOUT[] = "date.out";		// output file
const int MAX_L = 128;					// max length of a search engine's name
const int MAX_M = 1024;					// max number of queries
const int MAX_N = 128;					// max number of search engines

int n;									// number of search engines
int m;									// number of queries
map<string, int> no;					// associates each serch engine with a number
int v[MAX_M];							// holds the queries

int Solve() {
	int ret = 0;						// number of switches needed

	int p = 0;
	while (p < m) {
		int first[MAX_N];
		for (int i = 0; i < n; ++i)
			first[i] = m;
		for (int i = m-1; i >= p; --i)
			first[ v[i] ] = i;

		int best = 0;
		for (int i = 0; i < n; ++i)
			if (first[i] > best)
				best = first[i];
		p = best;
		++ret;
	}

	return m == 0 ? 0 : ret-1;
}

int main() {
	freopen(FILEIN, "r", stdin);
	freopen(FILEOUT, "w", stdout);

	int t;								// number of test cases;
	scanf("%d\n", &t);
	for (int case_no = 1; case_no <= t; ++case_no) {
		scanf("%d\n", &n);

		no.clear();
		for (int i = 0; i < n; ++i) {
			char name[MAX_L];
			fgets(name, MAX_L, stdin);

			no[ string(name) ] = i;
		}

		scanf("%d\n", &m);
		for (int i = 0; i < m; ++i) {
			char name[MAX_L];
			fgets(name, MAX_L, stdin);

			v[i] = no[ string(name) ];
		}

		printf("Case #%d: %d\n", case_no, Solve());
	}
}