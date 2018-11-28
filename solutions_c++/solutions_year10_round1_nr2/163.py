#include <cstdio>
#include <algorithm>
#include <cctype>
#include <cstring>
#include <cmath>
#include <list>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <climits>

#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define FORQ(i,a,b) for (int i=(a);i<=(b);++i)
#define FORD(i,a,b) for (int i=(a)-1;i>=(b);--i)
#define FORDQ(i,a,b) for (int i=(a);i>=(b);--i)
#define FORE(i,x) for (__typeof__((x).begin()) i=(x).begin();i!=(x).end();++i)
#define MP make_pair
#define F first
#define S second
#define PB push_back

using namespace std;

typedef long long LL;

int cosTV[256];
int TcosTV[256];

const int INF = (1<<20);

int main() {
    int lw;
    scanf("%d",&lw);
    FORQ(l,1,lw) {
        int D,I,M,n;
        scanf("%d%d%d%d",&D,&I,&M,&n);
        FOR(i,0,256)
            cosTV[i] = I;
        int cosE = 0;
        FOR(z,0,n) {
            int A;
            scanf("%d",&A);
            int ncosE = cosE + D;
            FOR(i,0,256) {
                TcosTV[i] = cosTV[i] + D;
                FOR(j,0,256) {
                    int cA = I + D + cosTV[j];
                    int dif = abs(i-j);
                    if (M == 0 && dif > 0) {
                        continue;
                    }
                    if (dif > 0)
                        cA += ((((dif % M) == 0) ? (dif/M) : ((dif/M)+1))-1)*I;
                    TcosTV[i] = min(TcosTV[i], cA);
                }
                   
                //V change
                FOR(j,0,256) {
                    int cA = abs(A-i) + cosTV[j];
                    int dif = abs(i-j);
                    if (M == 0 && dif > 0) {
                        continue;
                    }
                    if (dif > 0)
                        cA += ((((dif % M) == 0) ? (dif/M) : ((dif/M)+1))-1)*I;
                    TcosTV[i] = min(TcosTV[i], cA);
                }
                FOR(j,0,256) {
                    int cA = cosTV[j];
                    int dif = abs(A-j);
                    if (M == 0 && dif > 0) {
                        continue;
                    }
                    if (dif > 0) {
                        cA += ((((dif % M) == 0) ? (dif/M) : ((dif/M)+1))-1)*I;
                    }
                    dif = abs(i-A);
                    if (M == 0 && dif > 0) {
                        continue;
                    }
                    if (dif > 0) { 
                        cA += ((((dif % M) == 0) ? (dif/M) : ((dif/M)+1))-1)*I;
                        cA += I;
                    }
                    TcosTV[i] = min(TcosTV[i], cA);
                }
                TcosTV[i] = min(TcosTV[i], abs(A-i) + cosE);
            }
            TcosTV[A] = min(TcosTV[A], cosE);
            FOR(i,0,256)
                cosTV[i] = TcosTV[i];
            cosE = ncosE;
        }
        int best = INT_MAX;
        FOR(i,0,256)
            best = min(best, cosTV[i]);
        best = min(best,cosE);
        //FOR(i,0,256)
        //printf("%d\n",cosTV[i]);
        printf("Case #%d: %d\n",l,best);
    }
}
