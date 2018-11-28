#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef int ret_t;

class Solver {
public:
    ret_t solve(int n, int m, vector<string> old, vector<string> make) {
        int ret = 0;
        for (int i = 0; i < m; ++i) {
            //cerr<<"Searching "<<make[i]<<endl;
            string path = "";
            int k = 0;
            while (true) {
                k = make[i].find('/', k + 1);
                if (k == string::npos)
                    path = make[i];
                else
                    path = make[i].substr(0, k);
                bool found = false;
                for (int j = 0; j < old.size(); ++j)
                    if (old[j] == path) {
                        found = true;
                        break;
                    }
                if (!found) {
                    ++ret;
                    old.push_back(path);
                    //cerr<<" making "<<path<<endl;
                }
                if (k == string::npos)
                    break;
            }
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
    for (int no = 1; no <= N; ++no) {
        cerr << "Case " << no << " / " << N << endl;
        Solver solver;
        // *** get input ***
        getline(cin, s);
        int n, m;
        {
            stringstream A(s);
            A >> n >> m;
        }
        vector<string> old(n);
        vector<string> make(m);
        for (int i = 0; i < n; ++i) {
            getline(cin, old[i]);
        }
        for (int i = 0; i < m; ++i) {
            getline(cin, make[i]);
        }
        ret_t ret = solver.solve(n, m, old, make);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
