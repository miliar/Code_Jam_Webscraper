#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <stack>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>

using namespace std;

#define DPRINT printf
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

int main (void) {
    int T;
    cin >> T;
    REP(i, T) {
        int N;
        cin >> N;
        char schedule[200][200];
        int opNum[200];
        double wp[200];
        double owp[200];
        double oowp[200];
        REP(j, N) {
            cin >> schedule[j];
        }
        // calc wp.
        REP(j, N) {
            double tmpOpNum = 0;
            double winSum = 0;
            REP(k, N) {
                if (schedule[j][k] == '.') { continue; }
                tmpOpNum++;
                if (schedule[j][k] == '1') { winSum++; }
            }
            opNum[j] = tmpOpNum;
            wp[j] = winSum / opNum[j];
        }
        // calc owp.
        REP(j, N) {
            double wpSum = 0;
            REP(k, N) {
                if (schedule[j][k] == '.') { continue; }
                wpSum += ((wp[k] * opNum[k]) - (schedule[k][j] - '0')) /
                    (opNum[k] - 1);
            }
            owp[j] = wpSum / opNum[j];
        }
        // calc oowp.
        REP(j, N) {
            double owpSum = 0;
            REP(k, N) {
                if (schedule[j][k] == '.') { continue; }
                owpSum += owp[k];
            }
            oowp[j] = owpSum / opNum[j];
        }
        cout << "Case #" << i + 1 << ":" << endl;
        REP(j, N) {
            //cout << schedule[j] << endl;
            //cout << wp[j] << endl;
            //printf("%6f\n", wp[j]);
            //printf("%6f\n", owp[j]);
            //printf("%6f\n", oowp[j]);
            //cout << 0.25 * wp[j] + 0.5 * owp[j] + 0.25 * oowp[j] << endl;;
            printf("%.12f\n", 0.25 * wp[j] + 0.5 * owp[j] + 0.25 * oowp[j]);
        }
        //double a = 7, b = 12;
        //cout << a / b << endl;
    }
    return 0;
}

                //cout << k << ":wp[k]" << wp[k] << " opNum[k]" << opNum[k] << endl;
