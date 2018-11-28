#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <math.h>
#include <algorithm>
#define fori(n) for (int i = 0; i < n; i++)
#define forj(n) for (int j = 0; j < n; j++)
#define fork(n) for (int k = 0; k < n; k++)
#define MAXL 15
#define MAXD 5000
#define MAXN 500

using namespace std;

string dict[MAXD];
string tokenlist;

char tokens[MAXL][30];
char possibs[30];

int matches = 0;

int L,D,N;

bool ispossib(string curdict) {
	for (int l = 0; l < L; l++) {

		char c = curdict[l];
		bool found = false;
		for (int i = 0; i < possibs[l]; i++) {
			if (tokens[l][i] == c) {
				found = true;
				break;
			}
		}

		if (!found) return false;
	}
	return true;
}

int main() {
	ifstream in("alien.in");
	FILE* out = fopen("alien.out","w");

	in >> L >> D >> N;
	for (int i = 0; i < D; i++) 
		in >> dict[i];

	// Begin Pattern Input
	for (int n = 0; n < N; n++) {
		matches = 0;
		string tokenlist;
		in >> tokenlist;
		cout << tokenlist << endl;

		int pos = 0;
		for (int i = 0; i < L; i++) {
			possibs[i] = 0;

			char c = tokenlist[pos++];
			if (c == '(') {
				while(tokenlist[pos] != ')') {
					tokens[i][possibs[i]++] = tokenlist[pos++];
				}
				pos++;
			} else {
				tokens[i][0] = c;
				possibs[i] = 1;
			}
		}

	/*
		for (int i = 0; i < L; i++) {
			cout << "[";
			for (int j = 0; j < possibs[i]; j++) {
				if (j) cout << " ";
				cout << tokens[i][j];
			}
			cout << "]";
		}
		cout << endl;
	*/

		for (int d = 0; d < D; d++) {
			if (ispossib(dict[d])) {
				cout << "Matched: " << dict[d] << endl;
				matches++;
			}
		}

		printf("Case #%d: %d\n",n+1,matches);
		fprintf(out,"Case #%d: %d\n",n+1,matches);
	}
	
	return 0;
}
