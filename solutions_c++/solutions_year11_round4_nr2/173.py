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
string nextS() { string x; cin >> x; return x; }

string nextLine() { string x; getline(cin, x); return x; }

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

string do_single() {
    int R = nextI();
    int C = nextI();
    int D = nextI();
    LL p[510][510];
    LL w[510][510];
    LL wh[510][510];
    LL wv[510][510];
    nextLine();
    VS ww;
    for (int i = 0; i < 510; i++) for (int j = 0; j < 510; j++) {
        p[i][j] = 0;
        w[i][j] = 0;
        wh[i][j] = 0;
        wv[i][j] = 0;
    }
    for (int i = 0; i < R; i++) ww.push_back(nextS());
    for (int i = 1; i <= R; i++) for (int j = 1; j <= C; j++) {
        p[i][j] = ww[i - 1][j - 1] - '0';
        w[i][j] = ww[i - 1][j - 1] - '0';
        wh[i][j] = j * (ww[i - 1][j - 1] - '0');
        wv[i][j] = i * (ww[i - 1][j - 1] - '0');
    }
    for (int i = 1; i <= R; i++) for (int j = 1; j <= C; j++) {
        w[i][j] += w[i - 1][j] + w[i][j - 1] - w[i - 1][j - 1];
        wh[i][j] += wh[i - 1][j] + wh[i][j - 1] - wh[i - 1][j - 1];
        wv[i][j] += wv[i - 1][j] + wv[i][j - 1] - wv[i - 1][j - 1];
    }
    int n = C;
    if (R < C) n = R;
    for (int K = n; K >= 3; K--) {
        for (int i = 0; i + K <= R; i++) for (int j = 0; j + K <= C; j++) {
            LL h = wh[i + K][j + K] + wh[i][j] - wh[i + K][j] - wh[i][j + K];
            LL v = wv[i + K][j + K] + wv[i][j] - wv[i + K][j] - wv[i][j + K];
            LL t = w[i + K][j + K] + w[i][j] - w[i + K][j] - w[i][j + K];
            h -= p[i + 1][j + 1] * (j + 1)
               + p[i + K][j + 1] * (j + 1)
               + p[i + 1][j + K] * (j + K)
               + p[i + K][j + K] * (j + K);
            v -= p[i + 1][j + 1] * (i + 1)
               + p[i + K][j + 1] * (i + K)
               + p[i + 1][j + K] * (i + 1)
               + p[i + K][j + K] * (i + K);
            t -= p[i + 1][j + 1]
               + p[i + K][j + 1]
               + p[i + 1][j + K]
               + p[i + K][j + K];
            if (t * (2 * j + K + 1) == h * 2 && t * (2 * i + K + 1) == v *  2) {
                char buf[500];
                sprintf(buf, "%d", K);
                return string(buf);
            }
        }
    }
    return "IMPOSSIBLE";
}

