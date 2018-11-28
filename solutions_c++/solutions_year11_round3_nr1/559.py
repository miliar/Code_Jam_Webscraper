#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stack>
#include <queue>
#include <cmath>
#include <string>
#include <string.h>
using namespace std;

typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<VVI> VVVI;
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef vector<VVB> VVVB;
typedef vector<ll> VL;
typedef vector<VL> VVL;
typedef vector<VVL> VVVL;
typedef vector<char> VC;
typedef vector<VC> VVC;
typedef vector<VVC> VVVC;
typedef vector<string> VS;
typedef vector<VS> VVS;
typedef vector<VVS> VVVS;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<double> VD;
typedef vector<VD> VVD;
const int INF = 1000000000;

int arrf[] = {0, 0, 1, 1};
int arrc[] = {0, 1, 0, 1};

string out = "/\\\\/";

int main() {
    int casos;
    cin >> casos;
    for (int cas = 1; cas <= casos; ++cas) {
        int n, m;
        cin >> n >> m;
        VVC M(n, VC(m));
        bool can = true;
        for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j) cin >> M[i][j];
        for (int i = 0; i < n and can; ++i) {
            for (int j = 0; j < m and can; ++j) {
                if (M[i][j] != '#') continue;
                bool ok = true;
                for (int d = 0; d < 4 and ok; ++d) {
                    int ni = i + arrf[d], nj = j + arrc[d];
                    if (ni >= n or ni < 0 or nj >= m or nj < 0 or M[ni][nj] != '#') ok = false;
                    else M[ni][nj] = out[d];
                }
                if (not ok) can = false;
            }
        }
        cout << "Case #" << cas << ":" << endl;
        if (can) {
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < m; ++j) cout << M[i][j];
                cout << endl;
            }
        }
        else cout << "Impossible" << endl;
    }
}
