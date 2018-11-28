#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const int maxn = 105;
const int inf = 2147483647/2;
int pos[maxn][2];
int q[maxn*maxn*maxn][3],f[maxn][maxn][maxn];

void update(int data,int x,int y,int p,int tail){
    f[x][y][p] = data;
    q[tail][0] = x; q[tail][1] = y; q[tail][2] = p;
}

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;
    cin >> T;
    for (int casenum = 1; casenum <= T; ++casenum){
        int n;
        cin >> n;
        for (int i=1; i<=n; ++i){
            char ch;
            cin >> ch >> pos[i][1];
            if (ch == 'O')
                pos[i][0] = 0;
            else pos[i][0] = 1;
        }
        for (int i=1; i<=100; ++i)
            for (int j=1; j<=100; ++j)
                for (int k=1; k<=n; ++k)
                    f[i][j][k] = inf;
        f[1][1][1] = 0;
        int head = 0,tail = 0;
        q[head][0] = 1; q[head][1] = 1; q[head][2] = 1;
        int ans;
        while (head <= tail){
            int x = q[head][0], y = q[head][1], p = q[head][2], d = f[x][y][p];
            if (pos[p][0] == 0 && x == pos[p][1]){
                if (p == n){
                    ans = d + 1; break;
                }
                for (int i=-1; i<=1; ++i)
                    if (y+i > 0 && y + i <= 100 && d + 1 < f[x][y+i][p+1])
                        update(d+1,x,y+i,p+1,++tail);
            }
            if (pos[p][0] == 1 && y == pos[p][1]){
                if (p == n){
                    ans = d + 1; break;
                }
                for (int i=-1; i<=1; ++i)
                    if (x+i > 0 && x + i <= 100 && d + 1 < f[x+i][y][p+1])
                        update(d+1,x+i,y,p+1,++tail);
            }
            for (int d1 = -1; d1 <= 1; ++d1)
                for (int d2 = -1; d2 <=1; ++d2)
                    if (x + d1 > 0 && x + d1 <= 100 && y + d2 > 0 && y + d2 <= 100 && d + 1 < f[x+d1][y+d2][p])
                        update(d+1,x+d1,y+d2,p,++tail);
            head++;
        }
        printf("Case #%d: %d\n",casenum,ans);
    }
    return 0;
}
