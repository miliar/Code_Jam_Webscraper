#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
 
using namespace std;

const int MAXN = 105;

int cc;

int n, s, p;
int t, k;
bool flag;
int res;

int diff(int a, int b, int c) {
    return max(abs(a-b), max(abs(a-c), abs(b-c)));
}

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
    scanf("%d\n", &cc);
    for (int cas = 1; cas <= cc; cas++) {
        res = 0;
        cin >> n >> p >> s;
        for (int i = 0; i < n; i++) {
            cin >> t;
            k = t / 3;
            flag = false;
            for (int a = k - 1; a <= k + 1 && !flag; a++) {
                if (a < 0 || a > 10) continue;
                for (int b = a - 1; b <= a + 1 && !flag; b++) {
                    if (b < 0 || b > 10) continue;
                    for (int c = a - 1; c <= a + 1 && !flag; c++) {
                        if (c < 0 || c > 10) continue;
                        if (a + b + c == t && max(a, max(b, c)) >= s) {
                            if (diff(a, b, c) <= 1) {
                                res++;
                                flag = true;
                            }
                        }
                    }
                }
            }
            for (int a = k - 2; a <= k + 2 && !flag; a++) {
                if (a < 0 || a > 10) continue;
                for (int b = a - 2; b <= a + 2 && !flag; b++) {
                    if (b < 0 || b > 10) continue;
                    for (int c = a - 2; c <= a + 2 && !flag; c++) {
                        if (c < 0 || c > 10) continue;
                        if (a + b + c == t && max(a, max(b, c)) >= s) {
                            if (diff(a, b, c) == 2 && p > 0) {
                                res++;
                                p--;
                                flag = true;
                            }
                        }
                    }
                }
            }
        }
        cout << "Case #" << cas << ": " << res << endl;
    }
	return 0;
}