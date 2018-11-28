#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

#define pb push_back
#define mp make_pair

#define ALL(x) (x).begin(),(x).end()
#define CLR(a,b) memset(a,b,sizeof(a))
#define REPN(x,a,b) for (int x=a; x<b;++x)
#define REP(x,b) REPN(x, 0, b)

#define dbg(x) cout << #x << " = " << x << endl;
#define dbg2(x, y) cout << #x << " = " << x << "  " << #y << " = " << y << endl;
#define dbg3(x, y, z) cout << #x << " = " << x << "  " << #y << " = " << y << "  " << #z << " = " << z << endl;
#define dbg4(x, y, z, w) cout << #x << " = " << x << "  " << #y << " = " << y << "  " << #z << " = " << z << "  " << #w << " = " << w <<  endl;

int main() {

    int n;
    cin >> n;
    string A[4];
    string B = "XO";
    REP(tc, n) {
        REP(i, 4)
            cin >> A[i];
        int win = 2;
        REP(k, 2) {
            bool bo = 1;
            REP(i, 4) {
                bo = 1;
                REP(j, 4) if (A[i][j] != B[k] && A[i][j] != 'T') bo = 0;
                if (bo) win = k; 
            }
            REP(i, 4) {
                bo = 1;
                REP(j, 4) if (A[j][i] != B[k] && A[i][j] != 'T') bo = 0;
                if (bo) win = k;
            }
            bo = 1;
            REP(j, 4) if (A[j][j] != B[k] && A[j][j] != 'T') bo = 0;
            if (bo) win = k;
            bo = 1;
            REP(j, 4) if (A[j][3-j] != B[k] && A[j][3-j] != 'T') bo = 0;
            if (bo) win = k;
        }
        if (win != 2) {
            cout << "Case #" << tc+1 << ": " << B[win] << " won" << "\n";
        }
        else {
            bool no = 0;
            REP(i, 4) REP(j, 4) if (A[i][j] == '.') no = 1;
            if (no) cout << "Case #" << tc+1 << ": Game has not completed\n";
            else cout << "Case #" << tc+1 << ": Draw\n";
        }
    }
	
	return 0;
}
