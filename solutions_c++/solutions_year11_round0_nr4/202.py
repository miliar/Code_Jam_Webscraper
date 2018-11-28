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

double ans_random[1001], ans_whole[1001];

void init() {
	ans_random[0] = ans_random[1] = ans_whole[0] = ans_whole[1] = 0;
	for (int N = 2; N <= 1000; ++N) {
		// wN = 1 + rN
		// rN = (1/N)sum_i (wi + r(N-i))

		// wN = 1 + (1/N)sum_i (wi + r(N-i))
		double sum = 1;
		for (int i = 1; i < N; ++i)
			sum += (ans_whole[i] + ans_random[N - i]) / N;
		ans_whole[N] = sum / (1 - 1.0 / N);
		ans_random[N] = ans_whole[N] - 1;
	}
}

int N, inp[1001], val[1001];

string solve() {
	cin >> N;
	for (int i = 0; i < N; ++i)
		cin >> inp[i];
	copy(inp, inp + N, val);
	sort(val, val + N);
	for (int i = 0; i < N; ++i)
		inp[i] = lower_bound(val, val + N, inp[i]) - val;
	double ans = 0;
	for (int i = 0; i < N; ++i)
		if (inp[i] != -1) {
			int len = 0, k = i;
			while (inp[k] != -1) {
				++len;
				int t = inp[k];
				inp[k] = -1;
				k = t;
			}
			ans += ans_whole[len];
		}
	char buf[1000] = {0};
	snprintf(buf, sizeof(buf), "%.20f", ans);
	return buf;
}

int main(int argc, char* argv[]) {
	init();
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
