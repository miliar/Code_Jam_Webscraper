#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <math.h>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
using namespace std;

struct Poi{
    int x, y;
}Q[2][1000000], *C;

struct CMP{
    bool operator () (const int a, const int b){
        if (C[a].x == C[b].x){
            return C[a].y < C[b].y;
        }
        return C[a].x < C[b].x;
    }
};

int N[2], n;
set <int, CMP> Set[2];
set <int, CMP> :: iterator P;

void input(){
    int i, j, x1, x2, y1, y2;
    scanf("%d", &n);
    N[0] = 1;
    C = Q[0];
    Set[0].clear();
    for (i = 0; i < n; ++ i){
        scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
        if (x1 > x2) swap(x1, x2);
        if (y1 > y2) swap(y1, y2);
        while (x1 <= x2){
            for (j = y1; j <= y2; ++ j){
                Q[0][N[0]].x = x1;
                Q[0][N[0]].y = j;
                Set[0].insert(N[0]);
                ++ N[0];
            }
            ++ x1;
        }
    }
}
    
void print(int n){
    int i;
    puts("\n--------------------------------------");
    for (i = 1; i < N[n]; ++ i){
        printf("%d %d\n", C[i].x, C[i].y);
    }
}
    
int solve(){
    int ans = 0, m, nm, i, k, x, y;
    m = 0;
    nm = 1;
    while (!Set[m].empty()){
        ++ ans;
        //if (ans > 10) break;
        N[nm] = 1;
        Set[nm].clear();
        C = Q[m];
        //print(m);
        for (i = 1; i < N[m]; ++ i){
            x = Q[m][i].x;
            y = Q[m][i].y;
            C[0].x = x + 1;
            C[0].y = y - 1;
            P = Set[m].find(0);
            if (P != Set[m].end()){
                C[0].x = x + 1;
                C[0].y = y;
                P = Set[m].find(0);
                if (P == Set[m].end()){
                    Q[nm][N[nm]].x = x + 1;
                    Q[nm][N[nm]].y = y;
                    C = Q[nm];
                    //printf("### %d %d\n", x+1, y);
                    Set[nm].insert(N[nm]);
                    ++ N[nm];
                    C = Q[m];
                }
            }
            
            C[0].x = x;
            C[0].y = y - 1;
            P = Set[m].find(0);
            if (P == Set[m].end()){
                C[0].x = x - 1;
                C[0].y = y;
                P = Set[m].find(0);
                if (P == Set[m].end()){
                    continue;
                }
            }
            Q[nm][N[nm]].x = x;
            Q[nm][N[nm]].y = y;
            C = Q[nm];
            //printf("## %d %d\n", x, y);
            Set[nm].insert(N[nm]);
            ++ N[nm];
            C = Q[m];
        }
        m ^= 1;
        nm ^= 1;
    }
    
    return ans;
}

int main(){
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int T, ti = 0;
    scanf("%d", &T);
    while (T --){
        input();
        printf("Case #%d: %d\n", ++ ti, solve());
    }
    return 0;
}
