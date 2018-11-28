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

bool isIN(int i, int j, int size) {
    return 0 <= i && i < size && 0 <= j && j < size;
}

bool check(vector<string> &w, char c, int K) {
    int size = w.size();
    
    const int di[8] = {-1, -1, -1, 0, 1, 1, 1, 0};
    const int dj[8] = {-1, 0, 1, 1, 1, 0, -1, -1};
    REP(i, size) REP(j, size) if (w[i][j] == c) {
        REP(k, 8) {
            int ii = i;
            int jj = j;
            int count = 0;
            while(isIN(ii, jj, size) && w[ii][jj] == c) {
                ++count;
                ii += di[k];
                jj += dj[k];
            }
            if (count == K)
                return true;
        }
    }
    return false;
}

vector<string> rotate(vector<string> &w) {
    int size = w.size();
    vector<string> ret(size, string(size, '.'));
    REP(j, size) {
        int p = size-1;
        for (int k = size-1; k >= 0; --k) if (w[size-j-1][k] != '.') {
            ret[p--][j] = w[size-j-1][k];
        }
    }
    return ret;
}

string solve(vector<string> &w, int K) {
    vector<string> w2 = rotate(w);
    bool okR = check(w2, 'R', K);
    bool okB = check(w2, 'B', K);
    if (okR && okB)
        return "Both";
    if (okR)
        return "Red";
    if (okB)
        return "Blue";
    return "Neither";
}

int main(void)
{
    int T;
    cin >> T;
    REP(_t, T) {
        int N, K;
        cin >> N >> K;
        vector<string> w(N);
        REP(i, N)
            cin >> w[i];
        cout << "Case #" << _t+1 << ": " << solve(w, K) << endl;
    }
    return 0;
}

