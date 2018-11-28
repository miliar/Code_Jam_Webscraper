#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long ent;
typedef vector<ent> Vi;
typedef vector<Vi> Mi;

const ent INF = 1000000000000000LL;

ent tree[1000000];
ent vec[1000000];
int N, M;

Mi calc;

ent f(int n, int m, int e, int d) {
    if (e + 1 == d) {
        if (m >= vec[e] and m >= vec[d]) return 0;
        if (m + 1 >= vec[e] and m + 1 >= vec[d]) return tree[n];
        return INF;
    }
    if (calc[n][m] != -1) return calc[n][m];
    ent na = tree[n] + f(2*n, m + 1, e, (e + d)/2) + f(2*n + 1, m + 1, (e + d)/2 + 1, d);
    ent nb = f(2*n, m, e, (e + d)/2) + f(2*n + 1, m, (e + d)/2 + 1, d);
//     cerr << n << ' ' << na << ' ' << nb << endl;
    return calc[n][m] = min(na, nb);
}

int main() {
    int tcas;
    cin >> tcas;
    for (int cas = 1; cas <= tcas; ++cas) {
        cin >> N;
        M = 1<<N;
        for (int i = 0; i < M; ++i) {
            cin >> vec[i];
            vec[i] = N - vec[i];
        }
        for (int i = N - 1; i >= 0; --i) {
            int p = 1<<i;
            for (int j = 0; j < p; ++j) {
                cin >> tree[p + j];
//                 cerr << "# " << p + j << ' ' << tree[p + j] <<  endl;
            }
        }
//         for (int i = 0; i < M; ++i) cerr << ' ' << vec[i];
//         cerr << endl;
//         for (int i = 1; i < M; ++i) cerr << ' ' << tree[i];
//         cerr << endl;
        calc = Mi(2*M + 3, Vi(N + 3, -1));
        cout << "Case #" << cas << ": " << f(1, 0, 0, M - 1) << endl;
    }
}
