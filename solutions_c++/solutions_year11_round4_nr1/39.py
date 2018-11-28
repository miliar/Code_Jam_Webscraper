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

int N, len, S, R;
double cz_b;
double czas;

pair<int, pii> kor[1000]; //(pr, pocz, kon)


int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        scanf("%d%d%d%lf%d", &len, &S, &R, &cz_b, &N);
        double zos = len;
        REP(a, N) {
            scanf("%d%d%d", &kor[a].second.first, &kor[a].second.second, &kor[a].first);
            zos -= kor[a].second.second-kor[a].second.first;
        }
        sort(kor, kor+N);
        czas = 0;
        if (zos/(double)R<cz_b) {
            czas += zos/(double)R;
            cz_b -= zos/(double)R;
        } else {
            czas += cz_b;
            zos -= R*cz_b;
            cz_b = 0;
            czas += zos/(double)S;
        }
        REP(a, N) {
            double dl = kor[a].second.second-kor[a].second.first;
            int speed = kor[a].first;
            if (dl/(double)(speed+R)<cz_b) {
                czas += dl/(double)(speed+R);
                cz_b -= dl/(double)(speed+R);
            } else {
                czas += cz_b;
                dl -= (speed+R)*cz_b;
                cz_b = 0;
                czas += dl/(double)(speed+S);
            }
        }
        printf("Case #%d: %.8f\n", (tt+1), czas);
    }
}


