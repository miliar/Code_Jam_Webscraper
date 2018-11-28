#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <set>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <map>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef vector<pii> vii;

int main() {
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        printf("Case #%d: ", test);
        bool x=false, o=false, e=true;
        vector<string> v(4);
        for (int i = 0; i < 4; ++i) {
            cin >> v[i];
            for (int j = 0; j < 4; ++j)
                if (v[i][j] == '.')
                    e = false;
        }
        for (int i = 0; i < 4; ++i) {
            bool x1=1,x2=1,o1=1,o2=1;
            for (int j = 0; j < 4; ++j) {
                if (v[i][j] == '.') {
                    x1 = o1 = 0;
                }
                if (v[j][i] == '.') {
                    x2 = o2 = 0;
                }
                if (v[i][j] == 'X')
                    o1 = 0;
                if (v[i][j] == 'O')
                    x1 = 0;
                if (v[j][i] == 'X')
                    o2 = 0;
                if (v[j][i] == 'O')
                    x2 = 0;
            }
            if (x1||x2)
                x = 1;
            if (o1||o2)
                o = 1;
        }
        bool x1=1,x2=1,o1=1,o2=1;
        for (int i = 0; i < 4; ++i) {
            if (v[i][i] == '.') {
                x1 = o1 = 0;
            }
            if (v[i][3-i] == '.') {
                x2 = o2 = 0;
            }
            if (v[i][i] == 'X')
                o1 = 0;
            if (v[i][i] == 'O')
                x1 = 0;
            if (v[i][3-i] == 'X')
                o2 = 0;
            if (v[i][3-i] == 'O')
                x2 = 0;
        }
        if (x1||x2)
            x = 1;
        if (o1||o2)
            o = 1;
        if (x) {
            cout << "X won\n";
        } else if (o) {
            cout << "O won\n";
        } else if (e) {
            cout << "Draw\n";
        } else {
            cout << "Game has not completed\n";
        }
    }
    return 0;
}
