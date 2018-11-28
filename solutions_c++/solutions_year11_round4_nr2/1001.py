#include <stdlib.h>
#include <fstream>
#include <math.h>
#include <ctype.h>
#include <string.h>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <utility>
#include <fstream>
#include <numeric>
#include <limits.h>
#include <limits>
#include <iterator>
#include <iomanip>
#include <bitset>
#include <assert.h>

using namespace std;

#define EPS (1e-9)
#define PI (2 * acos(0.0))
#define XOR(exp1,exp2) ( ( (exp1)&&!(exp2) ) || (!(exp1) && (exp2)) )
#define REP(x,n)  for(x=0;x<(int)(n);x++)
#define EACH(itr, cont) for(typeof((cont).begin()) itr = (cont).begin(); itr != (cont).end(); ++itr)
#define ALL(X)    (X).begin(),(X).end()
#define mem0(X)    memset((X),0,sizeof(X))
#define mem1(X)    memset((X),255,sizeof(X))

typedef long long LL;

ifstream input;
ofstream output;
bool writeToFile = false;

void setSIO(std::string iFilePath, std::string oFilePath) {
    cin.sync_with_stdio(false);
    cout << setprecision(16);
    if (writeToFile) {
        streambuf *i, *o;
        input.open(iFilePath.c_str(), ifstream::in);
        i = input.rdbuf();
        output.open(oFilePath.c_str(), ifstream::out);
        o = output.rdbuf();
        cin.rdbuf(i);
        cout.rdbuf(o);
    }
}

template <typename T>
void printTest(T result) {
    static int testIndex = 1;
    cout << "Case #" << testIndex << ": " << result << endl;
    testIndex++;
}

void main2();

int main(int argc, char** argv) {
    writeToFile = true;
    setSIO("in.txt", "out.txt");
    int t, T;
    cin >> T;

    REP(t, T) {
        main2();
        assert(cin);
    }
    cout.flush();
    return 0;
}

void main2() {
    LL R, C;
    double D;
    cin >> R >> C >> D;
    char G[505][505];
    LL i, j;
    REP(i, R) REP(j, C) cin >> G[i][j];
    LL max = min(C, R);
    for (LL size = max; size >= 3; size--) {

        REP(i, R - size + 1) REP(j, C - size + 1) {
            double cX = (double) (size - 1) / 2, cY = (double) (size - 1) / 2;
            LL tX = 0, tY = 0;
            int x, y;

            REP(x, size) REP(y, size) {
                if (x == 0 && (y == 0 || y == size - 1)) continue;
                if (x == size - 1 && (y == 0 || y == size - 1)) continue;
                tX += (LL) (round(2 * (cX - x)))*(D + (G[i + x][j + y] - '0'));
                tY += (LL) (round(2 * (cY - y)))*(D + (G[i + x][j + y] - '0'));
            }
            //            if (tX < 0) tX *= -1;
            //            if (tY < 0) tY *= -1;
            //if (tX < numeric_limits<double>::min() && tY < numeric_limits<double>::min()) {
            if (tX == 0 && tY == 0) {
                printTest(size);
                return;
            }
        }
    }
    printTest("IMPOSSIBLE");
}