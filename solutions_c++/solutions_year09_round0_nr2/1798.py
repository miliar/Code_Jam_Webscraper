#include <algorithm>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

#define ALL(x)        (x).begin(), (x).end()
#define FOR(i, N, M)  for(int i = (int)(N); i != (int)(M); ++ i)
#define FORD(i, N, M) for (int i = (int)(N); i >= (int)(M); -- i)
#define FORI(it, x)   (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define REP(i, N)     for(int i = 0; i != (int)(N); ++ i)
#define INF           0x3f3f3f3f
#define TIP(x)        (cerr << #x << " = " << (x) << endl)
#define TIPA(a, i)    (cerr << #a << "[" #i " = " << (i) << "] = " << (a)[i] << endl)
#define SZ size()
#define MP make_pair
#define PB push_back

#define MAXN 128

int pozx[] = {-1, 0, 0, 1};
int pozy[] = {0, -1, 1, 0};

int T, H, W;
int M[MAXN][MAXN];
char Ans[MAXN][MAXN];
int lit;
vector< pair<int, int> > seq;

void makeBasin(char x) {
    int sz = seq.SZ;
    
    for (int i = 0; i < sz; ++ i) {
        Ans[seq[i].first][seq[i].second] = x;
    }
}

void drain (int i, int j) {
    int ii = 0, jj = 0, min = INF;
    seq.clear();
    
    while (true) {
        min = INF;
        seq.PB(MP(i, j));
        for (int k = 0; k < 4; ++ k)
            if (min > M[i + pozx[k]][j + pozy[k]]) {
                min = M[i + pozx[k]][j + pozy[k]];
                ii = i + pozx[k];
                jj = j + pozy[k];
            }
        if (Ans[i][j] != 0) {
            makeBasin(Ans[i][j]);
            break;
        }   
        
        if (M[ii][jj] >= M[i][j]) {
            makeBasin('a' + lit);
            ++lit;
            break;
        }
        
        i = ii;
        j = jj;        
    }
            
}

int main() {
    freopen ("inputx.in", "rt", stdin);
    freopen ("outputx.out", "wt", stdout);
    
    scanf ("%d\n", &T);
    for (int i = 1; i <= T; ++ i) {
        scanf ("%d %d\n", &H, &W);
        memset (M, 0, sizeof(M));
        memset (Ans, 0, sizeof(Ans));
        lit = 0;
        
        for (int j = 1; j <= H; ++ j)
            for (int k = 1; k <= W; ++ k)
                scanf ("%d ", &M[j][k]);
        for (int j = 1; j <= H; ++ j) M[j][0] = M[j][W+1] = INF;
        for (int j = 1; j <= W; ++ j) M[0][j] = M[H+1][j] = INF;
          
        for (int j = 1; j <= H; ++ j)
            for (int k = 1; k <= W; ++ k)
                if (Ans[j][k] == 0)
                    drain(j, k);
        
        printf ("Case #%d:\n", i);            
        for (int j = 1; j <= H; ++ j) {
            for (int k = 1; k < W; ++ k)
                printf ("%c ", Ans[j][k]);
            printf("%c\n", Ans[j][W]);
        }
    }
    
    return 0;
} 
