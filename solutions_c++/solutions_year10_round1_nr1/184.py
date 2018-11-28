#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const int dx[4] = {1,0,1,1};
const int dy[4] = {0,1,-1,1};
const int maxn = 60;
char a[maxn][maxn],b[maxn][maxn];
int n,m;

int check(int x,int y,int d){
    for (int i=0; i<m; ++i){
        if (x+dx[d]*i <= 0 || x+dx[d]*i > n) return false;
        if (y+dy[d]*i <= 0 || y+dy[d]*i > n) return false;
        if (a[x][y] != a[x+dx[d]*i][y+dy[d]*i]) return false;
    }
    return true;
}

int main()
{
    freopen("A.in","r",stdin); freopen("A.out","w",stdout);
    int t; scanf("%d\n",&t);
    for (int casenum=1; casenum <= t; ++casenum){
        scanf("%d %d\n",&n,&m);
        for (int i=1; i<=n; ++i)
            for (int j=1; j<=n; ++j)
                a[i][j] = '.';
        for (int i=1; i<=n; ++i){
            for (int j=1; j<=n; ++j){
                scanf("%c",&b[i][j]);
                a[j][n-i+1] = b[i][j];
            }
            scanf("\n");
        }
        bool can = true;
        while (can){
            can = false;
            for (int i=n; i>=1; --i)
                for (int j=1; j<=n; ++j)
                    if (a[i][j] != '.'){
                        int x = i,y = j;
                        while (x < n && a[x+1][y] == '.'){
                            a[x+1][y] = a[x][y]; a[x][y] = '.'; x++;
                            can = true;
                        }
                    }
        }
        bool r = false,b = false;
        for (int i=1; i<=n; ++i)
            for (int j=1; j<=n; ++j)
                if (a[i][j] != '.'){
                    for (int k=0; k<4; ++k)
                        if (check(i,j,k)){
                            if (a[i][j] == 'R') r = true; else b = true;
                            break;
                        }
                }
        printf("Case #%d: ",casenum);
        if (!r && !b)
            printf("Neither\n");
        else if (r && b)
            printf("Both\n");
        else if (r) printf("Red\n");
            else printf("Blue\n");
    }
    return 0;
}
