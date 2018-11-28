#include <iostream>
#include <deque>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)

int N, M;
string mm[105];
string dict[105];
string list[15];
int vv[105];

int doit(int idx1, int idx2) {
    REP(i,N) mm[i] = dict[i];
    int ret = 0;
    string str = mm[idx1];
    string lst = list[idx2];
    memset(vv, 0, sizeof(vv));
    REP(i,N) {
        if (mm[i].length() != str.length()) {
            vv[i] = 1;
        }
    }
    REP(i,26) {
        char ch = lst[i];
        bool found = false;
        REP(j,N) {
            if (vv[j] == 1) continue;
            if (mm[j].find(ch) != string::npos) {
                found = true;
                break;
            }
        }
        if (!found) continue;

        if (str.find(ch) == string::npos) {
            ++ret;
            REP(j,N) {
                if (mm[j].find(ch) != string::npos) {
                    vv[j] = 1;
                }
            }
        } else {
            REP(j,str.length()) {
                if (str[j] == ch) {
                    REP(k,N) {
                        if (k == idx1) continue;
                        if (vv[k] == 1) continue;
                        if (mm[k][j] != ch) {
                            vv[k] = 1;
                        } else {
                            mm[k][j] = '_';
                        }
                    }
                }
            }
            REP(k,N) {
                if (k == idx1) continue;
                if (vv[k] == 1) continue;
                if (mm[k].find(ch) != string::npos) {
                    vv[k] = 1;
                }
            }
        }
    }

    return ret;
}

void run() {
    cin >> N >> M;
    REP(i,N) cin >> dict[i];
    REP(i,M) cin >> list[i];
    REP(i,M) {
        int pt = -1;
        string wd = "";
        REP(j,N) {
            int tp = doit(j, i);
            if (tp > pt) {
                pt = tp;
                wd = dict[j];
            }
        }
        if (i) cout << " ";
        cout << wd;
    }
    cout << endl;
}

int main() {
    int kase;
    cin >> kase;
    FOR(k,1,kase) {
        cout << "Case #" << k << ": ";
        run();
    }
    return 0;
}
