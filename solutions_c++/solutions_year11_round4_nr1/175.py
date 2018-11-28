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
int    nextLD() { LD n; cin >> n; return n; }

string do_single();

int main(int argc, char *argv[]) {
    int T = nextI();
    for (int t = 1; t <= T; t++) {
        string res = do_single();
        cout << "Case #" << t << ": " << res << endl;
    }
    return 0;
}

string do_single() {
    int X = nextLD();
    LD S = nextLD();
    LD R = nextLD();
    LD t = nextLD();
    int N = nextI();
    vector <pair <int, int> > ww;
    int empty = X;
    for (int i = 0; i < N; i++) {
        int from = nextI();
        int to = nextI();
        int w = nextI();
        int len = to - from;
        ww.push_back(make_pair(w, len));
        empty -= len;
    }
    ww.push_back(make_pair(0, empty));
    sort(ww.begin(), ww.end());
    long double total = 0.0;
    for (int i = 0; i < ww.size(); i++) {
        int w = ww[i].first;
        int x = ww[i].second;
        long double needRun = x / (R + w);
        if (needRun <= t) {
            t -= needRun;
            total += needRun;
        } else if (t > 0) {
            long double distRun = t * (R + w);
            total += t + (x - distRun) / (S + w);
            t = 0;
        } else {
            total += x / (S + w);
        }
    }
    char buf[1000];
    sprintf(buf, "%.8Lf", total);
    return string(buf);
}






























