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

string solve(int N, int K)
{
	int v = (1 << N) - 1;

	if (K < v) {
		return "OFF"; 
	}

	K -= v;

	if ((K % (1 << N)) == 0) {
		return "ON";
	} else {
		return "OFF";
	}
}

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
		int N, K;

		input >> N >> K;

		cout << "Case #" << t << ": " << solve(N, K) << endl;
		output << "Case #" << t << ": " << solve(N, K) << endl;
	}
}
