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

#define INF 1000000000
#define PB push_back
#define MP make_pair
 
//////////////////////////////////////////


int X[40], Y[40], R[40];

int N;


int main() {
    int TT;
    scanf("%d", &TT);
    REP(t, TT) {
        scanf("%d", &N);
        REP(a, N)
          scanf("%d%d%d", X+a, Y+a, R+a);
        double best = INF;
        if (N==1)
          best = R[0];
        else
        if (N==2)
          best = max(R[0], R[1]);
        else
        if (N==3)
          REP(sam, N) {
            int ns1 = sam==0 ? 1 : 0;
            int ns2 = sam==2 ? 1 : 2;
            int xd = X[ns1]-X[ns2];
            xd *= xd;
            int yd = Y[ns1]-Y[ns2];
            yd *= yd;
            best = min(best, max(1.*R[sam], (sqrt(xd+yd)+R[ns1]+R[ns2])/2));
          }

        printf("Case #%d: %f\n", t+1, best);
    }
    
}


