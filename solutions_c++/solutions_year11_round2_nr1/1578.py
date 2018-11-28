#include <boost/config.hpp>
#include <iostream>
#include <utility>
#include <algorithm>
#include <string>
#include <sstream>
#include <fstream>
#include <map>
#include <gmp.h>
#include <gmpxx.h>
#include <boost/utility.hpp>

using namespace std;
using namespace boost;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define PI(a,b) make_pair(a,b);



int main() {
    int T;
    cin >> T;
    FOR(i,1,T+1) {
            int N;
            cin >> N; // Number of Teams
            int mat[N][N];

            FOR(j,0,N) {
                string str;
                cin >> str;
                FOR(k,0,str.length()) {
                    char ch = str.at(k);
                    if (ch == '0') mat[j][k] = 0;
                    else if (ch == '1') mat[j][k] = 1;
                    else mat[j][k] = -1;
                }
            }
            double numopps[N];

            FOR (j,0,N) {
                numopps[j] = 0;
                FOR (s,0,N)
                    if (mat[j][s] != -1) numopps[j]++;
            }
            double avgs[N];
            FOR (j,0,N) {
                    avgs[j] = 0.;
                    FOR(s,0,N)
                        if (mat[j][s] != -1)
                            avgs[j] += mat[j][s];
                    avgs[j] /= numopps[j];
            }



            double owp[N];
            FOR (j,0,N) {
                    owp[j] = 0.;
                    FOR(k,0,N) {
                        if (mat[j][k] != -1) {
                            int ct = numopps[k];
                            double val = avgs[k] * ct;
                            if (mat[j][k] == 0) val--;
                            val = val / (ct-1);
                            owp[j] += val;
                        }
                    }
                    owp[j] /= numopps[j];
            }
            double oowp[N];
            FOR (j,0,N) {
                    oowp[j] = 0.;
                    FOR (k,0,N) {
                        if (mat[j][k] != -1) {
                            oowp[j] += owp[k];
                        }
                    }
                    oowp[j] /= numopps[j];
            }

            cout.precision(7);
            cout << "Case #" << i << ": " << endl;
            FOR(j,0,N)
                cout << (0.25 * avgs[j] + 0.5 * owp[j] + 0.25*oowp[j]) << endl;

    }
}


