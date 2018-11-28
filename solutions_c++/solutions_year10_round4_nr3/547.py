#include <cstdio>
#include <cstring>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

int r, n=0, m=0;

bool a[111][128];

int reduce(){
    int res = 0;
    for (int i=n; i>0; i--)
        for (int j=m; j>0; j--){
            res |= a[i][j];
            if (a[i][j])
                a[i][j] = a[i-1][j] | a[i][j-1];
            else
                a[i][j] = a[i-1][j] & a[i][j-1];
        }
    return res;
}

void solve(int tst)
{
    printf("Case #%d: ", tst);
    memset(a, 0, sizeof(a));
    n = 0, m = 0;
    scanf("%d", &r);
    for (int i=0; i<r; i++){
        int x1, y1, x2, y2;
        scanf("%d %d %d %d\n", &x1, &y1, &x2, &y2);
        for (int x=x1; x<=x2; x++)
            for (int y=y1; y<=y2; y++)
                a[x][y] = true;
        if (x2 > n)
            n = x2;
        if (y2 > m)
            m = y2;
    }
    int sol = 0;
    while (reduce()){
        sol++;
    }
    printf("%d\n", sol);
}

int main()
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    int tst;
    scanf("%d", &tst);
    for (int i=1; i<=tst; i++)
        solve(i);
    return 0;
}
