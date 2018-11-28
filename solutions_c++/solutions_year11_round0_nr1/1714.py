#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cassert>
#include <cstring>
using namespace std;

typedef long long LL ;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;

const int INF = 1000*1000*1000 + 1000;
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

int solve() {
    int n;
    cin >> n;
    VI v;
    for (int i = 0; i < n; i++) {
        int a;
        char c;
        cin >> c >> a;
        if (c == 'O') {
            v.PB(a);
        } else {
            v.PB(-a);
        }
    }
    int ret = 0;
    int p = 1;
    int q = -1;
    int move = 0;
    int f1 = 0;
    int f2 = 0;
    for (int i = 0; i < n; i++) {
        if (v[i] > 0) {
            move = max(0, abs(p - v[i]) - f1) + 1;
            ret += move;
            p = v[i];
            f1 = 0;
            f2 += move;
        }
        else {
            move = max(0, abs(q - v[i]) - f2) + 1;
            ret += move;
            q = v[i];
            f1 += move;
            f2 = 0;
        }
    }
    return ret;
}

int main()
{
    ios_base::sync_with_stdio(0) ;
    int te;
    cin >> te;
    for (int u = 1; u <= te; u++) {
        int ret = solve();
        cout << "Case #" << u << ": " << ret << "\n";
    }
}

