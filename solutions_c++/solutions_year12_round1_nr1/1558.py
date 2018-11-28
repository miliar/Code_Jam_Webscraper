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

int cc;

#define MAXA 5

int a, b;
double p[MAXA], pp, res, sres;

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
    scanf("%d\n", &cc);
    for (int cas = 1; cas <= cc; cas++) {
        cin >> a >> b;
        for (int i = 0; i < a; i++) cin >> p[a - i - 1];
        // Enter right away
        res = b + 2.0;
        for (int i = 0; i <= a; i++) {
            // Backspace i times
            for (int j = 0; j < a; j++) {
                sres = 0.0;
                for (int k = (1 << (a)) - 1; k >= 0; k--) {
                    pp = 1.0;
                    for (int z = 0; z < a; z++) {
                        if ((k >> z) & 1) pp *= 1 - p[z]; else pp *= p[z];
                    }
                    if ((k >> i) > 0) { // Still a mistake
                        sres += pp * (b - (a - i) + i + 1 + b + 1);
                    } else {
                        sres += pp * (b - (a - i) + i + 1);
                    }
                }
                res = min(res, sres);
            }
        }
        cout << setprecision(7);
        cout << fixed << "Case #" << cas << ": " << res << endl;
    }
	return 0;
}