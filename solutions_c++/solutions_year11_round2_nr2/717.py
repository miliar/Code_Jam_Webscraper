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

const int MAXN = 25;
const double eps = 1e-7;

int cc;
int n, d;
int v[MAXN];
double p[MAXN];
double lo, hi, adj;

bool check(double m) {
    double a = p[0] - m, b;
    int i = 0, j = 1;
    if (j >= v[i]) {
        i++;
        j = 0;
    }
    while (i < n) {
        if (p[i] - m < a + d) {
            b = a + d;
            if (fabs(p[i] - b) > m) return false;
        } else {
            b = p[i] - m;
        }
        j++;
        swap(a, b);
        if (j >= v[i]) {
            i++;
            j = 0;
        }
    }
    return true;
}

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
    scanf("%d", &cc);
    for (int cas = 1; cas <= cc; cas++) {
        lo = hi = 0;
        scanf("%d%d", &n, &d);
        for (int i = 0, a, b; i < n; i++) {
            cin >> p[i] >> v[i];
            hi += v[i];
        }
        hi *= 100;
        adj = (hi - lo) / 2;
        while (adj > eps) {
            if (check(lo + adj) == false) lo += adj;
            else hi -= adj;
            adj /= 2;
        }
        cout << "Case #" << cas << ": ";
        cout << lo << endl;
    }
	return 0;
}