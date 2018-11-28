#include <algorithm>
#include <cassert>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;
static const double EPS = 1e-8;
static const double PI = 4.0 * atan(1.0);
static const double PI2 = 8.0 * atan(1.0);
typedef long long ll;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int N, K;
		cin >> N >> K;

		string line;
		getline(cin, line);
		vector<string> lines;
		for (int n = 0; n < N; ++n) {
			getline(cin, line);
			lines.push_back(line);
		}

		for (int y = 0; y < N; ++y) {
			int to = N - 1;
			for (int from = N - 1; from >= 0; --from) {
				if (lines[y][from] != '.') {
					swap(lines[y][to], lines[y][from]);
					--to;
				}
			}
		}

		bool red = false;
		bool blue = false;
		const string RED = string(K, 'R');
		const string BLUE = string(K, 'B');

		// ‰¡
		for (int y = 0; y < N; ++y) {
			if (lines[y].find(RED) != string::npos) {
				red = true;
			}
			if (lines[y].find(BLUE) != string::npos) {
				blue = true;
			}
		}

		// c
		for (int x = 0; x < N; ++x) {
			string s;
			for (int y = 0; y < N; ++y) {
				s += lines[y][x];
			}

			if (s.find(RED) != string::npos) {
				red = true;
			}
			if (s.find(BLUE) != string::npos) {
				blue = true;
			}
		}

		// ‰E‰º
		for (int y = -N; y < N; ++y) {
			string s;
			for (int x = 0; x < N; ++x) {
				int yy = x + y;
				if (yy < 0 || N <= yy) {
					continue;
				}

				s += lines[yy][x];
			}

			if (s.find(RED) != string::npos) {
				red = true;
			}
			if (s.find(BLUE) != string::npos) {
				blue = true;
			}
		}

		// ‰Eã
		for (int y = 0; y < 2 * N; ++y) {
			string s;
			for (int x = 0; x < N; ++x) {
				int yy = y - x;
				if (yy < 0 || N <= yy) {
					continue;
				}

				s += lines[yy][x];
			}

			if (s.find(RED) != string::npos) {
				red = true;
			}
			if (s.find(BLUE) != string::npos) {
				blue = true;
			}
		}

		printf("Case #%d: ", t);
		if (red) {
			if (blue) {
				printf("Both\n");
			} else {
				printf("Red\n");
			}
		} else {
			if (blue) {
				printf("Blue\n");
			} else {
				printf("Neither\n");
			}
		}
	}
}
