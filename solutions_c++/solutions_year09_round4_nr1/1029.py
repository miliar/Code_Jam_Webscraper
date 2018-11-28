#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef int ret_t;

class Solver {
public:
    ret_t solve(int n, vector<string> m) {
        vector<int> allow(n);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) if (m[i][j] == '1') allow[i] = j;
        }
        int ret = 0;
        /*int todo = n;
        while (todo > 0) {
            int hi = allow[0];
            int no = 1;
            for (int i = 0; i < todo; ++i) if (allow[i] >= hi) {
                if (allow[i] == hi)
                    ++no;
                else
                    no = 1;
                hi = allow[i];
            }
            
        }*/
        while (true) {
            //for (int i = 0; i < n; ++i) cout<<allow[i]; cout<<endl;
            bool ok = true;
            for (int i = 0; i < n; ++i) if (i < allow[i]) {
                ok = false;
                int j = i + 1;
                for (; j < n; ++j) if (allow[j] <= i) {
                    ret += j - i;
                    for (; j > i; --j) swap(allow[j], allow[j-1]);
                    break;
                }
                break;
                /*if (allow[i+1] < allow[i]) {
                    ++ret;
                    swap(allow[i], allow[i+1]);
                    break;
                    }*/
            }
            else if (!ok && i > allow[i] && allow[i-1] > allow[i]) {
                ++ret;
                swap(allow[i], allow[i-1]);
                break;
            }
            if (ok) break;
        }
        /*while (true) {
            bool ok = true;
            for (int i = 0; i < n; ++i) if (i < allow[i]) ok = false;
            if (ok) break;
            int hi = allow[0];
            int at = 0;
            for (int i = 1; i < n; ++i) if (abs(i - allow[i]) > hi) {
                hi = abs(i - allow[i]);
                at = i;
            }
            
            }*/
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
        vector<string> m(n);
        for (int i = 0; i < n; ++i) {
            getline(cin, m[i]);
        }
        ret_t ret = solver.solve(n, m);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
