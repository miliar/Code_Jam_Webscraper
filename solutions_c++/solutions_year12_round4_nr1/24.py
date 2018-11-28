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
#define FOR(a,b,c) for(int a=(b); a<=(c); ++a)
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

int N,D;
int di[20000], li[20000], maxdl[20000];

int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        scanf("%d", &N);
        REP(a, N) {
            scanf("%d%d", &di[a], &li[a]);
            maxdl[a] = 0;
        }
        scanf("%d", &D);
        maxdl[0] = di[0];
        bool ok = false;
        REP(a, N) {
          if (di[a]+maxdl[a]>=D)
            ok = 1;
          for (int b = a+1; b<N && di[b]-di[a]<=maxdl[a]; ++b)
            maxdl[b] = max(maxdl[b], min(li[b], di[b]-di[a]));
        }
        printf("Case #%d: %s\n", (tt+1), ok ? "YES" : "NO");
    }
}


