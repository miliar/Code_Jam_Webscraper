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

const char NO[] = "Impossible";

string solve() {
	int R, C;
	cin >> R >> C;
	vector<string> b(R);
	for (int i = 0; i < R; ++i)
		cin >> b[i];
	for (int i = 0; i < R; ++i)
		for (int j = 0; j < C; ++j)
			if (b[i][j] == '#') {
				if (i + 1 >= R || j + 1 >= C || b[i + 1][j] != '#'
						|| b[i][j + 1] != '#' || b[i + 1][j + 1] != '#')
					return NO;
				b[i][j] = b[i + 1][j + 1] = '/';
				b[i + 1][j] = b[i][j + 1] = '\\';
			}
	string ans;
	ans.reserve(R * C + R + 1);
	for (int i = 0; i < R; ++i) {
		if (i) ans += '\n';
		ans += b[i];
	}
	return ans;
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
            cout << "Case #" << cc + 1 << ":" << endl << solve() << endl;
    return 0;
}
