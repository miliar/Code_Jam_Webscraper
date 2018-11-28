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

VS nextVSn(int n) { VS r; for (int i = 0; i < n; i++) r.push_back(nextS()); return r; }

string I_str(int x) {
    ostringstream s;
    s << x;
    return s.str();
}

string L_str(LL x) {
    ostringstream s;
    s << x;
    return s.str();
}

string D_str(LD x) {
    char buf[1000];
    sprintf(buf, "%.8Lf", x);
    return string(buf);
}

string VI_str(VI x) {
    ostringstream s;
    for (int i = 0; i < x.size(); i++) {
        if (i > 0) s << " ";
        s << x[i] << " ";
    }
    return s.str();
}

string VL_str(VL x) {
    ostringstream s;
    for (int i = 0; i < x.size(); i++) {
        if (i > 0) s << " ";
        s << x[i] << " ";
    }
    return s.str();
}

string VD_str(VD x) {
    ostringstream s;
    char buf[50];
    for (int i = 0; i < x.size(); i++) {
        if (i > 0) s << " ";
        sprintf(buf, "%.8Lf", x[i]);
        s << string(buf);
    }
    return s.str();
}

string VS_str(VS x) {
    ostringstream s;
    for (int i = 0; i < x.size(); i++) {
        if (i > 0) s << " ";
        s << x[i] << " ";
    }
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

string do_single() {
    int R = nextI();
    int C = nextI();
    VS x = nextVSn(R);
    int N = R * C;
    int c = 0;
    for (int i = 0; i < (1 << N); i++) {
        VI prev(N, -1);
        int ok = 1;
        for (int j = 0; j < R; j++) for (int k = 0; k < C; k++) {
            int p = j * C + k;
            int b = ((1 << p) & i) > 0 ? 1 : 0;
            int nextJ;
            int nextK;
            switch (x[j][k]) {
                case '|':
                    nextK = k;
                    nextJ = b ? j + 1 : j - 1;
                    break;
                case '-':
                    nextJ = j;
                    nextK = b ? k + 1 : k - 1;
                    break;
                case '/':
                    nextJ = b ? j + 1 : j - 1;
                    nextK = b ? k - 1 : k + 1;
                    break;
                case '\\':
                    nextJ = b ? j + 1 : j - 1;
                    nextK = b ? k + 1 : k - 1;
                    break;
            }
            if (nextJ < 0) nextJ += R;
            if (nextK < 0) nextK += C;
            if (nextJ >= R) nextJ -=R;
            if (nextK >= C) nextK -=C;
            int nextP = nextJ * C + nextK;
            if (prev[nextP] != -1) ok = 0;
            prev[nextP] = p;
        }
        if (ok) c++;
    }
    return I_str(c);
}

