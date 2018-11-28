#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <valarray>
#include <vector>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

#define DEB  0
#define EPS  1e-10
#define M_PI 3.14159265358979323846

using namespace std;

typedef complex<double> point;
typedef vector<bool> boolary;
typedef vector<int> intary;
typedef vector<string> strary;
typedef vector<intary> graph;
typedef vector<boolary> bgraph;

int N, K;
char tbl[100][100];
char res[100][100];
int move [][2] = {
    {1, 0},
    {0, 1},
    {1, 1},
    {1, -1}
};
bool ans[128];

void output (char tt[][100]) {
    for (int i = 0 ; i < N ; i++) {
        for (int j = 0 ; j < N ; j++) {
            cout << tt[i][j];
        }
        cout << endl;
    }
    cout << endl;
}

void rotate() {
    for (int i = 0 ; i < N ; i++) {
        for (int j = 0 ; j < N ; j++) {
            res[i][j] = '.';
        }
    }

    for (int i = 0 ; i < N ; i++) {
        int y = N - 1;
        for (int j = N - 1 ; j >= 0 ; j--) {
            if (tbl[i][j] != '.') {
                res[y][N - i - 1] = tbl[i][j];
                y--;
            }
        }
    }
}

void check () {
    for (int i = 0 ; i < N ; i++) {
        for (int j = 0 ; j < N ; j++) {
            int t = res[i][j];

            if (t == '.') continue;
            if (ans[t] == true) continue;
            if (ans['R'] and ans['B']) return;

            for (int k = 0 ; k < 4 ; k++) {   
                for (int a = 1 ; a < K ; a++) {
                    int ni = i + move[k][0] * a;
                    int nj = j + move[k][1] * a;

                    if (ni >= 0 && ni < N && nj >= 0 && nj < N) {
                        if (t != res[ni][nj]) goto NEXT;
                    }
                    else {
                        goto NEXT;
                    }
                }
                
                ans[t] = true;
                break;
              NEXT:;
            }

        }
    }
}

int main() {
    int TC; cin >> TC;

    char tbl2[100][100];

    for (int C = 1 ; C <= TC ; C++) {
        ans['R'] = ans['B'] = false;

        cin >> N >> K;
        string in;
        for (int i = 0 ; i < N ; i++) {
            for (int j = 0 ; j < N ; j++) {
                cin >> tbl[i][j];
            }
        }

        rotate();
        
        check();
        
        cout << "Case #" << C << ": ";
        if (ans['R'] and ans['B']) {
            cout << "Both" << endl;
        }
        else if (ans['R']){
            cout << "Red" << endl;
        }
        else if (ans['B']){
            cout << "Blue" << endl;
        }
        else {
            cout << "Neither" << endl;
        }
    }
}
