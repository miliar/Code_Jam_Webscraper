#include <iostream>
using namespace std;

// int M[100], C[100][100];
// 
// int der(int n) {
//     if (n == 0) return 1;
//     if (n == 1) return 0;
//     if (M[n] == -1) {
//         M[n] = (n - 1)*(der(n - 1) + der(n - 2));
//     }
//     return M[n];
// }
// 
// int combi(int n, int k) {
//     if (n == k or k == 0) return 1;
//     if (C[n][k] == -1) {
//         C[n][k] = combi(n - 1, k - 1) + combi(n - 1, k);
//     }
//     return C[n][k];
// }
// 
// double f(int n) {
//     if (n == 0) return 0;
//     if (n == 1) return 0;
//     double fact = tgamma(n + 1);
//     double res = 0;
//     for (int i = 1; i <= n; ++i) {
//         res += double(combi(n, i))*der(n - i)*(1 + f(n - i));
//     }
//     res += der(n);
//     res /= (fact - der(n));
//     return res;
// }
// 
// int main() {
//     memset(M, -1, sizeof(M));
//     memset(C, -1, sizeof(C));
//     int n;
//     while (cin >> n) cout << f(n) << endl;
// }

int main() {
    cout.setf(ios::fixed);
    cout.precision(7);
    int casos;
    cin >> casos;
    for (int cas = 1; cas <= casos; ++cas) {
        int n;
        cin >> n;
        int bad = 0;
        for (int i = 1; i <= n; ++i) {
            int a;
            cin >> a;
            if (a != i) ++bad;
        }
        cout << "Case #" << cas << ": ";
        cout << double(bad) << endl;
    }
}