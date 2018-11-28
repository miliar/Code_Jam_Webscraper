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
        vector<pii> s(t);
        for (int i = 0; i < t; ++i) {
            string ss;
            cin >> ss;
            if (ss == "B")
                s[i].first = 1;
            cin >> s[i].second;
        }
        vi curpos(2, 1);
        int ans = 0;
        for (int i = 0; i < t; ++i) {
            vi needpos(2);
            for (int j = t - 1; j >= i; --j) {
                needpos[s[j].first] = s[j].second;
            }
            int canmove = 1 + abs(needpos[s[i].first] - curpos[s[i].first]);
            int oth = 1 - s[i].first;
            curpos[oth] += sign(needpos[oth] - curpos[oth]) * min(canmove, abs(needpos[oth] - curpos[oth]));
            curpos[s[i].first] = s[i].second;
            ans += canmove;
        }
        printf("Case #%d: %d\n", cn, ans);
    }
    return 0;
}
