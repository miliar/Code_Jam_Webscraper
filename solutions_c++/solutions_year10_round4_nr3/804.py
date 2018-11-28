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

int T[111][111];
int P[111][111];

bool isEmpty() {
    FORQ(i,1,100)
        FORQ(j,1,100)
            if (T[i][j] == 1)
                return false;
    return true;
}

int main() {
    int lw;
    scanf("%d",&lw);
    FORQ(l,1,lw) {
        int r;
        scanf("%d",&r);
        FORQ(i,1,100)
            FORQ(j,1,100)
                T[i][j] = 0;
        while (r--) {
            int x1,y1,x2,y2;
            scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
            FORQ(i,y1,y2)
                FORQ(j,x1,x2)
                    T[i][j] = 1;
        }
        int res = 0;
        while (!isEmpty()) {
            FORQ(i,1,100)
                FORQ(j,1,100)
                    P[i][j] = 0;
            FORQ(i,1,100)
                FORQ(j,1,100)
                    if (T[i][j] == 1) {
                        if (T[i-1][j] == 0 && T[i][j-1] == 0)
                            P[i][j] = 0;
                        else
                            P[i][j] = 1;
                    } else {
                        if (T[i-1][j] == 1 && T[i][j-1] == 1)
                            P[i][j] = 1;
                        else
                            P[i][j] = 0;
                    }
            FORQ(i,1,100)
                FORQ(j,1,100)
                    T[i][j] = P[i][j];
            res++;
        }

        printf("Case #%d: %d\n",l,res);
    }
}
