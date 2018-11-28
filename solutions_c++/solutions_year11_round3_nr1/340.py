#include <cstdio>
#include <iostream>
#include <cmath>
using namespace std;

char mat[100][100];
void solve()
{
    int r, c;
    scanf("%d %d", &r, &c);
    
    getchar();
    for(int i = 0; i < r; i++) {
        for(int j = 0; j < c; j++) {
            mat[i][j] = getchar();
        }
        getchar();
    }
    
    bool flag = true;
    for(int i = 0; i < r; i++) {
        for(int j = 0; j < c; j++) {
            if (mat[i][j] == '#') {
                if (i + 1 >= r || j + 1 >= c) {
                    flag = false;
                    break;
                }
                if (mat[i+1][j] != '#' || mat[i][j+1] != '#' || mat[i+1][j+1] != '#') {
                    flag = false;
                    break;
                }
                mat[i][j] = '/';
                mat[i][j+1] = '\\';
                mat[i+1][j] = '\\';
                mat[i+1][j+1] = '/';
            }
        }
    }
    
    if(flag) {
        for(int i = 0; i < r; i++) {
            for(int j = 0; j < c; j++) {
                putchar(mat[i][j]);
            }
            putchar(10);
        }
    } else {
        printf("Impossible\n");
    }
}
 
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    
    int T;
    scanf("%d", &T);
    
    for (int i = 1; i <= T; i++)
    {
        printf("Case #%d:\n", i);
        solve();
    }
    return 0;
}
