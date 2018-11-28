#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

#define abs(x) ( ((x) < 0) ? (-(x)) : (x) )

int puc[31][11], puc2[31][11];

void rec(int p, vector<int>& v) {
    if (p == 3) {
        int suma = v[0] + v[1] + v[2], maxim = max(v[0], max(v[1], v[2]));
        int maxdif = max(abs(v[0] - v[1]), max(abs(v[0] - v[2]), abs(v[1] - v[2])));
        if (maxdif > 2) return;
        if (maxdif == 2) {
            for (int i = 0; i <= maxim; ++i) puc2[suma][i] = 1;
        }
        else {
            for (int i = 0; i <= maxim; ++i) puc[suma][i] = 1;
        }
        return;
    }
    for (int i = 0; i <= 10; ++i) {
        v[p] = i;
        rec(p + 1, v);
    }
}

int main() {
    memset(puc, 0, sizeof(puc));
    memset(puc2, 0, sizeof(puc2));
    vector<int> aux(3);
    rec(0, aux);
    int casos;
    cin >> casos;
    for (int z = 1; z <= casos; ++z) {
        int n, s, p;
        cin >> n >> s >> p;
        int res = 0;
        for (int i = 0; i < n; ++i) {
            int a;
            cin >> a;
            if (puc[a][p]) ++res;
            else if (puc2[a][p] and s > 0) {
                ++res;
                --s;
            }
        }
        cout << "Case #" << z << ": " << res << endl;
    }
}