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
typedef vector<double> VD;
typedef vector<VD> VVD;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
const int INF = 1000000000;

int main() {
    cout.setf(ios::fixed);
    cout.precision(10);
    int casos;
    cin >> casos;
    for (int cas = 1; cas <= casos; ++cas) {
        cout << "Case #" << cas << ":" << endl;
        int n;
        cin >> n;
        VVC M(n, VC(n));
        VI wins(n, 0), games(n, 0);
        VVD wout(n, VD(n, 0));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                cin >> M[i][j];
                if (M[i][j] != '.') {
                    if (M[i][j] == '1') ++wins[i];
                    ++games[i];
                }
            }
            for (int j = 0; j < n; ++j) {
                if (M[i][j] == '.') wout[i][j] = double(wins[i])/games[i];
                else if (M[i][j] == '1') wout[i][j] = double(wins[i] - 1)/(games[i] - 1);
                else wout[i][j] = double(wins[i])/(games[i] - 1);
            }
        }
        // owp
        VD owp(n, 0);
        for (int i = 0; i < n; ++i) {
            int cnt = 0;
            for (int j = 0; j < n; ++j) {
                if (M[i][j] == '.') continue; //not played
                owp[i] += wout[j][i];
                ++cnt;
            }
            owp[i] /= double(cnt);
        }
        for (int i = 0; i < n; ++i) {
            double res = 0.25*double(wins[i])/games[i] + 0.5*owp[i];
            double aux = 0;
            int cnt = 0;
            for (int j = 0; j < n; ++j) {
                if (M[i][j] == '.') continue;
                aux += owp[j];
                ++cnt;
            }
            res += 0.25*aux/double(cnt);
            cout << res << endl;
        }
    }
}
