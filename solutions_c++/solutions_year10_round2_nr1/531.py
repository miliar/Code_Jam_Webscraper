#include "stdafx.h"

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

const int MAX = 100;

int N, M;
set<string> L[MAX];

int main()
{
//	ifstream input("A-small.in");
//	ifstream input("A-small-attempt0.in");
	ifstream input("A-large.in");

//	ofstream output("A-small.out", ios::out);
//	ofstream output("A-small-attempt0.out", ios::out);
	ofstream output("A-large.out", ios::out);

	int T;

	input >> T;

	for (int t = 1; t <= T; t++) {
		for (int j = 0; j < MAX; j++) {
			L[j].clear();
		}

		input >> N >> M;

		for (int i = 0; i < N; i++) {
			string path;

			input >> path;

			for (int j = 0; j < path.length(); j++) {
				if (path[j] == '/') {
					path[j] = ' ';
				}
			}

			istringstream iss(path);

			int k = 0;

			string s;
			string prefix = "";

			while (iss >> s) {
				prefix += (s + "/");
				L[k++].insert(prefix);
			}
		}

		int ret = 0;

		for (int j = 0; j < M; j++) {
			string path;

			input >> path;

			for (int j = 0; j < path.length(); j++) {
				if (path[j] == '/') {
					path[j] = ' ';
				}
			}

			istringstream iss(path);

			int k = 0;

			string prefix = "";
			string s;

			while (iss >> s) {
				prefix += (s + "/");
				if (L[k].find(prefix) == L[k].end()) {
					L[k].insert(prefix);
					ret++;
				}
				k++;
			}
		}

		cout << "Case #" << t << ": " << ret << endl;
		output << "Case #" << t << ": " << ret << endl;
	}
}
