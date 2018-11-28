#pragma comment(linker, "/STACK:256000000")

#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <ctime>
#include <math.h>
#include <vector>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <sstream>

using namespace std;

// #define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define sqr(x) ((x)*(x))
//#define foreach(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();++e)


const double PI = acos(-1.0);
const int INF = 1000000000;
const int MOD = 1000000007;

string solve(const vector<string>& field) {

	for (int i = 0; i < 4; ++i) {
		map<char, int> current;
		for (int j = 0; j < 4; ++j) {
			++current[field[i][j]];
		}

		if (current['X'] == 4 || (current['X'] == 3 && current['T'] == 1)) {
			return "X won";
		}

		if (current['O'] == 4 || (current['O'] == 3 && current['T'] == 1)) {
			return "O won";
		}

		current.clear();
		for (int j = 0; j < 4; ++j) {
			++current[field[j][i]];
		}

		if (current['X'] == 4 || (current['X'] == 3 && current['T'] == 1)) {
			return "X won";
		}

		if (current['O'] == 4 || (current['O'] == 3 && current['T'] == 1)) {
			return "O won";
		}
	}

	map<char, int> current;
	for (int j = 0; j < 4; ++j) {
		++current[field[j][j]];
	}

	if (current['X'] == 4 || (current['X'] == 3 && current['T'] == 1)) {
		return "X won";
	}

	if (current['O'] == 4 || (current['O'] == 3 && current['T'] == 1)) {
		return "O won";
	}

		
	current.clear();
	for (int j = 0; j < 4; ++j) {
		++current[field[3-j][j]];
	}

	if (current['X'] == 4 || (current['X'] == 3 && current['T'] == 1)) {
		return "X won";
	}

	if (current['O'] == 4 || (current['O'] == 3 && current['T'] == 1)) {
		return "O won";
	}


	int free = 0;
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j) {
			free += field[i][j] == '.';
		}

	if (free != 0) {
		return "Game has not completed";
	}

	return "Draw";
}


int main() {

	freopen("in.txt","r", stdin);
	freopen("out.txt", "w", stdout);
 
	int T; cin >> T;
	for (int test = 1; test <= T; ++test) {
		vector<string> field(4);
		for (int i = 0; i < 4; ++i) {
			cin >> field[i];
		}

		printf("Case #%d: %s\n", test, solve(field).c_str());
	}
	
	return 0;
}

// nrg 3