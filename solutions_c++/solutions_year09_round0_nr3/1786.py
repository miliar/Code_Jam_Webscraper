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

vector< int > poz[32];
int T, N, Ans;
int d[512][20];
char sir[512];
char match[20] = {'w','e','l','c','o','m','e',' ','t','o',' ','c','o','d','e',' ','j','a','m'};

int main() {
    freopen ("inputx.in", "rt", stdin);
    freopen ("outputx.out", "wt", stdout);
    
    scanf ("%d\n", &T);
    for (int i = 1; i <= T; ++ i) {
        Ans = 0;
        for (int j = 0; j < 32; ++ j) poz[j].clear();
        memset(d, 0 ,sizeof(d));
        gets(sir);
        N = strlen(sir);
        
        for (int j = 0; j < N; ++ j) {
            if (sir[j] == ' ') poz[27].PB(j);
            else poz[sir[j] - 'a'].PB(j);
            if (sir[j] == 'w')
                d[j][0] = 1;
        }        
        
        for (int j = 0; j < N; ++ j) {
            for (int k = 1; k < 19; ++ k)
                if (match[k] == sir[j]) {
                    int p, sz;
                    if (match[k-1] == ' ')
                        p = 27;
                    else
                        p = match[k-1] - 'a';
                    sz = poz[p].SZ;
                    
                    for (int l = 0; l < sz; ++ l) {
                        if (poz[p][l] < j) {
                            d[j][k] += d[poz[p][l]][k-1];
                            if (d[j][k] > 10000)
                                d[j][k] -= 10000;
                        }
                    }
                }
        }
        
        /*for (int j = 0; j < N; ++ j, printf("\n"))
            for (int k = 0; k < 19; ++ k)
                printf ("%d ", d[j][k]);*/
        
        for (int j = 0; j < N; ++ j) {
            Ans += d[j][18];
            if (Ans > 10000)
                Ans -= 10000;
        }
            
        printf ("Case #%d: %04d\n", i, Ans);
    }
    
    return 0;
} 
