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

int     nextI() { int n; cin >> n; return n; }
LL     nextL() { LL n; cin >> n; return n; }

string nextLine() { string x; getline(cin, x); return x; }

int do_single();

int p[1100000];
int main(int argc, char *argv[]) {
    for (int i = 0; i < 1100000; i++) {
        p[i] = 1;
    }
    for (int i = 2; i * i < 1100000; i++) {
        if (p[i]) {
            for (int j = i * i; j < 1100000; j += i) p[j] = 0;
        }
    }
    int T = nextI();
    nextLine();
    for (int t = 1; t <= T; t++) {
        int res = do_single();
        cout << "Case #" << t << ": " << res << endl;
    }
    return 0;
}

int do_single() {
    LL N = nextL();
    if (N == 1) return 0;
    if (N == 2) return 1;
    int r = 1;
    for (int i = 2; i < 1100000; i++) {
        if (p[i]) {
            LL q = (LL)(i);
            if (q * q <= N) {
                LL x = q * q;
                while (x <= N) {
                    r++;
                    x *= q;
                }
            }
            else return r;
        }
    }
    return -1;
}

