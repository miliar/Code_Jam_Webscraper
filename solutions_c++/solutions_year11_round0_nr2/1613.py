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

char ch[256][256];
bool de[256][256];

int solve() {
    for (int i = 0; i < 256; i++) {
        for (int j = 0; j < 256; j++) {
            ch[i][j] = 0;
            de[i][j] = 0;
        }
    }
    int C;
    cin >> C;
    for (int i = 0; i < C; i++) {
        char a, b, c;
        cin >> a >> b >> c;
        ch[a][b] = c;
        ch[b][a] = c;
    }
    int D;
    cin >> D;
    for (int i = 0; i < D; i++) {
        char a, b;
        cin >> a >> b;
        de[a][b] = true;
        de[b][a] = true;
    }
    int n;
    cin >> n;
    vector<char> v;
    for (int i = 0; i < n; i++) {
       char a;
       cin >> a;
       if (v.empty()) {
           v.PB(a);
           continue;
       }
       char b = v.back();
       if (ch[a][b] > 0) v.back() = ch[a][b];
       else {
           bool czy = false;
           for (int i = 0; i < (int) v.size(); i++) {
               if (de[v[i]][a]) czy = true;
           }
           if (czy) v.clear();
           else v.PB(a);
       }
    }
    cout << "[";
    for (int i = 0; i < (int) v.size(); i++) {
        if (i > 0) cout << ", ";
        cout << v[i];
    }
    cout << "]";
}

int main()
{
    ios_base::sync_with_stdio(0) ;
    int te;
    cin >> te;
    for (int u = 1; u <= te; u++) {
        cout << "Case #" << u << ": ";
        solve();
        cout << "\n";
    }
}

