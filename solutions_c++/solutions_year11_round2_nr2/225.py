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
#include <iterator>
#include <iomanip>
#include <bitset>
#include <limits>

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

bool good(const vector<long double> &p, long double t, long double D) {
    long double prev = numeric_limits<double>::max()*-1;
    int i, N = p.size();

    REP(i, N) {
        prev += D;
        if (p[i] < prev) {
            if (prev - p[i] > t) return false;
        }
        if (p[i] > prev) {
            prev = max(prev, p[i] - t);
        }
    }
    return true;
}

int main(int argc, char** argv) {
    writeToFile = true;
    setSIO("in.txt", "out.txt");
    int t, T;
    cin >> T;

    REP(t, T) {
        int C, D;
        vector<long double> p;
        cin >> C >> D;
        int i, V, P, j;

        REP(i, C) {
            cin >> P >> V;
            REP(j, V) p.push_back(P);
        }
        sort(ALL(p));
        long double min = 0;
        long double max = 1000000000000LL, result;

        REP(i, 3000) {
            result = (min + max) / 2;
            if (max - min < 0.0000001) break;
            if (good(p, result, D)) {
                max = result;
            } else {
                min = result;
            }
        }
        printTest(result);
    }
    cout.flush();
    return 0;
}

