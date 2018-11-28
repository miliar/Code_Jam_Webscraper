#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
#include <cstdlib>
#include <map>
#include <vector>
#include <string>
#include <cmath>
#include <cassert>

using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef set<int> si;
typedef vector<si> vsi;
typedef vector<vi> vvi;
typedef vector<long long> vl;
typedef vector<pii> vpii;
typedef pair<pii, int> piii;
typedef vector<piii> vpiii;
typedef pair<pii, pii> piiii;
typedef pair<int, double> pid;
typedef pair<pid, pii> pgavno;

double distf(pii a, pii b) {
    return sqrt((a.first * 1. - b.first) * (a.first * 1. - b.first) + (a.second
            * 1. - b.second) * (a.second * 1. - b.second));
}

int dx[] = { -1, 1, 0, 0 };
int dy[] = { 0, 0, -1, 1 };
int n;
vi ans;
vi prior;

vector<vi> curq;

vector<vpii> e;

bool mcmp(int a, int b) {
    return prior[a] < prior[b];
}

int sign(int a) {
    if (a >= 0)
        return 1;
    return -1;
}

int main() {
    int n;
    cin >> n;
    for (int cn = 1; cn <= n; ++cn) {
        int t;
        cin >> t;
        vi v(t);
        int xr = 0;
        int sum = 0;
        int mymin = 10000000;
        printf("Case #%d: ", cn);
        for (int i = 0; i < t; ++i) {
            cin >> v[i];
            xr ^= v[i];
            sum += v[i];
            mymin = min(mymin, v[i]);
        }
        if (xr)
            printf("NO\n");
        else {
            printf("%d\n", sum - mymin);
        }
        //%d\n", cn, ans);
    }
    return 0;
}
