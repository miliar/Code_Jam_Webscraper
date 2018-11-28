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

int R, k, N;
vector<int> g;

typedef unsigned long long ull;

ull solve0()
{
	ull sum = 0;

	for (int i = 0; i < g.size(); i++) {
		sum += g[i];
	}

	if (sum <= k) {
		return R * sum;
	}

	int cur = 0;
	int curi = 0;

	ull ret = 0;

	while (cur < R) {
		ull s = 0;

		while (s + g[curi % N] <= k) {
			s += g[curi % N];
			curi = (curi + 1) % N;
		}

		ret += s;
		cur++;
	}

	return ret;
}


ull solve()
{
	ull sum = 0;

	for (int i = 0; i < g.size(); i++) {
		sum += g[i];
	}

	if (sum <= k) {
		return R * sum;
	}

	int cur = 0;
	int curi = 0;

	map<int, int> M;
	map<int, ull> MV;

	M[0] = cur;
	MV[0] = 0; 

	ull ret = 0;

	while (cur < R) {
		ull s = 0;

		while (s + g[curi % N] <= k) {
			s += g[curi % N];
			curi = (curi + 1) % N;
		}

		ret += s;
		cur++;

		if (M.find(curi) == M.end()) {
			M[curi] = cur;
			MV[curi] = ret;
		} else {
			int cycle = cur - M[curi];
			ull cycleValue = ret - MV[curi];

			ret = ret + (ull)((R - cur) / cycle) * cycleValue;
			cur = cur + (ull)((R - cur) / cycle) * cycle;
		}
	}

	return ret;
}

int main()
{
//	ifstream input("C-small.in");
//	ifstream input("C-small-attempt0.in");
	ifstream input("C-large.in");

//	ofstream output("C-small.out", ios::out);
//	ofstream output("C-small-attempt0.out", ios::out);
	ofstream output("C-large.out", ios::out);

	int T;

	input >> T;

	for (int t = 1; t <= T; t++) {
		input >> R >> k >> N;

		int gi;
		g.clear();

		for (int i = 0; i < N; i++) {
			input >> gi;
			g.push_back(gi);
		}

		cout << "Case #" << t << ": " << solve() << endl;
		output << "Case #" << t << ": " << solve() << endl;
	}
}
