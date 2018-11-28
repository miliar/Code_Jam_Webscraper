#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
const ll MOD = 10000;

typedef string ret_t;

ll dp[501][20];

class Solver {
public:
    ret_t solve(string s) {
        ll ret;
        string q = "welcome to code jam";
        int n = s.size();
        for (int i = 0; i < n; ++i) for (int j = 0; j < q.size(); ++j) {
            ll h = 0;
            if (i > 0) h += dp[i-1][j];
            if (s[i] == q[j]) {
                if (j == 0)
                    h++;
                else
                    h += dp[i-1][j-1];
            }
            h %= MOD;
            dp[i][j] = h;
            //if (j == 0) cerr<<endl<<s[i]<<' ';
            //cerr<<q[j]<<h<<' ';
        }
        ret = dp[n-1][q.size()-1];
        stringstream A;
        A << ret;
        string ret2 = A.str();
        while (ret2.size() < 4) ret2 = string(1, '0') + ret2;
        return ret2;
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
    for (int no = 1; no <= N; ++no) {
        cerr << "Case " << no << " / " << N << endl;
        Solver solver;
        // *** get input ***
        getline(cin, s);
        ret_t ret = solver.solve(s);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
