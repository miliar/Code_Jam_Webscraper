#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>

using namespace std;

typedef long long LL;
typedef long double LD;

typedef vector <LD> VD;
typedef vector <LL> VL;
typedef vector <string> VS;
typedef vector <int> VI;

typedef vector <VI> VVI;
typedef vector <VL> VVL;
typedef vector <VD> VVD;
typedef vector <VS> VVS;

int    nextI() { int n; cin >> n; return n; }

string nextLine() { string x; getline(cin, x); return x; }

VI nextVIn(int n) { VI r; for (int i = 0; i < n; i++) r.push_back(nextI()); return r; }

string I_str(int x) {
    ostringstream s;
    s << x;
    return s.str();
}

string do_single();

int main(int argc, char *argv[]) {
    int T = nextI();
    nextLine();
    for (int t = 1; t <= T; t++) {
        string res = do_single();
        cout << "Case #" << t << ": " << res << endl;
    }
    return 0;
}

int mm[1050];
VI x;

int straight(int bm, int k) {
    VI y;
    for (int i = 0; i < x.size(); i++) {
        if ((bm & (1 << i))) y.push_back(x[i]);
    }
    if (y.size() < k) return 0;
    for (int i = 1 ; i < y.size(); i++) {
        if (y[i] != y[0] + i) return 0;
    }
    return 1;
}

int check(int bm, int k) {
    if (mm[bm] != -1) return mm[bm];
    if (bm == 0) return 1;
    int res = 0;
    for (int i = 1; i < (1 << x.size()); i++) {
        if ((i & bm) != i) continue;
        if (!straight(i, k)) continue;
        if (check(bm ^ i, k)) {
            res = 1;
            break;
        }
    }
    mm[bm] = res;
    return res;
}

int canDo(int k) {
    for (int i = 0; i < 1050; i++) mm[i] = -1;
    return check((1 << x.size()) - 1, k);
}

string do_single() {
    int N = nextI();
    if (N == 0) {
        return I_str(0);
    }
    x = nextVIn(N);
    sort(x.begin(), x.end());
    for (int i = N; i >= 1; i--)
        if (canDo(i)) return I_str(i);
    return I_str(0);
}











