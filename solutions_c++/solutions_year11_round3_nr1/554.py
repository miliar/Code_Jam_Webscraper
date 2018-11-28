#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
char map[55][55];


int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int ct = 1, T, n, m, i, j, rb, ctmp, f;
    scanf("%d",&T);
    while (T--) {
        scanf("%d %d",&n,&m);
        f = 0;
        for (i = 0; i < n; ++i) {
            scanf("%s",map[i]);
            ctmp = 0;
            for (j = 0; j < m; ++j) {
                if (map[i][j] == '#') ctmp++;
            }
            if (ctmp % 2 == 1 && f == 0) f = 1;
        }
        printf("Case #%d:\n",ct++);
        if (f == 1) {
            printf("Impossible\n");
            continue;
        }
        
        for (i = 0; i < (n - 1); ++i) {
            for (j = 0; j < (m - 1); ++j) {
                if (   map[i][j] == '#' && map[i][j+1] == '#' 
                    && map[i+1][j] == '#' && map[i+1][j+1] == '#') {
                    
                    map[i][j] =   '//'; 
                    map[i+1][j+1] = '//'; 
                    map[i+1][j] = '\\';
                    map[i][j+1] = '\\';
                }
            }
        }
        
        f = 0;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                if (map[i][j] == '#') {
                    f = 1;
                    break;
                }
            }
        }
        
        if (f == 1) {
            printf("Impossible\n");
        }
        else {
             for (i = 0; i < n; ++i) {
                 printf("%s\n",map[i]);
             }        
        }
    }
    return 0;
}
