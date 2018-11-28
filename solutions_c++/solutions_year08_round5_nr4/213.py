#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

#define mset(c, val) memset((c), (val), sizeof((c)))
#define all(v) v.begin(), v.end()
#define INF 1000000000
#define EPS 1e-10

#define MOD 10007

typedef vector<int> vi;
typedef long long lint;

	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int test, tnum;

	bool rock[128][128];
	int memo[128][128];

	int n, m, r;

	int f(int i, int j) {
		if (i < 0) return 0;
		if (j < 0) return 0;
		if (rock[i][j]) return 0;

		int &res = memo[i][j];
		if (res < 0) {
			res = (f(i - 2, j - 1) + f(i - 1, j - 2)) % MOD;
		}

		return res;
	}

int main()
{
    fin >> tnum;
	for (test = 0; test < tnum; test++) {
		mset(rock, false);
		mset(memo, -1);

		fin >> n >> m >> r;
		for (int k = 0; k < r; k++) {
			int i, j;
			fin >> i >> j;
			rock[i - 1][j - 1] = true;
		}

		memo[0][0] = 1;
		fout << "Case #" << (test + 1) << ": " << f(n - 1, m - 1) << endl;
	}
	return 0;
}
