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
        int n;cin>>n;
        int r[1024], v[1024];
        pii t[1024];
        REP(i, n) {
            cin>>r[i];
            t[i] = make_pair(r[i], i);
        }
        sort(t, t + n);
        REP(i, n)
            r[t[i].second] = i;
        double sum = 0;
        memset(v, 0, sizeof v);
        REP(i, n)
            if (!v[i]) {
                int L = 0, c = i;
                while (1) {
                    L++;
                    v[c] = 1;
                    if (v[r[c]])
                        break;
                    else
                        c = r[c];
                }
                sum += L == 1 ? 0 : L;
            }
        printf("Case #%d: %.9lf\n", caseN + 1, sum);
    }
    return 0;
}
