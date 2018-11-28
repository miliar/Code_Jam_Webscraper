#include <vector>
#include <string>
#include <map>
#include <fstream>
#include <sstream>
using namespace std;

const int INF = 1000000000;

ifstream in("A.in");
ofstream out("A.out");

vector <string> S, Q;
map <string, int> M;
int A[1005][105];

void read() {
    int cnt;
    char s[105], tmp[10];
    in.getline(tmp, 10);
    istringstream *s_in = new istringstream(tmp);
    *s_in >> cnt;
    S.resize(cnt);
    M.clear();
    for(int i = 0; i < cnt; ++i) {
        in.getline(s, 105);
        S[i] = string(s);
        M[S[i]] = i;
    }
    delete s_in;

    in.getline(tmp, 10);
    s_in = new istringstream(tmp);
    *s_in >> cnt;
    Q.resize(cnt);
    for(int i = 0; i < cnt; ++i) {
        in.getline(s, 105);
        Q[i] = string(s);
    }
    delete s_in;
}

void solve() {
    for(size_t i = 0; i < Q.size(); ++i) {
        map <string, int> :: iterator it = M.find(Q[i]);
        int p = (it == M.end() ? -1 : it->second);
        for(size_t j = 0; j < S.size(); ++j) {
            if(p == j) {
                A[i][j] = INF;
                continue;
            }
            if(!i)
                A[i][j] = 0;
            else {
                A[i][j] = A[i - 1][j];
                for(int k = 0; k < S.size(); ++k)
                    A[i][j] = min(A[i][j], A[i - 1][k] + 1);
            }
        }
    }
}


int main() {
    int T, case_cnt = 1; char tmp[10];
    in.getline(tmp, 10);
    istringstream s_in(tmp);
    for(s_in >> T; T--; ++case_cnt) {
        read();
        solve();
        int val = INF;
        for(size_t i = 0; i < S.size(); ++i)
            val = min(val, A[Q.size() - 1][i]);
        out << "Case #" << case_cnt << ": " << val;
        if(T)
            out << "\n";
    }
    return 0;
}
