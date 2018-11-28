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

int main(int argc, char** argv) {
    writeToFile = true;
    setSIO("in.txt", "out.txt");
    int t, T;
    cin >> T;

    REP(t, T) {
        int n, N, i, j;
        cin >> N;
        vector<string> G(N);
        REP(i, N) cin >> G[i];
        vector<double> win(N), play(N), OWP(N), OOWP(N), result(N);

        REP(i, N) {
            int count = 0, w = 0;

            REP(j, N) {
                if (G[i][j] != '.') ++count;
                if (G[i][j] == '1') ++w;
            }
            win[i] = w;
            play[i] = count;
        }

        REP(i, N) {
            double wp = 0;
            int count = 0;
            REP(j, N) if (G[i][j] == '1') {
                count++;
                wp += win[j] / (play[j] - 1);
            } else if (G[i][j] == '0') {
                count++;
                wp += (win[j] - 1) / (play[j] - 1);
            }
            OWP[i] = wp / (double) count;
        }

        REP(i, N) {
            double owp = 0;
            int count = 0;
            REP(j, N) if (G[i][j] != '.') ++count, owp += OWP[j];
            OOWP[i] = owp / (double) count;
        }

        REP(i, N) result[i] = 0.25 * win[i] / play[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
        printTest("");
        REP(i, N) cout << result[i] << endl;
    }
    cout.flush();
    return 0;
}

