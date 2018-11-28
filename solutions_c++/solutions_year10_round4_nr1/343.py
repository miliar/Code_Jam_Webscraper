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
    ret_t solve(int n, vector<string> d) {
        int N = 2*n-1;
        int mincost = 999999;
        vector<bool> horsym(N);
        vector<bool> versym(N);
        for (int i = 0; i < N; ++i) {
            bool sym = true;
            for (int j = 0; j < N; ++j) {
                int j2 = 2*i - j;
                if (j2 >= 0 && j2 < N && j2 != j) {
                    for (int k = 0; k < N; ++k) {
                        if (j < d[k].size() && j2 < d[k].size() && d[k][j] >= '0' && d[k][j2] >= '0' && d[k][j] != d[k][j2]) {
                            sym = false;
                            break;
                        }
                    }
                }
                if (!sym)
                    break;
            }
            horsym[i] = sym;
            //cerr<<(sym?'T':'F');
        }
        //cerr<<endl;
        for (int i = 0; i < N; ++i) {
            bool sym = true;
            for (int j = 0; j < N; ++j) {
                int j2 = 2*i - j;
                if (j2 >= 0 && j2 < N && j2 != j) {
                    for (int k = 0; k < N; ++k) {
                        if (k < d[j].size() && k < d[j2].size() && d[j][k] >= '0' && d[j2][k] >= '0' && d[j][k] != d[j2][k]) {
                            sym = false;
                            break;
                        }
                    }
                }
                if (!sym)
                    break;
            }
            versym[i] = sym;
            //cerr<<(sym?'T':'F');
        }
        //cerr<<endl;
        for (int i = 0; i < N; ++i) {
            if (!horsym[i]) continue;
            for (int j = 0; j < N; ++j) {
                if (!versym[j]) continue;
                int here = n + abs(n-1 - i) + abs(n-1 - j);
                here *= here;
                here -= n*n;
                mincost = min(mincost, here);
            }
        }
        return mincost;
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
        int n;
        {
            stringstream A(s);
            A >> n;
        }
        vector<string> d(2*n-1);
        for (int i = 0; i < 2*n-1; ++i) {
            getline(cin, d[i]);
        }
        ret_t ret = solver.solve(n, d);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
