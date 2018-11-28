#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:64000000")
#include <iostream>
#include <vector>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <set>
#include <map>
#include <cassert>
#include <queue>
#include <deque>
#include <stack>
#include <sstream>
#include <cstring>
#include <string>
#include <functional>
#include <numeric>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()

const int INF = ((1 << 31) - 1);
const long long LLINF = (((1LL << 63) - 1LL));
const double eps = 1e-9;
const double PI = 3.14159265358979323846;

typedef long long ll;
long long labs(long long x) {
    if (x < 0)
        return -x;
    return x;
}

const long long MAX = 1000 * 1000 * 1000* 1000LL;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    int tests;
    cin >> tests;
    for (int test = 0; test < tests; ++test) {
        long long lower = -1;
        long long upper = MAX;
        int c, d;
        vector<int> pos;
        cin >> c >> d;
        d *= 2;
        for (int i = 0; i < c; ++i) {
            int x, y;
            scanf("%d%d", &x, &y);
            while(y --> 0) {
                pos.push_back(2 * x);
            }
        }
        sort(all(pos));
        while(lower + 1 < upper) {
            long long median = (lower + upper) >> 1;
            long long bound = MAX + MAX;
            bool ok = true;
            for (int i = pos.size() - 1; ok && i >= 0; --i) {
                long long new_pos = min(pos[i] + median, bound);
                bound = new_pos - d;
                if (labs(new_pos - pos[i]) > median)
                    ok = false;
            }
            if (ok)
                upper = median;
            else
                lower = median;
        }
        if (upper > MAX - 1000LL) {
            cerr << "Oops!\n";
        }
        printf("Case #%d: %lf\n", 1 + test, 0.5 * upper);
    }
	return 0;
}