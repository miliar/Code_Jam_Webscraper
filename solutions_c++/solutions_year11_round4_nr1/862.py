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

int main(){
    int caseNumber;
    scanf("%d", &caseNumber);
    //cin>>caseNumber;
    REP(caseN, caseNumber) {
        int X, S, R, t, N;
        scanf("%d%d%d%d%d", &X, &S, &R, &t, &N);
        double res = 0;
        vector<pii> V;
        R -= S;
        REP(i, N) {
            int B, E, w;
            scanf("%d%d%d", &B, &E, &w);
            V.pb(make_pair(w + S, E - B));
            X -= E - B;
        }
        V.pb(make_pair(S, X));
        sort(V.begin(), V.end());
        REP(i, V.size()) {
            res += V[i].second * 1.0 / V[i].first;
            //~ cout<<V[i].second<<'x'<<V[i].first<<' '<<res<<endl;
        }
        double T = t;
        REP(i, V.size()) {
            double des = V[i].second * 1.0 / (V[i].first + R);
            if (des > T) {
                des = T;                
            }
            res -= des * (R ) / V[i].first;
            T -= des;
            //~ cout<<des<<' '<<i<<' '<<res<<' ' <<T<<endl;
        }

        printf("Case #%d: %.10lf\n", caseN + 1, res);
    }
    return 0;
}
