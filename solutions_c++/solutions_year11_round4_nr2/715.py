#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cassert>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <fstream>
using namespace std;
#define pb push_back 
#define REP(i,n) for(int i=0;i<(n);i++ )
typedef long long LL;
typedef pair<int, int> pii;

int d[100][100];

int main(){
    int caseNumber;
    scanf("%d", &caseNumber);
    //cin>>caseNumber;
    REP(caseN, caseNumber) {
        int R, C, D;
        scanf("%d%d%d", &R, &C, &D);
        char buf[512];
        REP(i, R) {
            scanf("%s", buf);
            REP(j, C)
                d[i][j] = buf[j] - '0';
        }
        int res = 0;
        for (int s = 3; s <= min(R, C); s++) {
            for (int i = 0; i <= R - s; i++)
                for (int j = 0; j <= C - s; j++) {
                    double d1 = 0, d2 = 0;
                    REP(t1, s)
                        REP(t2, s) {
                            if (t1 == 0 && t2 == 0)
                                continue;
                            if (t1 == s - 1 && t2 == 0)
                                continue;
                            if (t1 == 0 && t2 == s - 1)
                                continue;
                            if (t1 == s - 1 && t2 == s - 1)
                                continue;
                            d1 += d[i + t1][j + t2] * ((s - 1) / 2.0 - t1);
                            d2 += d[i + t1][j + t2] * ((s - 1) / 2.0 - t2);
                        }
                    //~ cout<<s<<' '<<i<<' '<<j<<' '<<d1<<' '<<d2<<' '<<endl;
                    if (fabs(d1) < 1e-4 &&fabs(d2) < 1e-4)
                        res >?= s;
                }
        }
        if (res)
            printf("Case #%d: %d\n", caseN + 1, res);
        else
            printf("Case #%d: IMPOSSIBLE\n", caseN + 1);
    }
    return 0;
}
