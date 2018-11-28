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

#define MAXN 5005

int L, D, N;
int ind[MAXN];
char sir[MAXN][16];
char s[1024];
int check[64], iter;
int cnt;

void updateInd(int poz) {
    cnt = 0;
    for (int i = 0; ind[i] > -1; ++ i) {
        if (check[sir[ind[i]][poz] - 'a'] == iter) {
            ind[cnt++] = ind[i];
        }
    }
    ind[cnt] = -1;
}

int main() {
    freopen ("inputx.in", "rt", stdin);
    freopen ("outputx.out", "wt", stdout);
    
    scanf ("%d %d %d\n", &L, &D, &N);
    
    for (int i = 0; i < D; ++ i) {
        gets(sir[i]);
        ind[i] = i;
    }
    ind[D] = -1;
    
    for (int i = 0; i < N; ++ i) {
        cnt = D;
        for (int j = 0; j < D; ++ j) {
            ind[j] = j;
        }
        ind[cnt = D] = -1;
        gets(s);
        int sz = strlen(s), par = 0, poz = 0;
        for (int j = 0; j < sz; ++j) {
            if (s[j] == '(') {
                par = 1;
                ++iter;
            }
            else if (s[j] == ')') {
                par = 0;
                updateInd(poz);
                ++poz;
            }
            else {
                if (par == 0) {
                    check[s[j] - 'a'] = ++iter;
                    updateInd(poz);
                    ++poz;
                }
                else {
                    check[s[j] - 'a'] = iter;
                }
            }
        }
        
        // for (int j = 0; j < cnt; ++ j) printf ("%d ", ind[j]);
        // printf ("\n");
        printf ("Case #%d: %d\n", i+1, cnt);
    }
    
    return 0;
} 
