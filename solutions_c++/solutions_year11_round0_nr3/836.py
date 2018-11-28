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
        int total_xor = 0, min_element = 1e6, sum_all = 0;
        for (int i = 0; i < n; ++i) {
            int x;
            cin >> x;
            sum_all += x;
            total_xor ^= x;
            min_element = min(min_element, x);
        }
        stringstream result;
        if (total_xor) {
            result << "NO";
        }
        else {
            result << (sum_all - min_element);
        }
        printf("Case #%d: %s\n", test, result.str().c_str());
    }
	return 0;
}
