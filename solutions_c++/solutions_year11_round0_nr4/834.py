#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <deque>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <ctime>
#include <sstream>

using namespace std;

#define all(v) (v).begin(), (v).end()

const double PI = 3.1415926535897932384626433832795;
const double EPS = 1e-9;
const int INF = 1000 * 1000;

typedef long long ll;
typedef pair<int, int> pii;


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        cerr << test << endl;
        int n;
        cin >> n;
        vector<int> numbers(n);
        for (int i = 0; i < n; ++i) {
            cin >> numbers[i];
            --numbers[i];
        }
        vector<bool> used(n, false);
        int result = 0;
        for (int i = 0; i < n; ++i) {
            if (used[i]) {
                continue;
            }
            int circle_size = 0, last = i;
            while (!used[last]) {
                used[last] = true;
                last = numbers[last];
                ++circle_size;
            }
            assert(last == i);
            int add = circle_size == 1 ? 0 : circle_size;
            result += add;
        }
        printf("Case #%d: %d\n", test, result);
    }
	return 0;
}
