#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <ctime>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define SIZE(c) ((int)((c).size()))
#define FOREACH(i,c) for(__typeof((c).begin()) i =(c).begin();i!=(c).end();++i)
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef long long LL;
typedef long double LD;

#define st first
#define nd second
#define mp make_pair
#define pb push_back

const int NIL = (-1);

const int N = 300;

bool c[N][N];

void step() {
    for(int i=N-1;i>0;i--)
        for(int j=N-1;j>0;j--) {
            if (c[i][j]) {
                if (!(c[i-1][j]||c[i][j-1]))
                    c[i][j] = 0;
            } else {
                if (c[i-1][j]&&c[i][j-1])
                    c[i][j] = 1;
            }
        }
}

bool died() {
    REP(i,N) REP(j,N) if (c[i][j]) return false;
    return true;
}

void check() {
    REP(i,N) if (c[i][N-1]||c[N-1][i]) {
        printf("DUPA\n");
        exit(13);
    }
}

void scase() {
    REP(i,N) REP(j,N) c[i][j] = 0;
    int r;
    scanf("%d",&r);
    while(r--) {
        int x1,y1,x2,y2;
        scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
        for(int i=x1;i<=x2;i++)
            for(int j=y1;j<=y2;j++)
                c[i][j] = 1;
    }
    int count = 0;
    while(!died()) {
        step();
        check();
        count++;
    }
    printf("%d\n",count);
}


int main() {
    int j;
    scanf("%d",&j);
    for(int i=1;i<=j;i++) {
        printf("Case #%d: ",i);
        scase();
    }
    return 0;
}

