#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<cstdio>

#define INF 1000000

using namespace std;

int tree[11000];
int change[11000];
int best[2][11000];
int m, n, v;
int t;



int main() {
    int i, j;
    scanf("%d", &n);
    for (t=0; t<n; t++) {
        scanf("%d %d\n", &m, &v);
        for (i=0; i<m/2; i++) {
            scanf("%d %d\n", &tree[i], &change[i]);
        }
        for (; i<m; i++) {
            scanf("%d\n", &tree[i]);
            best[tree[i]][i]=0;
            best[1-tree[i]][i]=INF;
        }
        for (i=m/2-1; i>=0; i--){
            if (tree[i]==1) {
               best[0][i] = min(best[0][2*i+1],best[0][2*i+2]);
               best[1][i] = min(best[1][2*i+1]+best[1][2*i+2], INF);
               if (change[i]==1) {
                  best[1][i] = min(best[1][i],
                  1+min(best[1][2*i+1],best[1][2*i+2]));
               }
            }
            else {
               best[1][i] = min(best[1][2*i+1],best[1][2*i+2]);
               best[0][i] = min(best[0][2*i+1]+best[0][2*i+2], INF);
               if (change[i]==1) {
                  best[0][i] = min(best[0][i],
                  1+min(best[0][2*i+1],best[0][2*i+2]));
               }
            }
        }
        if (best[v][0] < INF) {
           printf("Case #%d: %d\n", t+1, best[v][0]);
        }
        else
           printf("Case #%d: IMPOSSIBLE\n", t+1);        
    }
    return 0;    
}


