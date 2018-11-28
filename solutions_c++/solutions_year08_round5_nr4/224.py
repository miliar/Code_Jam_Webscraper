#define _CRT_SECURE_NO_DEPRECATE
#pragma warning(disable:4530)
#include <string>
#include <vector>
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <sstream>
#include <set>
#include <cmath>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(it,x) for(typeof((x).begin())it=(x).begin();it!=(x).end();++it)
#define all(x) (x).begin(),(x).end()
#define CLR(x,v) memset(x,v,sizeof(x))
#define pb push_back
#define sz size()
#define exist(c,x) ((c).find(x)!=(c).end())
#define cexist(c,x) (find(all(c),x)!=(c).end())
#define SMIN(a, b) a = min((a),(b))
#define SMAX(a, b) a = max((a),(b))

typedef long long ll;

int D[100][100];
int H, W, R;
int ob[10][2];

const int magic = 10007;
int main(int argc, char *argv[]) {
    freopen(argv[1], "r", stdin);
    int Tests;
    cin >> Tests;
    FOR(test, 1, Tests+1) {
        printf("Case #%d: ", test);
        cin >>H >>W >>R;
        REP(i, R) {
            cin >> ob[i][0] >>ob[i][1];
            ob[i][0]--; ob[i][1]--;
        }
        CLR(D, 0);
        REP(r, H) {
            REP(c, W) {
                if (r == 0 && c == 0) {
                    D[r][c] = 1;
                    continue;
                }
                D[r][c] = 0;
                bool obs = false;
                REP(obid, R) {
                    if (ob[obid][0] == r &&
                        ob[obid][1] == c) {
                        obs = true;
                        break;
                    }
                }
                if (obs) continue;
                int dr, dc;

                dr = r-2; dc = c-1;
                if (!(dr < 0 || H <= dr || dc < 0 || W <= dc)) 
                    D[r][c] += D[dr][dc];
                dr = r-1; dc = c-2;
                if (!(dr < 0 || H <= dr || dc < 0 || W <= dc)) 
                    D[r][c] += D[dr][dc];

                D[r][c] = D[r][c] % magic;
            }
        }
        /*
        REP(i, H) {
            REP(j, W) {
                cout << D[i][j] << " ";
            }
            cout <<endl;
        }
        */
        printf("%d\n", D[H-1][W-1]);
    }

}
