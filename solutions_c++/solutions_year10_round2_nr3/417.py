#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef int ret_t;

const int MOD = 100003;

int binomt[501][501];
int binom(int n, int k) {
    if (n < 0 || k < 0 || k > n) {
        cerr<<"Bad binom"<<endl;
        return 0;
    }
    return binomt[n][k];
}

class Solver {
public:
    int dp[501][501];
    int calc(int n, int r) {
        if (r == 1)
            return 1;
        if (dp[n][r] >= 0)
            return dp[n][r];
        int ret = 0;
        for (int r2 = max(1, 2*r-n); r2 < r; ++r2) {
            int here = binom(n-r-1, r-r2-1) * calc(r, r2);
            here %= MOD;
            ret += here;
            ret %= MOD;
        }
        //cerr<<'['<<n<<','<<r<<"] = "<<ret<<endl;
        dp[n][r] = ret;
        return ret;
    }
    ret_t solve(int n) {
        int ret = 0;
        for (int r = 1; r < n; ++r) {
            ret += calc(n, r);
            ret %= MOD;
        }
        return ret;
	}
};

int main(int argc, char ** argv) {
    string s;
    int N;
    getline(cin, s);
    {
        stringstream A(s);
        A >> N;
    }
    for (int n = 0; n <= 500; ++n) {
        binomt[n][0] = binomt[n][n] = 1;
        for (int k = 1; k < n; ++k)
            binomt[n][k] = (binomt[n-1][k-1] + binomt[n-1][k]) % MOD;
    }
    Solver solver;
    for (int i = 0; i <= 500; ++i) for (int j = 0; j <= 500; ++j) solver.dp[i][j] = -1;
    for (int no = 1; no <= N; ++no) {
        cerr << "Case " << no << " / " << N << endl;
        // *** get input ***
        getline(cin, s);
        int n;
        {
            stringstream A(s);
            A >> n;
        }
        ret_t ret = solver.solve(n);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
