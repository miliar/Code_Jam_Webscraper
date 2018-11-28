//      anks
#include <string>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <map>
#include <iostream>
#include <string.h>
using namespace std;

typedef long long ll;
#define debug(args...) dbg(),args
#define S(N) scanf("%d", &N)
#define SF(N) scanf("%f", &N)
#define SS(N) scanf("%s", N)
#define FOR(A,B,C) for(int A=B;A<C;++A)
#define RFOR(A,B,C) for(int A=B;A>=C;--A)
#define PB(A,B) A.push_back(B);
#define MEM(A,B) memset(A,B,sizeof(A))
#define MAX(A,B) ((A > B) ? A : B)
#define MIN(A,B) ((A < B) ? A : B)
#define MAXLIM 100000
#define INF 1000000
bool DBG;
struct dbg { template<typename T> dbg& operator , (const T& v) { if (DBG)
 cerr << v << " "; return *this; } ~dbg() { if (DBG) cerr << endl; } };
int a, b;

float solve1(float pa[]) {
    int size = (1<<a);
    float pr[size];

    pr[0] = pa[0];
    pr[1] = (1 - pa[0]);

    int keys[3][2] = {
        {b-a+1, 2*b-a+2},
        {b-a+3, b-a+3},
        {b+2, b+2}
    };

    float min, expected;

    min = INF;
    FOR(i, 0, 3) {
        expected = 0;
        FOR(j, 0, size) {
            expected += pr[j] * keys[i][j];
        }
        min = MIN(expected, min);
    }

    return min;
}

float solve2(float pa[]) {
    int size = (1<<a);
    float pr[size];

    pr[0] = pa[0] * pa[1];
    pr[1] = pa[0] * (1- pa[1]);
    pr[2] = (1- pa[0]) * pa[1];
    pr[3] = (1 - pa[0]) * (1- pa[1]);

    int keys[4][4] = {
        {b-a+1, 2*b-a+2, 2*b-a+2, 2*b-a+2},
        {b-a+3, b-a+3, 2*b-a+4, 2*b-a+4},
        {b-a+5, b-a+5, b-a+5, b-a+5},
        {b+2, b+2, b+2, b+2}
    };

    float min, expected;

    min = INF;
    FOR(i, 0, 4) {
        expected = 0;
        FOR(j, 0, size) {
            expected += pr[j] * keys[i][j];
        }
        min = MIN(expected, min);
    }

    return min;
}

float solve3(float pa[]) {
    int size = (1<<a);
    float pr[size];

    pr[0] = pa[0] * pa[1] * pa[2];
    pr[1] = pa[0] * pa[1] * (1- pa[2]);
    pr[2] = pa[0] * (1- pa[1]) * pa[2];
    pr[3] = (1- pa[0]) * pa[1] * pa[2];
    pr[4] = pa[0] * (1 - pa[1]) * (1- pa[2]);
    pr[5] = (1 - pa[0]) * pa[1] * (1- pa[2]);
    pr[6] = (1 - pa[0]) * (1- pa[1]) * pa[2];
    pr[7] = (1 - pa[0]) * (1- pa[1]) * (1- pa[2]);

    int keys[5][8]= {
        {b-a+1, 2*b-a+2, 2*b-a+2, 2*b-a+2, 2*b-a+2, 2*b-a+2, 2*b-a+2, 2*b-a+2},
        {b-a+3, b-a+3, 2*b-a+4, 2*b-a+4, 2*b-a+4, 2*b-a+4, 2*b-a+4, 2*b-a+4},
        {b-a+5, b-a+5, b-a+5, b-a+5, b-a+5, b-a+5, b-a+5, 2*b-a+6},
        {b-a+7, b-a+7, b-a+7, b-a+7, b-a+7, b-a+7, b-a+7, b-a+7},
        {b+2, b+2, b+2, b+2, b+2, b+2, b+2, b+2}
    };

    float min, expected;

    min = INF;
    FOR(i, 0, 5) {
        expected = 0;
        FOR(j, 0, size) {
            expected += pr[j] * keys[i][j];
        }
        min = MIN(expected, min);
    }

    return min;
}

int main (int argc, char *argv[]) {
    DBG = (argc > 1 && *argv[1]);

    int t;
    S(t);

    FOR(k, 0, t) {
        S(a); S(b);
        float pa[a];
        FOR(i, 0, a) {
            SF(pa[i]);
        }
        switch(a) {
            case 1:
                printf("Case #%d: %f\n", k+1, solve1(pa)); break;
            case 2:
                printf("Case #%d: %f\n", k+1, solve2(pa)); break;
            case 3:
                printf("Case #%d: %f\n", k+1, solve3(pa)); break;
        }
    }

    return 0;
}
