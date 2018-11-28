#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cstdio>
#include <vector>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <numeric>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

//TopCoder defines
#define EACH(i,c) for(__typeof((c).begin()) i = (c).begin();i!=(c).end();i++)
#define dbg(e) cout<<(#e)<<" : "<<e<<endl
#define REP(i,n) for(int i=0;i<(n);i++)
#define all(x) x.begin(),x.end()
#define sz(x) int((x).size())
#define pb  push_back
#define mp make_pair

//Extras
#define SI(x) scanf("%d", &x)
#define SLL(x) scanf("%lld", &x)
#define SD(x) scanf("%lf", &x)

typedef long long LL;

void main2() {
    int A, B;
    double p[105];
    SI(A); SI(B);
    REP(i,A) SD(p[i]);
    double rit = 0, bak[5] = {}, giv = 0;
    REP(mask, 1 << A) {
        //calculate prob
        double now = 1;
        REP(i,A) if(mask & (1 << i)) now *= 1 - p[i]; else now *= p[i];

        //type right away
        if(mask == 0) rit += now * (B - A + 1);
        else rit += now * (B - A + 2 + B);

        //backspace
        REP(i,A) {
            //backspace 'i' times
            int cnt = 2 * (i + 1), bad = 0;
            REP(j,A) if(j < A - i - 1 && (mask & (1 << j))) bad = 1;
            if(bad) cnt += B + 1;
            cnt += B - A + 1;
            bak[i] += now * cnt;
        }

        //give up
        giv += now * (B + 2);
    }
    double mini = 1e10;
    mini = min(mini, rit);
    REP(i,A) mini = min(mini, bak[i]);
    mini = min(mini, giv);
    printf("%.6lf\n", mini);
}

int main() {
    int test; SI(test); REP(tt,test) {
        printf("Case #%d: ", tt+1);
        main2();
    }
}
