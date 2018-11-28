#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:64000000")
#include <cstdio>
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
#include <bitset>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()
#define debug(x) cerr << #x << ": " << x << endl;

const int INF = ((1 << 31) - 1);
const long long LLINF = (((1LL << 63) - 1LL));
const double eps = 1e-9;
const double PI = 3.14159265358979323846;

typedef long long ll;
typedef pair<int, int> pii;

const string PROBLEM_NAME = "task";

vector<int> g(const string& s) {
    vector<int> res;
    for (int i = 0; i < s.size(); ++i) {
        string f(s);
        rotate(f.begin(), f.begin() + i, f.end());
        if (f[0] == '0')
            continue;
        int x;
        sscanf(f.c_str(), "%d", &x);
        res.push_back(x);
    }
    sort(all(res));
    res.erase(unique(all(res)), res.end());
    return res;
}

int main() {
    freopen((PROBLEM_NAME + ".in").c_str(), "r", stdin);
    freopen((PROBLEM_NAME + ".out").c_str(), "w", stdout);
    //freopen((PROBLEM_NAME + ".err").c_str(), "w", stderr);
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        cout << "Case #" << t + 1 << ": ";
        int res = 0;
        int a, b;
        cerr << t << " ";
        cin >> a >> b;
        for (int i = a; i <= b; ++i) {
            char buf[222];
            sprintf(buf, "%d", i);
            string s(buf);
            vector<int> shifts = g(s);
            for (int j = 0; j < shifts.size(); ++j) {
                int v = shifts[j];
                res += a <= v && v <= b && v > i;
            }
        }
        cout << res<< "\n";
        cerr << 1.0 * clock() / CLOCKS_PER_SEC << " sec.\n";
    }

    return 0;
}