#include <algorithm>
#include <cstring>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>

using namespace std;

int T, R, C;
char pic[52][52];

int main() {
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cin >> R >> C;
        memset(pic, 0, sizeof(pic));
        for (int j = 0; j < R; j++) {
            scanf("\n");
            for (int k = 0; k < C; k++) {
                scanf("%c", &pic[j][k]);
            }
        }
        
        for (int j = 0; j < R-1; j++) {
            for (int k = 0; k < C-1; k++) {
                if (pic[j][k] == '#' && pic[j+1][k] == '#' && pic[j][k+1] == '#' && pic[j+1][k+1] == '#') {
                    pic[j][k] = pic[j+1][k] = pic[j][k+1] = pic[j+1][k+1] = '*';
                }
            }
        }
        
        bool impo = true;
        for (int j = 0; j < R; j++) {
            for (int k = 0; k < C; k++) {
                if (pic[j][k] == '#') {
                    impo = false;
                    break;
                }
            }
            if (!impo) break;
        }
        
        printf("Case #%d:\n", i);
        if (!impo) {
            printf("Impossible\n");
        } else {
            int count = 0;
            for (int j = 0; j < R; j++) {
                for (int k = 0; k < C; k++) {
                    if (pic[j][k] == '*' && j<R-1 && k<C-1) {
                        pic[j][k] = pic[j+1][k+1] = '/';
                        pic[j+1][k] = pic[j][k+1] = '\\';
                    }
                    putchar(pic[j][k]);
                }
                puts("");
            }
        }
    }
    return 0;
}

