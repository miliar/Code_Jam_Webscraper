#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <queue>
#include <stack>
using namespace std;

typedef long long ll;

const int LIM = 500 + 10;

int R, C, D;

struct Sum {
	ll d[LIM][LIM];

	void Clear() {
		for (int i = 0; i <= R; ++i)
			fill(d[i], d[i] + C + 1, 0LL);
	}

	void Set(int i, int j, ll w) {
		d[i + 1][j + 1] = w;
	}

	void Finish() {
		for (int i = 0; i <= R; ++i)
			for (int j = 0; j <= C; ++j) {
				if (i) d[i][j] += d[i - 1][j];
				if (j) d[i][j] += d[i][j - 1];
				if (i && j) d[i][j] -= d[i - 1][j - 1];
			}
	}

	ll operator()(int i1, int j1, int i2, int j2) const {
		return d[i2][j2] - d[i2][j1] - d[i1][j2] + d[i1][j1];
	}

	ll operator()(int i, int j) const {
		return (*this)(i, j, i + 1, j + 1);
	}
};

inline ll GetBlade(const Sum& sum, int i, int j, int z) {
	ll ret = sum(i, j, i + z, j + z);
	ret -= sum(i, j);
	ret -= sum(i, j + z - 1);
	ret -= sum(i + z - 1, j);
	ret -= sum(i + z - 1, j + z - 1);
	return ret;
}

Sum sumW, sumX, sumY;

int solve() {
	cin >> R >> C >> D;
	sumW.Clear();
	sumX.Clear();
	sumY.Clear();
	for (int i = 0; i < R; ++i) {
		string line;
		cin >> line;
		for (int j = 0; j < C; ++j) {
			ll w = line[j] - '0';
			sumW.Set(i, j, w);
			sumX.Set(i, j, w * i);
			sumY.Set(i, j, w * j);
		}
	}
	sumW.Finish();
	sumX.Finish();
	sumY.Finish();
	for (int z = min(R, C); z >= 3; --z) {
		for (int i = 0; i <= R - z; ++i)
			for (int j = 0; j <= C - z; ++j) {
if(z==5&&i==1&&j==1)
cout<<"";
				ll w = GetBlade(sumW, i, j, z);
				ll x = GetBlade(sumX, i, j, z);
				ll y = GetBlade(sumY, i, j, z);
				if (z % 2) {
					// x / w == i + z/2
					if (x == (i + z / 2) * w
							&& y == (j + z / 2) * w)
						return z;
				} else {
					// x / w == i + z/2 - 0.5
					if (x * 2 == (i * 2 + z - 1) * w
							&& y * 2 == (j * 2 + z - 1) * w)
						return z;
				}
			}
	}
	return -1;
}

int main(int argc, char* argv[]) {
    if (argc > 1) {
        char* file_name = argv[1];
        int len = strlen(file_name);
        if (strcmp(file_name + len - 3, ".in") == 0)
            file_name[len - 3] = 0;
        else if (strcmp(file_name + len - 1, ".") == 0)
            file_name[len - 1] = 0;
        freopen((string(file_name) + ".in").c_str(), "r", stdin);
        freopen((string(file_name) + ".out").c_str(), "w", stdout);
    }
    int cc = 0, ccc = 0;
    for (cin >> ccc; cc < ccc; ++cc) {
            cout << "Case #" << cc + 1 << ": ";
		    ll ret = solve();
			if (ret < 0)
				cout << "IMPOSSIBLE" << endl;
			else
				cout << ret << endl;
	}
    return 0;
}
