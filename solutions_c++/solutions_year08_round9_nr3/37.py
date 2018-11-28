#include <stdio.h>
#include <algorithm>
#include <set>
#define eps (1.0e-5)

using namespace std;

int data[50][50];
int choice[50][50];
int n, m, best;

int check () {
    int f = 1;
    for (int i = 0; i < n; i ++)
        for (int j = 0; j < m; j ++) {
            int tot = data[i][j];
            for (int k = (i - 1 >? 0); k <= (i + 1 <? n - 1); k ++)
                for (int l = (j - 1 >? 0); l <= (j + 1 <? m - 1); l ++)
                    tot -= choice[k][l];
            if (tot)
                return 0;
            }
    int cn = 0;
    
    for (int j = 0; j < m; j ++)
        cn += choice[n/2][j];
    return cn;
    }

void dfs (int x, int y) {
//    printf("dfs %d %d\n",x,y);
    if (x == n) {
        best >?= check();
        return;
        }
    choice[x][y] = 0;
    dfs(x + (y + 1) / m, (y + 1) % m);
    choice[x][y] = 1;
    dfs(x + (y + 1) / m, (y + 1) % m);
    }

int main () {
    int ct = 0, t;
    
    freopen("c.in", "r", stdin);
    freopen("c_bf.out", "w", stdout);
    
    for (scanf("%d", &t); t > 0; t --) {
        scanf("%d%d",&n,&m);
        for (int i = 0; i < n; i ++)
            for (int j = 0; j < m; j ++)
                scanf("%d", data[i] + j);
        
        best = 0;
        dfs(0,0);
            
        printf("Case #%d: %d\n", ++ct, best);
        }
   
    return 0;
    }
