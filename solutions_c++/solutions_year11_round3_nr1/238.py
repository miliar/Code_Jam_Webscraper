#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
#include <algorithm>
#include <cmath>

using namespace std;

int t, n, m, ok;
char a[55][55], sol[55][55];

int main(){
    //freopen("A.in", "r", stdin);
    //freopen("A.out", "w", stdout);
    scanf("%d", &t);
    for (int tc=1; tc<=t; tc++){
        memset(sol, '.', sizeof sol);
        ok=true;
        scanf("%d %d", &n, &m);
        for (int i=1; i<=n; i++)
            scanf("%s", a[i]+1);
        for (int i=1; i<=n and ok; i++)
            for (int j=1; j<=m; j++)
                if (a[i][j]=='#' and sol[i][j]=='.'){
                    if (i==n or j==m){
                        ok=false;
                        break;
                    }
                    if (sol[i+1][j]!='.' or sol[i][j+1]!='.' or sol[i+1][j+1]!='.'){
                        ok=false;
                        break;
                    }
                    if (a[i+1][j]!='#' or a[i][j+1]!='#' or a[i+1][j+1]!='#'){
                        ok=false;
                        break;
                    }
                    sol[i][j]=47;
                    sol[i+1][j]=92;
                    sol[i][j+1]=92;
                    sol[i+1][j+1]=47;
                }

        printf("Case #%d:\n", tc);
        if (!ok)
            printf("Impossible\n");
        else
            for (int i=1; i<=n; i++){
                for (int j=1; j<=m; j++)
                    printf("%c", sol[i][j]);
                printf("\n");
            }
    }
	return 0;
}
