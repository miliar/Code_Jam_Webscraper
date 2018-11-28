/*
 * Author: NomadThanatos
 * Created Time:  2011/5/21 10:17:05
 * File Name: A.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <numeric>
#include <sstream>
#include <string>
using namespace std;
#define out(X) cerr << #X << ": " << (X) << endl
#define SZ(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))
#define REP(I,N) for (int I = 0; I < (N); ++I)
#define FOR(I,L,H) for (int I = (L); I < (H); ++I)
#define FORIT(I,V) for (typeof(V.begin()) I = V.begin(); I != V.end(); ++I)
#define MP(X,Y) make_pair((X),(Y))
#define PB push_back
#define ALL(X) X.begin(), X.end()
typedef long long lint;

int main() {
    freopen("A.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t = 0 ; t < T ; t++) {
        lint PD,PG,N;
        scanf("%lld%lld%lld",&N,&PD,&PG);
        lint gcd = __gcd(PD,100LL);
        bool flag;
        if (N >= 100LL / gcd) {
            if (PD == 100LL) {
                if (PG == 100LL) {
                    flag = true;
                }
                else flag = false;
            }
            else if (PD == 0LL) {
                if (PG == 0LL) {
                    flag = true;
                }
                else flag = false;
            }
            else {
                if (PG == 0LL || PG == 100LL) flag = false;
                else flag = true;
            }
        }
        else flag = false;
        printf("Case #%d: %s\n",t + 1,flag?"Possible":"Broken");
    }
    return 0;
}

