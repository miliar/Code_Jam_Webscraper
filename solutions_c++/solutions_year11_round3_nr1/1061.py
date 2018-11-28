#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
    int T;

    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++){
        int r, c;
        char a[60][60];

        scanf("%d%d", &r, &c);
        for (int i = 0; i < r; i++)
            scanf("%s", a[i]);
        for (int i = 1; i < r; i++)
            for (int j = 0; j < c - 1; j++)
                if (a[i][j] == '#' && a[i][j+1] == '#' &&
                     a[i-1][j] == '#' && a[i-1][j+1] == '#'){
                    a[i-1][j]='/';
                    a[i-1][j+1] = '\\';
                    a[i][j] = '\\';
                    a[i][j+1] = '/';
                }
        bool flag = 1;
        for (int i = 0;i < r; i++)
            for (int j = 0; j < c; j++)
                if (a[i][j] == '#') {
                    flag = 0;
                    break;
                }
        printf("Case #%d:\n", cas);
        if (flag){
            for (int i = 0; i < r; i++)
                printf("%s\n", a[i]);
        }else printf("Impossible\n");
    }

    return 0;
}