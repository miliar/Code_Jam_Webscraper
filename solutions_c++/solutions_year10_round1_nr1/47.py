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
#define FORD(a,b,c) for(int a=(b); a>=(c); --a)
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

int N, K;
int tab[50][50];
char input[100];

int test[50];
bool g1, g2;

void sprawdz(int len) {
    int ile = 0;
    REP(a, len) {
        if (test[a]==0 || !a || test[a]!=test[a-1])
            ile = 0;
        if (test[a])
            ++ile;
        if (ile>=K && test[a]==1)
            g1 = true;
        if (ile>=K && test[a]==2)
            g2 = true;
    }
}

int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        scanf("%d%d", &N, &K);
        REP(y, N) {
            scanf("%s", input);
            int pos = N-1;
            FORD(x, N-1, 0)
                if (input[x]!='.')
                    tab[y][pos--] = input[x]=='R' ? 1 : 2;
            while (pos>=0)
                tab[y][pos--] = 0;
        }
        g1 = g2 = 0;
        REP(y, N) {
            /// poziomo
            REP(x, N)
                test[x] = tab[y][x];
            sprawdz(N);
            
            // w dol
            REP(x, N-y)
                test[x] = tab[y+x][x];
            sprawdz(N-y);
            REP(x, N-y)
                test[x] = tab[y+x][N-1-x];
            sprawdz(N-y);
            
            //  w gore
            REP(x, y+1)
                test[x] = tab[y-x][x];
            sprawdz(y+1);
            REP(x, y+1)
                test[x] = tab[y-x][N-1-x];
            sprawdz(y+1);
        }
        REP(x, N) {
            REP(y, N) // pionowo
                test[y] = tab[y][x];
            sprawdz(N);
        }
        
        printf("Case #%d: %s\n", tt+1, (g1 && g2) ? "Both" : g1 ? "Red" : g2 ? "Blue" : "Neither");
    }
}


