#include <cstdio>
#include <algorithm>
using namespace std;

#define Max 52

int T, R, C;
char table[Max][Max];

int main() {
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d\n", &T);
    for (int xxx = 1; xxx <= T; xxx++) {
        for (int i = 0; i < Max; i++)
            for(int j = 0; j < Max; j++)
                table[i][j] = '.';
        scanf("%d%d\n", &R, &C);
        for (int i = 1; i <= R; i++) {
            for (int j = 1; j <= C; j++)
                scanf("%c", &table[i][j]);
            scanf("\n");    
        }
        printf("Case #%d:\n", xxx);
        int c = 0;
        for (int i = 1; i <= R; i++)
            for (int j = 1; j <= C; j++)
                if (table[i][j] == '#') c++;
        
        bool found = true;
        while (found && c > 0) {
            found = false;
            for (int i = 1; i <= R && !found; i++)
                for (int j = 1; j <= C && !found; j++) 
                    if (table[i][j] == '#' &&
                        table[i+1][j] == '#' &&
                        table[i][j+1] == '#' &&
                        table[i+1][j+1] == '#') {
                            found = true;
                            table[i][j] = table[i+1][j+1] = '/';
                            table[i+1][j] = table[i][j+1] = '\\';
                            c -= 4;
                        }
        }
        if (c > 0) 
            printf("Impossible\n");
        else {
            for (int i = 1; i <= R; i++) {
                for (int j = 1; j <= C; j++)
                    printf("%c", table[i][j]);
                printf("\n");
            }
        }
    }
    return 0;    
}
