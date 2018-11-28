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

const int MAX = 50;

int N, K, B, T;
vector<int> X;
vector<int> V;

int bestTimes[MAX];

int solve()
{
	for (int i = 0; i < N; i++) {
		bestTimes[i] = (B - X[i] - 1) / V[i] + 1;
	}

	int count = 0;

	for (int i = 0; i < N; i++) {
		if (bestTimes[i] <= T) {
			count++;
		}
	}

	if (count < K) {
		return -1;
	}

	int ret = 0;

	int cur = 0;

	for (int i = N - 1; i >= 0; i--) {
		if (bestTimes[i] <= T) {
		    for (int j = i + 1; j < N; j++) {
				if (bestTimes[j] > T) {
					ret++;
				}
		    }
			cur++;
		}

		if (cur == K) break;
	}

	return ret;
}

int main()
{
//	ifstream input("B-small.in");
//	ifstream input("B-small-attempt1.in");
	ifstream input("B-large.in");

//	ofstream output("B-small.out", ios::out);
//	ofstream output("B-small-attempt1.out", ios::out);
	ofstream output("B-large.out", ios::out);

	int C;

	input >> C;

	for (int t = 1; t <= C; t++) {
		input >> N >> K >> B >> T;
		X.clear();
		V.clear();

		for (int i = 0; i < N; i++) {
			int x;

			input >> x;
			X.push_back(x);
		}

		for (int i = 0; i < N; i++) {
			int v;

			input >> v;
			V.push_back(v);
		}

		int ret = solve();

		cout << "Case #" << t << ": ";
		output << "Case #" << t << ": ";

		if (ret == -1) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			cout << ret << endl;
		}

		if (ret == -1) {
			output << "IMPOSSIBLE" << endl;
		} else {
			output << ret << endl;
		}
	}
}
