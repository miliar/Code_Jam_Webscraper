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

int N;

struct planet {
    int x;
    int y;
    int z;
    int p;
} P[2000];


#define sqr(x) ((x)*(x))

double evaluate(double x, double y, double z) {
    double mini = 0.0;
    REP(i, N) {
        double th = fabs(x-P[i].x) + fabs(y-P[i].y) + fabs(z-P[i].z);
        th = th / P[i].p;
        mini = max(mini, th);
    }
    return mini;
}

double eval() {
    double b[3][2];
    REP(i, 3) {
        b[i][0] = 1e7;
        b[i][1] = -1e7;
    }
    REP(i, N) {
        b[0][0] = min(b[0][0], 1.0*P[i].x);
        b[1][0] = min(b[1][0], 1.0*P[i].y);
        b[2][0] = min(b[2][0], 1.0*P[i].z);

        b[0][1] = max(b[0][1], 1.0*P[i].x);
        b[1][1] = max(b[1][1], 1.0*P[i].y);
        b[2][1] = max(b[2][1], 1.0*P[i].z);
    }

    double las = 0.0;

    REP(z, 500) {
        int c[3], mc[3];
        double mini = 1e10;
        for (c[0] = 0; c[0] < 2; c[0]++) 
            for (c[1] = 0; c[1] < 2; c[1]++) 
                for (c[2] = 0; c[2] < 2; c[2]++) {
                    double np[3];
                    REP(i, 3) {
                        if (c[i] == 0) 
                            np[i] = (b[i][0] * 2 + b[i][1] ) / 3.0;
                        else
                            np[i] = (b[i][1] * 2 + b[i][0] ) / 3.0;
                    }
                    double thi = evaluate(np[0], np[1], np[2]);
                    if (thi < mini) {
                        mini = thi;
                        REP(i, 3) {
                            mc[i] = c[i];
                        }
                    }
                }
        REP(i, 3) {
            if (mc[i] == 0) {
                b[i][1] = (b[i][0] + b[i][1] * 2) / 3.0;
            }
            else {
                b[i][0] = (b[i][1] + b[i][0] * 2) / 3.0;
            }
        }

        las = mini;
    }
    return las;
}

int main(int argc, char *argv[]) {
    int Tests;
    freopen(argv[1], "r", stdin);
    cin >>Tests;
    FOR(test, 1, Tests+1) {
        printf("Case #%d: ", test);
        cin >> N;
        REP(i, N) {
            cin >> P[i].x;
            cin >> P[i].y;
            cin >> P[i].z;
            cin >> P[i].p;
        }
        printf("%.6lf\n", eval());
    }
    return 0;
}

