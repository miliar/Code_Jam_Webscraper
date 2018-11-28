#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

typedef vector<double> vd;

double solve(int C, int N) {
    int len = C-N+1;
    vd s(len), t(len), q(len, 1.0);
    s[0] = t[0] = 1.0;
    for (int i=1; i<len; ++i) {
        s[i] = s[i-1]*static_cast<double>(C-i+1)/static_cast<double>(i);
        s[i] *= -1.0;
        t[i] = t[i-1]*static_cast<double>(C-i-N+1)/static_cast<double>(C-i+1);
    }
    static const int plen = 2000;
    vd p(plen, 0.0);
    double res = 0.0;
    for (int i=1; i<plen; ++i) {
        for (int j=0; j<len; ++j) {
            q[j] *= t[j];
            p[i] += s[j]*q[j];
        }
        double pdif = p[i] - p[i-1];
        double term = i*pdif;
        if (i>50 && term <1.0e-9) break;
        res += term;
    }
    return res;
}

int main() {
    int T;
    cin >> T;
    for (int i=0; i<T; ++i) {
        int C, N;
        cin >> C >> N;
        double res = solve(C, N);
        cout << "Case #" << i+1 << ": " << fixed << setprecision(8) << res << "\n";
    }
}
