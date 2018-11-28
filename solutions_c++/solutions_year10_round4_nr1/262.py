#include <cstdio> 
#include <cstdlib> 
#include <cmath> 
#include <cstring> 
#include <climits> 
#include <cfloat> 
#include <map> 
#include <utility> 
#include <set> 
#include <iostream> 
#include <memory> 
#include <string> 
#include <vector> 
#include <algorithm> 
#include <functional> 
#include <sstream> 
#include <complex> 
#include <stack> 
#include <queue> 
#include <numeric>
#include <cassert>

#define FOR(i, min, max) for (int i = (min); i < (max); ++i) 
#define FORE(i, min, max) for (int i = (min); i <= (max); ++i) 
#define REP(i, n) for (int i = 0; i < (n); ++i) 
#define REPV(vec, i) for (int i = 0; i < (int)(vec.size()); ++i) 
#define FOR_EACH(vec, it) for (typeof((vec).begin()) it = (vec).begin(); it != (vec).end(); ++it)

using namespace std; 
static const double EPS = 1e-12; 
typedef long long ll; 

bool can(vector<vector<int> > &w) {
    int size = w.size();
    REP(i, size) REP(j, size) {
        int &a = w[i][j];
        int &b = w[j][i];
        if (a != b && a != -1 && b != -1)
            return false;
//        if (a == -1 && b == -1)
//            a = b = 0;
        if (a == -1)
            a = b;
        if (b == -1)
            b = a;
    }
    REP(i, size) REP(j, size) {
        int &a = w[i][j];
        int &b = w[size-1-j][size-1-i];
//        cerr << "test2:" << a << "," << b << endl;
        if (a != b && a != -1 && b != -1)
            return false;
//        if (a == -1 && b == -1)
//            a = b = 0;
        if (a == -1)
            a = b;
        if (b == -1)
            b = a;
    }

    return true;
}

bool can(const vector<vector<int> > &w_o, int size, int si, int sj) {
    vector<vector<int> > w(size, vector<int>(size, -1));
    REPV(w_o, i) REPV(w_o, j) {
        w[i+si][j+sj] = w_o[i][j];
    }
    return can(w);
}

int solve(vector<vector<int> > &w) {
    int size = w.size();
    int maxSize = 3*size;
    FORE(s, size, maxSize) {
        REP(i, s-size+1) REP(j, s-size+1) if (can(w, s, i, j)) {
            return s*s-size*size;
        }
    }
    assert(0);
    return -1;
}

int main(void)
{
    int T;
    cin >> T;
    REP(_t, T) {
        int k;
        cin >> k;
        string s;
        getline(cin, s); // remove kaigyo
        vector<vector<int> > w(2*k-1);
        REP(i, 2*k-1) {
            getline(cin, s);
            istringstream iss(s);
            int n;
            while(iss >> n)
                w[i].push_back(n);
        }
        vector<vector<int> > input(k, vector<int>(k));
        REP(i, k) REP(j, k) {
            input[i][j] = w[i+j].back();
            w[i+j].pop_back();
        }
        cout << "Case #" << _t+1 << ": " << solve(input) << endl;
    }
    return 0;
}

