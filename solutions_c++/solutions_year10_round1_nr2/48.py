#include <string>
#include <cstring>
#include <vector>
#include <cmath> 
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
 
using namespace std;
 
#define REP(a,n) for(int a=0; a<(n); ++a)
#define INIT(a, v) __typeof(v) a = (v)
#define FOREACH(a, v) for (INIT(a, (v).begin()); a!=(v).end(); ++a)
 
template<class T>
inline int size(const T&t){return t.size();}
 
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef long long LL;

#define INF 1000000000
#define PB push_back
#define MP make_pair
 
//////////////////////////////////////////

int D, I, M, N;
int input[100];
int res[101][256];

int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        scanf("%d%d%d%d", &D, &I, &M, &N);
        REP(a, N)
            scanf("%d", &input[a]);
        REP(a, 256)
            res[0][a] = 0;
        REP(x, N)
            REP(dc, 256) {
                res[x+1][dc] = INF;
                REP(oc, 256) {
                    if (M>0)
                        res[x+1][dc] = min(res[x+1][dc], res[x][oc]+min(abs(dc-input[x])+max(0, abs(dc-oc)-1)/M*I, D+(abs(dc-oc)+M-1)/M*I));
                    else
                        if (dc==oc)
                            res[x+1][dc] = res[x][oc]+min(abs(dc-input[x]), D);
                }
            }
        int best = INF;
        REP(c, 256)
            best = min(best, res[N][c]);
        printf("Case #%d: %d\n", tt+1, best);
    }
}


