#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>
#include <iomanip>
#include <cassert>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for(__typeof__((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define mp make_pair
#define pb push_back
#define DBG(...) { if(1) fprintf(stderr, __VA_ARGS__); }
#define DBGDO(X) { if(1) cerr << "DBGDO: " << (#X) << " = " << (X) << endl; }

int T;

char board[6][6];

bool chkpl(char p) {
    FOR (x, 0, 4) {
        bool b = true;
        FOR (y, 0, 4) {
            if (board[y][x] != 'T' && board[y][x] != p) {
                b = false;
                break;
            }
        }
        if (b) return true;
    }
    FOR (y, 0, 4) {
        bool b = true;
        FOR (x, 0, 4) {
            if (board[y][x] != 'T' && board[y][x] != p) {
                b = false;
                break;
            }
        }
        if (b) return true;
    }
    bool b;
    b = true;
    FOR (i, 0, 4) {
        if (board[3-i][i] != 'T' && board[3-i][i] != p) {
            b = false;
            break;
        }
    }
    if (b) return true;
    b = true;
    FOR (i, 0, 4) {
        if (board[i][i] != 'T' && board[i][i] != p) {
            b = false;
            break;
        }
    }
    if (b) return true;
    return false;
}

int main() {
    cin >> T;
    FOR (t, 0, T) {
        bool full = true;
        FOR (i, 0, 4) {
            scanf("%s\n", board[i]);
            if (strchr(board[i], '.')) {
                full = false;
            }
        }
        char* msg = (char*)"??";
        if (chkpl('X')) msg = (char*)"X won";
        else if (chkpl('O')) msg = (char*)"O won";
        else if (!full) msg = (char*)"Game has not completed";
        else msg = (char*)"Draw";
        printf("Case #%d: %s\n", t+1, msg);
    }
    return 0;
}

