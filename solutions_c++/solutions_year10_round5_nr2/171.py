#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

typedef long long ent;
typedef vector<int> Vi;
typedef vector<Vi> Mi;

const int INF = 1000000000;
const ent INFF = 4000000000000000000LL;

int v[1000];
Mi calc;
int f(int n, int m) {
    if (calc[n][m] != -1) return calc[n][m];
    if (m == 0) return 0;
    if (n == 0) return INF;
    int mini = INF;
    for (int i = m/v[n - 1]; i >= 0; --i)
        mini = min(mini, i + f(n - 1, m - i*v[n - 1]));
    return calc[n][m] = mini;
}

int main() {
    int tcas;
    cin >> tcas;
    for (int cas = 1; cas <= tcas; ++cas) {
        cerr << "CAS " << cas << endl;
        ent m;
        int n;
        cin >> m >> n;
        for (int i = 0; i < n; ++i) cin >> v[i];
        sort(v, v + n);
        ent mini = INFF;
//         cerr << m/v[n - 1] << endl;
//         cerr << m - (m/v[n - 1])*v[n - 1] << endl;
//         cerr << "OK" << endl;
        calc = Mi(n + 1, Vi(11200, -1));
        for (ent i = m/v[n - 1]; m - i*v[n - 1] <= 11111 /*and mini == INFF*/; --i) {
//             cerr << "OK" << endl;
//             cerr << i << endl;
            int r = f(n - 1, m - i*v[n - 1]);
            if (r < INF) mini = min(mini, i + r);
        }
//         int a, b;
//         while (cin >> a >> b) {
//             cerr << f(a, b) << endl;
//         }
        cout << "Case #" << cas << ": ";
        if (mini < INFF) cout << mini << endl;
        else cout << "IMPOSSIBLE" << endl;
    }
}
