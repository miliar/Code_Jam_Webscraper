#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef int ret_t;

class Solver {
public:
    ret_t solve(int n, int K, int B, int T, vector<int> x, vector<int> v) {
        vector<bool> canReach(n);
        int swaps = 0;
        int saved = 0;
        if (K == 0)
            return 0;
        for (int i = n - 1; i >= 0; --i) {
            canReach[i] = (x[i] + T * v[i] >= B);
            if (canReach[i]) {
                for (int j = i + 1; j < n; ++j)
                    if (!canReach[j])
                        ++swaps;
                ++saved;
                if (saved >= K)
                    return swaps;
            }
        }
        return -1;
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
        int n, K, B, T;
        {
            stringstream A(s);
            A >> n >> K >> B >> T;
        }
        vector<int> x(n);
        vector<int> v(n);
        getline(cin, s);
        {
            stringstream A(s);
            for (int i = 0; i < n; ++i)
                A >> x[i];
        }
        getline(cin, s);
        {
            stringstream A(s);
            for (int i = 0; i < n; ++i)
                A >> v[i];
        }
        ret_t ret = solver.solve(n, K, B, T, x, v);

        // *** give output ***
        if (ret >= 0)
            cout << "Case #" << no << ": " << ret << endl; // one line
        else
            cout << "Case #" << no << ": IMPOSSIBLE" << endl; // one line
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
