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

string solve() {
	int N, t, sum = 0, min = -1, bitsum = 0;
	for (cin >> N; N-- > 0;) {
		cin >> t;
		sum += t;
		if (min == -1 || t < min) min = t;
		bitsum ^= t;
	}
	if (bitsum) return "NO";
	ostringstream ret;
	ret << sum - min;
	return ret.str();
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
    for (cin >> ccc; cc < ccc; ++cc)
            cout << "Case #" << cc + 1 << ": " << solve() << endl;
    return 0;
}
