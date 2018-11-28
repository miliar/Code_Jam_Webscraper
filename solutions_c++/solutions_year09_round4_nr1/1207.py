#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <stack>
using namespace std;

#define x first
#define y second

typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef vector<ll> VL;
typedef vector<VL> VVL;
typedef vector<char> VC;
typedef vector<VC> VVC;
typedef vector<string> VS;
typedef vector<VS> VVS;
typedef pair<int, int> PII;
const int INF = 1000000000;

int fila(VC& M) {
    int res = 0;
    for (int i = 0; i < M.size(); ++i) {
        if (M[i] == '1') res = i;
    }
    return res;
}

bool buena(VVC& M) {
    for (int i = 0; i < M.size(); ++i) {
        if (fila(M[i]) > i) return false;
    }
    return true;
}

int rec(VVC& M) {
    map<VVC, int> d;
    d[M] = 0;
    queue<VVC> Q;
    Q.push(M);
    while (1) {
        VVC a = Q.front();
        Q.pop();
        int act = d[a];
        if (buena(a)) return d[a];
        for (int i = 0; i + 1 < a.size(); ++i) {
            swap(a[i], a[i + 1]);
            if (not d.count(a)) {
                d[a] = act + 1;
                Q.push(a);
            }
            swap(a[i], a[i + 1]);
        }
    }   
}
            
int main() {
    int k, caso = 1;
    cin >> k;
    while (k--) {
        int n;
        cin >> n;
        VVC M(n, VC(n));
        for (int i = 0 ; i < n; ++i) for (int j = 0; j < n; ++j) cin >> M[i][j];
        cout << "Case #" << caso++ << ": " << rec(M) << endl;
    }
}

