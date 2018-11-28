#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define IMPNUM 100000

int main(){
    
    int c;
    
    scanf("%d", &c);
    
    for (int casno = 1; casno <= c; casno ++){
        int m, v;
        int gate[20000], node[20000], chan[20000];
        
        scanf("%d %d", &m, &v);
        for (int i = 1; i <= (m - 1) / 2; i ++){
            scanf("%d %d", &gate[i], &chan[i]);
            node[i] = -1;
        }
        
        for (int i = (m + 1) / 2; i <= m; i ++){
            scanf("%d", &node[i]);
            chan[i] = 0;
        } 

        int d[20000][2];
        memset(d, 0, sizeof(d));
        
        for (int i = (m + 1) / 2; i <= m; i ++){
            d[i][node[i]] = 0;
            d[i][1 - node[i]] = IMPNUM;
        }
            
        for (int i = (m - 1) / 2; i >= 1; i --){
            d[i][0] = d[i][1] = IMPNUM;
            
            for (int j = 0; j <= 1; j ++){
                for(int k = 0; k <= 1; k ++){
                        if (gate[i] == 1){
                           d[i][j & k] = min(d[i][j & k], d[2 * i][j] + d[2 * i + 1][k]);
                           if (chan[i] == 1)
                              d[i][j | k] = min(d[i][j | k], d[2 * i][j] + d[2 * i + 1][k] + 1);
                           }
                        else{
                           if (chan[i] == 1)
                              d[i][j & k] = min(d[i][j & k], d[2 * i][j] + d[2 * i + 1][k] + 1);
                           d[i][j | k] = min(d[i][j | k], d[2 * i][j] + d[2 * i + 1][k]);
                           }
                }
            }
        }
        
        if (d[1][v] >= IMPNUM)
           printf("Case #%d: IMPOSSIBLE\n", casno);
        else
            printf("Case #%d: %d\n", casno, d[1][v]);
        
    }
    
    return 0;
}
                        
