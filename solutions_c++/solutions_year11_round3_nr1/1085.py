#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
    int n, r, c;
    int flag, con = 1;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &n);
    while(n--){
        char grid[60][60];
        scanf("%d %d", &r, &c);
        for(int i = 0; i < r; i++)
            scanf("%s", grid[i]);
        flag = 0;
        for(int i = 0; i < r; i++){
            for(int j = 0; j < c; j++){
                if(grid[i][j] == '#'){
                    if(i < r - 1 && j < c - 1){
                        if(grid[i][j + 1] == '#' && grid[i + 1][j] == '#' && grid[i + 1][j + 1] == '#'){
                            grid[i][j] = '/';
                            grid[i][j + 1] = '\\';
                            grid[i + 1][j] = '\\';
                            grid[i + 1][j + 1] = '/';
                        }else flag = 1;
                    }else flag = 1;
                }
                if(flag) break;
            }
            if(flag) break;
        }
        printf("Case #%d:\n", con++);
        if(flag) printf("Impossible\n");
        else {
            for(int i = 0; i < r; i++)
                printf("%s\n", grid[i]);
        }
    }
    return 0;
}
