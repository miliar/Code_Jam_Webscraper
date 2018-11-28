#include <cstdio>
#include <algorithm>
#include <cctype>
#include <cstring>
#include <cmath>
#include <list>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <climits>

#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define FORQ(i,a,b) for (int i=(a);i<=(b);++i)
#define FORD(i,a,b) for (int i=(a)-1;i>=(b);--i)
#define FORDQ(i,a,b) for (int i=(a);i>=(b);--i)
#define FORE(i,x) for (__typeof__((x).begin()) i=(x).begin();i!=(x).end();++i)
#define MP make_pair
#define F first
#define S second
#define PB push_back

using namespace std;

typedef long long LL;

int M[2000];
int C[15][2000];
int W[2000*20];

int mark(int co, int ile) {
    if (co == 1) {
        if (ile > 0)
            W[co] = -1;
        return 1;
    }
    int res = mark(co/2, ile);
    if (res < ile)
        W[co] = -1;
    return res + 1;
}

int main() {
    int lw;
    scanf("%d",&lw);
    FORQ(l,1,lw) {
        int p;
        scanf("%d",&p);
        int p2 = 1<<p;
        FOR(i,0,p2) {
            scanf("%d",&M[i]);
            M[i] = p-M[i];
        }
        FOR(i,0,p) {
            int pp2 = 1<<(p-i-1);
            FOR(j,0,pp2)
                scanf("%d",&C[i][j]);
        }
        int g = 1;
        FORD(i,p,0) {
            int pp2 = 1<<(p-i-1);
            FOR(j,0,pp2)
                W[g++] = C[i][j];
        }
        FOR(i,0,p2) {
            mark((g+i)/2,M[i]);
        }
        int res = 0;
        FOR(i,1,g)
            if (W[i] == -1)
                res++;
        printf("Case #%d: %d\n",l,res);
    }
}
