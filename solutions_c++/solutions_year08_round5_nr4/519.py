#include <cstdio>
#include <cstring>
#include <queue>

#define MAXW 105
#define MAXH 105

using namespace std;

int sol[MAXW][MAXH];

int main(){
    int tc, tcc = 0;
    for (scanf("%d", &tc); tc; --tc){
        memset(sol, 0, sizeof(sol));
        
        int h, w, r;
        scanf("%d %d %d", &h, &w, &r);
        
        for (int i = 0; i < r; i++){
            int x, y;
            scanf("%d %d", &x, &y);
            sol[x - 1][y - 1] = -1;
        }
        
        sol[0][0] = 1;
        for (int i = 0; i < h; i++)
            for (int j = 0; j < w; j++){
                if ( sol[i][j] == -1 ) continue;
                if ( i > 0 && j > 1 && sol[i - 1][j - 2] != -1 ) sol[i][j] = (sol[i][j] + sol[i - 1][j - 2]) % 10007;
                if ( i > 1 && j > 0 && sol[i - 2][j - 1] != -1 ) sol[i][j] = (sol[i][j] + sol[i - 2][j - 1]) % 10007;
            }
                
        printf("Case #%d: %d\n", ++tcc, sol[h - 1][w - 1] % 10007);
    }    
    return 0;
}
