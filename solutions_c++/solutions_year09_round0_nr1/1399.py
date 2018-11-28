#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef int ret_t;

class Solver {
public:
    ret_t solve(vector<string> dict, string msg) {
        int ret = 0;
        for (int i = 0; i < dict.size(); ++i) {
            bool ok = true;
            string w = dict[i];
            int p = 0;
            for (int j = 0; j < w.size(); ++j) {
                if (msg[p] == w[j]) {
                    ++p;
                }
                else if (msg[p] != '(') {
                    ok = false;
                    break;
                }
                else {
                    bool here = false;
                    for (++p; msg[p] != ')'; ++p) {
                        if (msg[p] == w[j]) here = true;
                    }
                    ++p;
                    if (!here) {
                        ok = false;
                        break;
                    }
                }
            }
            if (ok) ++ret;
        }
        return ret;
	}
};

int main(int argc, char ** argv) {
    string s;
    int N;
    int L, D;
    getline(cin, s);
    {
        stringstream A(s);
        A >> L >> D >> N;
    }
    vector<string> dict(D);
    for (int no = 1; no <= D; ++no) {
        getline(cin, s);
        stringstream A(s);
        A >> dict[no-1];
        //cerr << no << ". " << dict[no-1] << endl;
    }
    for (int no = 1; no <= N; ++no) {
        cerr << "Case " << no << " / " << N << endl;
        Solver solver;
        // *** get input ***
        getline(cin, s);
        string a;
        {
            stringstream A(s);
            A >> a;
        }
        ret_t ret = solver.solve(dict, a);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
