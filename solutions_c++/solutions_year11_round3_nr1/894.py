
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <queue>
#include <string>
#include <vector>
#define fl(var, start, limit) for(var = (start); var < (limit); ++var)
#define fd(var, start, limit) for(unsigned int var = (start); var < (limit); ++var)
#define flz(var, limit) for(var = 0; var < (limit); ++var)
#define fdz(var, limit) for(unsigned int var = 0; var < (limit); ++var)
#define rl(limitVar) unsigned int limitVar; cin >> limitVar;
#define frl(var, limitVar) rl(limitVar); fdz(var, limitVar)
#define fe(tp, it, in) for(tp ::iterator it = (in).begin(); it != (in).end(); ++it)
#define sp << " " <<
using namespace std;
typedef unsigned int ui;
typedef vector<unsigned int> vui;
typedef vector<int> vi;
typedef vector<char> vc;
#define nxt a; cin >> a; return a;
char nc() { char nxt; }
unsigned int nui() { unsigned int nxt; }
int ni() { int nxt; }
float nf() { float nxt; }
double nd() { double nxt; }

void doTestcase() {

    string p[50];
    rl(R); rl(C);

    fdz(i, R) {
        cin >> p[i];
    }

    fdz(i, R) {
        fdz(j, C) {
            if (p[i][j] == '#') {
                if (i > R-2 || j > C-2 || p[i+1][j] != '#' || p[i][j+1] != '#' || p[i+1][j+1] != '#') {
                    cout << endl;
                    cout << "Impossible";
                    return;
                }
                p[i][j] = '/';
                p[i+1][j] = '\\';
                p[i][j+1] = '\\';
                p[i+1][j+1] = '/';
            }
        }
    }

    fdz(i, R) {
        cout << endl;
        fdz(j, C) {
            cout << p[i][j];
        }
    }
}

int main(int argc, char *argv[]) {
    frl(t, tt) {
        cout << "Case #" << t + 1 << ":";
        doTestcase();
        cout << endl;
    }
    return EXIT_SUCCESS;
}

