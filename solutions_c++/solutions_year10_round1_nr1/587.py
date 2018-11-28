#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <cstdio>
#include <cmath>
#include <queue>
#include <sstream>
#include <map>
#include <set>
#include <stack>
using namespace std;

typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<char> VC;
typedef vector<VI> VVI;
typedef vector<VC> VVC;
typedef vector<bool> VVB;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

const int INF = 1000000000;

int main() {
    int casos;
    cin >> casos;
    for (int z = 1; z <= casos; ++z) {
        int n, tot;
        cin >> n >> tot;
        VVC M(n, VC(n));
        for (int i = 0; i < n; ++i) for (int j = 0; j < n; ++j) cin >> M[i][j];
        for (int i = 0; i < n; ++i) {
            int j = n - 1, k = n - 2;
            ini:
            while (j >= 0 and M[i][j] != '.') --j;
            k = min(k, j - 1);
            while (k >= 0 and M[i][k] == '.') --k;
            if (k >= 0 and j >= 0) swap(M[i][k], M[i][j]);
            if (j >= 0 and k >= 0) goto ini;
        }
        bool r = false, b = false;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (M[i][j] == '.') continue;
                for (int h = 1; h < tot; ++h) {
                    if (i + h >= n or M[i+h][j] != M[i][j]) break;
                    if (h == tot - 1 and M[i][j] == 'R') r = true;
                    else if (h == tot - 1 and M[i][j] == 'B') b = true;
                }
                for (int h = 1; h < tot; ++h) {
                    if (j + h >= n or M[i][j+h] != M[i][j]) break;
                    if (h == tot - 1 and M[i][j] == 'R') r = true;
                    else if (h == tot - 1 and M[i][j] == 'B') b = true;
                }
                for (int h = 1; h < tot; ++h) {
                    if (i + h >= n or j + h >= n or M[i+h][j+h] != M[i][j]) break;
                    if (h == tot - 1 and M[i][j] == 'R') r = true;
                    else if (h == tot - 1 and M[i][j] == 'B') b = true;
                }
                for (int h = 1; h < tot; ++h) {
                    if (i - h < 0 or j + h >= n or M[i-h][j+h] != M[i][j]) break;
                    if (h == tot - 1 and M[i][j] == 'R') r = true;
                    else if (h == tot - 1 and M[i][j] == 'B') b = true;
                }
            }
        }
        cout << "Case #" << z << ": ";
        if (r and b) cout << "Both" << endl;
        else if (not r and not b) cout << "Neither" << endl;
        else if (r) cout << "Red" << endl;
        else cout << "Blue" << endl;
    }
}
