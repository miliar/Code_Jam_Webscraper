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

int C, D, N;
char zloz[36][4], opo[28][3], txt[101];

int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        scanf("%d", &C);
        REP(a, C)
            scanf("%s", zloz[a]);
        scanf("%d", &D);
        REP(a, D)
            scanf("%s", opo[a]);
        scanf("%d%s", &N, txt);
        string wyn;
        REP(a, N) {
            if (size(wyn))
                REP(c, C)
                    if ((wyn[size(wyn)-1]==zloz[c][0] && txt[a]==zloz[c][1]) ||
                        (wyn[size(wyn)-1]==zloz[c][1] && txt[a]==zloz[c][0])) {
                        wyn[size(wyn)-1] = zloz[c][2];
                        goto dalej;
                    }
            REP(b, size(wyn))
                REP(d, D)
                    if ((wyn[b]==opo[d][0] && txt[a]==opo[d][1]) ||
                        (wyn[b]==opo[d][1] && txt[a]==opo[d][0])) {
                        wyn = "";
                        goto dalej;
                    }
            wyn += txt[a];
            dalej:;
        }
        string w2;
        REP(a, size(wyn)) {
            if (!w2.empty()) 
                w2 += ", ";
            w2 += wyn[a];
        }
        printf("Case #%d: [%s]\n", tt+1, w2.c_str());
    }
}


